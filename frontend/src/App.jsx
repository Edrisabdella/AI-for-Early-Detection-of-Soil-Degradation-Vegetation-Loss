import React from "react";
import MapView from "./components/MapView";
import Dashboard from "./components/Dashboard";

export default function App() {
  return (
    <div className="app">
      <header className="header">
        <h1>Early Detection of Soil Degradation & Vegetation Loss</h1>
        <p>Project Lead: Edris Abdella — edrisabdella178@gmail.com</p>
      </header>
      <main className="main">
        <MapView />
        <Dashboard />
      </main>
    </div>
  );
}
