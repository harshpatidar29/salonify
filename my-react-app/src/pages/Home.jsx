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
      <section className="bg-blue-600 text-white py-8 px-6">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-semibold">Welcome Back, Alex!</h2>
          <p className="text-blue-100 mt-2">Here’s your salon performance overview for today.</p>
        </div>
      </section>
    </>
  );
}

export default Home;
