import React from "react";
import "./sliderbar.css";

function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar-header">Salonify</div>
      <nav className="sidebar-nav">
        <a href="/owner/dashboard" className="sidebar-link">Dashboard</a>
        <a href="/owner/appointment" className="sidebar-link">Appointment</a>
        <a href="/owner/service" className="sidebar-link">Services</a>
        <a href="/owner/settings" className="sidebar-link">Settings</a>
      </nav>
    </aside>
  );
}

export default Sidebar;
