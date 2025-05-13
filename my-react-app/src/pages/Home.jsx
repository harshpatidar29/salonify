// src/pages/Home.jsx
import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Navbar from '../components/Navbar';

function Home() {
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      navigate("/login");
    }
  }, [navigate]);

  return (
    <>
      <Navbar />
      <main style={{ padding: "20px" }}>
        <h1>Welcome to SalonApp</h1>
        <p>Your one-stop destination for all your salon needs!</p>
      </main>
    </>
  );
}

export default Home;
