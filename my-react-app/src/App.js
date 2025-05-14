import './App.css';
import React from 'react';
import { Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Logout from "./components/Logout";
import Home from "./pages/Home";
import Service from "./components/Service";
import Appointment from "./components/Appointment";
import OwnerDashboard from "./pages/owner/Dashboard";

function App() {
  return (
      <Routes>
        <Route path="/owner/dashboard" element={<OwnerDashboard />} />
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/services" element={<Service />} />
        <Route path="/appointments" element={<Appointment />} />
      </Routes>
  );
}

export default App;
