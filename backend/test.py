import requests


url = "http://127.0.0.1:5000/chat"


questions = [
    "Where can I borrow books?",
    "Where is the MCA department?",
    "Where do I go for campus placements?",
    "Where can I eat?",
    "Where is the basketball court?"
]


for question in questions:

    response = requests.post(
        url,
        json={
            "query": question
        }
    )

    print("=" * 60)

    print("QUESTION:")
    print(question)

    print("\nRESPONSE:")

    print(response.json())