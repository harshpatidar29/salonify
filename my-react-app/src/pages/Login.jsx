// src/pages/Login.jsx
import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "./Login.css";

function Login() {
  const [form, setForm] = useState({ username: "", password: "" });
  const [message, setMessage] = useState("");
  const navigate = useNavigate(); 

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("");

    const formData = new URLSearchParams();
    formData.append("username", form.username);
    formData.append("password", form.password);

    try {
      const res = await axios.post("http://127.0.0.1:8000/auth/login", formData, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      });

      const token = res.data.access_token;
      localStorage.setItem("token", res.data.access_token);

      const userRes = await axios.get("http://127.0.0.1:8000/protected/", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const user = userRes.data;
      const role = user.role;

      if (role === "owner") {
        navigate("/owner/dashboard");
      } else {
        navigate("/");
      }
    } catch (err) {
      setMessage("❌ Login failed: Invalid credentials.");
    }
  };

  return (
    <div className="login-container">
      <form className="login-form" onSubmit={handleSubmit}>
        <h2>Salonify Login</h2>

        <input
          type="text"
          name="username"
          placeholder="Username"
          value={form.username}
          onChange={handleChange}
          required
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={form.password}
          onChange={handleChange}
          required
        />

        <button type="submit">Login</button>

        {message && <p className="message">{message}</p>}
      </form>
    </div>
  );
}

export default Login;
