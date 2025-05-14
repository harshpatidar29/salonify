import React, { useEffect } from "react";
import { useNavigate, Outlet } from "react-router-dom";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Slidbar";
import { isTokenValid } from "../utils/auth";

export default function OwnerLayout() {
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
      <Navbar />
      <Sidebar />
      <main style={{ marginLeft: '220px', marginTop: '60px', padding: '20px' }}>
        <Outlet />
      </main>
    </>
  );
}
