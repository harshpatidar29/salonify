import './App.css';
import React from 'react';
import { Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Home from "./pages/Home";
import Service from "./components/Service";
import Appointment from "./components/Appointment";

function App() {
  return (
      <Routes>      
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/services" element={<Service />} />
        <Route path="/appointments" element={<Appointment />} />
      </Routes>
  );
}

export default App;
