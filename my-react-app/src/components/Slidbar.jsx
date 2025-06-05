// src/components/Sidebar.jsx
import React from "react";
import { Link } from "react-router-dom";
import "./sliderbar.css";

function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar-header">Salonify</div>
      <nav className="sidebar-nav">
        <Link to="/owner/dashboard" className="sidebar-link">Dashboard</Link>
        <Link to="/owner/appointment" className="sidebar-link">Appointment</Link>
        <Link to="/owner/service" className="sidebar-link">Services</Link>
        <Link to="/owner/staff" className="sidebar-link">staff</Link>
        <Link to="/owner/settings" className="sidebar-link">Settings</Link>
      </nav>
    </aside>
  );
}

export default Sidebar;
