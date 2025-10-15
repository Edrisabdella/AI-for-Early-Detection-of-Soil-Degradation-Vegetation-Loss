import React, { useRef, useEffect, useState } from "react";
import mapboxgl from "mapbox-gl";

mapboxgl.accessToken = process.env.MAPBOX_TOKEN || "";

export default function MapView() {
  const mapContainer = useRef(null);
  const map = useRef(null);
  const [lng] = useState(39.8);
  const [lat] = useState(9.0);
  const [zoom] = useState(6);

  useEffect(() => {
    if (map.current) return;
    map.current = new mapboxgl.Map({
      container: mapContainer.current,
      style: "mapbox://styles/mapbox/satellite-streets-v12",
      center: [lng, lat],
      zoom: zoom,
    });

    map.current.on("load", () => {
      map.current.addControl(new mapboxgl.NavigationControl());
    });

    return () => {
      if (map.current) map.current.remove();
    };
  }, [lng, lat, zoom]);

  return <div ref={mapContainer} className="map-container" />;
}
