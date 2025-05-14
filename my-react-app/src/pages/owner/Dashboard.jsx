// src/pages/Home.jsx
import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Navbar from '../../components/Navbar';
import Sidebar from '../../components/Slidbar';
import DashboardCards from '../../components/DashboardCards';
import { isTokenValid } from "../../utils/auth";

export default function  OwnerDashboard() {
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token || !isTokenValid()) {
        localStorage.removeItem("token");
        navigate("/login");
    }
  }, [navigate]);

  return (
    <>
    <body>
      <Navbar />
      <Sidebar />
      <main style={{ marginLeft: '220px', marginTop: '0px', padding: '20px' }}>
        <section className="bg-blue-600 text-white py-8 px-6">
          <div className="max-w-6xl mx-auto">
            <h2 className="text-3xl font-semibold">Dashboard</h2>
          </div>
        </section>
        <DashboardCards />
      </main>
    </body>
    </>
  );
}

