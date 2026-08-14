import { useState } from "react";
import {
  Send,
  MapPin,
  BookOpen,
  GraduationCap,
  Briefcase,
  Utensils,
  Dumbbell,
  Bot,
  User,
} from "lucide-react";

import "./App.css";

function App() {
  const [query, setQuery] = useState("");

  const [messages, setMessages] = useState([
    {
      type: "bot",
      text: "Hello! 👋 I am your Smart Campus Navigation Assistant. Ask me about departments, offices, facilities, libraries, sports areas and other campus locations.",
    },
  ]);

  const [loading, setLoading] = useState(false);

  // =====================================================
  // AI TYPING EFFECT
  // =====================================================

  const typeResponse = (text, locationData = {}) => {
    let index = 0;

    setMessages((prev) => [
      ...prev,
      {
        type: "bot",
        text: "",
        ...locationData,
      },
    ]);

    const interval = setInterval(() => {
      index++;

      setMessages((prev) => {
        const updated = [...prev];

        updated[updated.length - 1] = {
          type: "bot",
          text: text.substring(0, index),
          ...locationData,
        };

        return updated;
      });

      if (index >= text.length) {
        clearInterval(interval);
        setLoading(false);
      }
    }, 20);
  };

  // =====================================================
  // SEND QUERY TO FLASK
  // =====================================================

  const sendQuery = async (questionFromButton = null) => {
    const question = (
      questionFromButton !== null ? questionFromButton : query
    ).trim();

    console.log("QUESTION:", question);

    if (!question || loading) {
      return;
    }

    // Add user's message
    setMessages((prev) => [
      ...prev,
      {
        type: "user",
        text: question,
      },
    ]);

    setQuery("");
    setLoading(true);

    try {
      console.log("Sending request to Flask...");

      const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          query: question,
        }),
      });

      console.log("HTTP STATUS:", response.status);

      const data = await response.json();

      console.log("FLASK RESPONSE:", data);

      if (data.success && data.response) {
        console.log("AI RESPONSE:", data.response);

        typeResponse(data.response, {
          destination: data.destination,
          building: data.building,
          category: data.category,
          floor: data.floor,
          confidence: data.confidence,
          route: data.route,
        });
      } else {
        typeResponse(
          data.message || "Sorry, I could not identify that campus location.",
        );
      }
    } catch (error) {
      console.error("BACKEND CONNECTION ERROR:", error);

      setLoading(false);

      setMessages((prev) => [
        ...prev,
        {
          type: "bot",
          text: "I couldn't connect to the campus navigation service. Please make sure the Flask backend is running.",
        },
      ]);
    }
  };

  // =====================================================
  // ENTER KEY
  // =====================================================

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();

      sendQuery();
    }
  };

  // =====================================================
  // QUICK QUESTIONS
  // =====================================================

  const quickQuestions = [
    {
      label: "Library",
      question: "Where can I borrow books?",
      icon: <BookOpen size={18} />,
    },

    {
      label: "Departments",
      question: "Where is the MCA department?",
      icon: <GraduationCap size={18} />,
    },

    {
      label: "Placements",
      question: "Where do I go for campus placements?",
      icon: <Briefcase size={18} />,
    },

    {
      label: "Food",
      question: "Where can I eat?",
      icon: <Utensils size={18} />,
    },

    {
      label: "Sports",
      question: "Where is the basketball court?",
      icon: <Dumbbell size={18} />,
    },
  ];

  // =====================================================
  // UI
  // =====================================================

  return (
    <div className="app">
      {/* HEADER */}

      <header className="header">
        <div className="brand">
          <div className="brand-icon">
            <MapPin size={26} />
          </div>

          <div>
            <h1>Smart Campus Navigator</h1>

            <p>Christ University • Central Campus</p>
          </div>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          AI Assistant Online
        </div>
      </header>

      {/* MAIN */}

      <main className="main">
        <section className="hero">
          <div className="hero-icon">
            <Bot size={42} />
          </div>

          <h2>Where do you want to go?</h2>

          <p>
            Ask me about departments, offices, facilities, libraries, sports
            areas and other campus locations.
          </p>
        </section>

        {/* QUICK NAVIGATION */}

        <section className="quick-section">
          <h3>Quick Navigation</h3>

          <div className="quick-buttons">
            {quickQuestions.map((item) => (
              <button
                key={item.label}
                className="quick-button"
                onClick={() => sendQuery(item.question)}
                disabled={loading}
              >
                {item.icon}

                {item.label}
              </button>
            ))}
          </div>
        </section>

        {/* CHAT */}

        <section className="chat-container">
          <div className="messages">
            {messages.map((message, index) => (
              <div key={index} className={`message-row ${message.type}`}>
                <div className="avatar">
                  {message.type === "bot" ? (
                    <Bot size={18} />
                  ) : (
                    <User size={18} />
                  )}
                </div>

                <div className="message-content">
                  <div className="message-text">{message.text}</div>

                  {/* LOCATION CARD */}

                  {message.destination && (
                    <div className="location-card">
                      <div className="location-header">
                        <div>
                          <h3>{message.destination}</h3>
                          <p>{message.building}</p>
                        </div>
                      </div>

                      <div className="location-answer">{message.response}</div>

                      {message.route && message.route.length > 0 && (
                        <div className="route-text">
                          <strong>Route:</strong> {message.route.join(". ")}.
                        </div>
                      )}
                    </div>
                  )}
                </div>
              </div>
            ))}

            {/* LOADING */}

            {loading && (
              <div className="message-row bot">
                <div className="avatar">
                  <Bot size={18} />
                </div>

                <div className="typing">AI is thinking...</div>
              </div>
            )}
          </div>

          {/* INPUT */}

          <div className="input-area">
            <input
              type="text"
              placeholder="Ask: Where is the MCA department?"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyDown={handleKeyDown}
              disabled={loading}
            />

            <button
              className="send-button"
              onClick={() => sendQuery()}
              disabled={loading || !query.trim()}
            >
              <Send size={20} />
            </button>
          </div>
        </section>
      </main>

      {/* FOOTER */}

      <footer>
        <Bot size={16} />
        AI-powered campus navigation • Sentence Transformers + FLAN-T5
      </footer>
    </div>
  );
}

export default App;
