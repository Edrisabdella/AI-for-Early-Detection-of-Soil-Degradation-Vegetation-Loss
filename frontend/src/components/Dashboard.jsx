import React, { useState } from "react";
import axios from "axios";

export default function Dashboard() {
  const [fileNir, setFileNir] = useState(null);
  const [fileRed, setFileRed] = useState(null);
  const [result, setResult] = useState(null);

  const handlePredict = async () => {
    if (!fileNir || !fileRed) return alert("Upload both NIR and Red GeoTIFFs");
    const form = new FormData();
    form.append("nir", fileNir);
    form.append("red", fileRed);
    try {
      const res = await axios.post("http://localhost:8000/api/v1/predict/ndvi-patch", form, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Prediction failed. Check backend logs.");
    }
  };

  return (
    <aside className="dashboard">
      <h2>Predict Patch Risk</h2>
      <p>Upload small GeoTiff NIR and Red band files (patch ~64x64)</p>
      <input type="file" onChange={(e) => setFileNir(e.target.files[0])} />
      <input type="file" onChange={(e) => setFileRed(e.target.files[0])} />
      <button onClick={handlePredict}>Predict</button>
      {result && (
        <div className="result">
          <h3>Risk Score</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
      <div className="info">
        <h3>Contact</h3>
        <p>Edris Abdella — edrisabdella178@gmail.com</p>
      </div>
    </aside>
  );
}
