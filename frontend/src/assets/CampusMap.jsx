function CampusMap({ destination }) {
  return (
    <div className="campus-map">
      <div className="map-title">📍 Campus Navigation Map</div>

      <div className="map-area">
        <div className="map-location main-gate">
          🚪
          <span>Main Gate</span>
        </div>

        <div className="map-line line-one"></div>

        <div className="map-location academic">
          🏫
          <span>Academic Block</span>
        </div>

        <div className="map-location library">
          📚
          <span>Central Library</span>
        </div>

        <div className="map-location sports">
          🏀
          <span>Sports Area</span>
        </div>

        <div className="map-location cafeteria">
          🍴
          <span>Cafeteria</span>
        </div>

        <div className="map-location destination">
          📍
          <span>{destination || "Destination"}</span>
        </div>
      </div>
    </div>
  );
}

export default CampusMap;
