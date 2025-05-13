import React, { useEffect, useState } from "react";
import Navbar from "../components/Navbar";

export default function Appointments() {
  const [appointments, setAppointments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAppointments = async () => {
      try {
        const token = localStorage.getItem("token");

        const response = await fetch("http://localhost:8000/appointments/", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (!response.ok) {
          throw new Error("Failed to fetch appointments");
        }

        const data = await response.json();
        setAppointments(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchAppointments();
  }, []);

  return (
    <>
      <Navbar />
      <main style={{ padding: "20px" }}>
        <h1>Appointments</h1>
        <button
          style={{
            marginBottom: "20px",
            padding: "10px 20px",
            backgroundColor: "#007bff",
            color: "white",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
          }}
        >
          + New Appointment
        </button>

        {loading && <p>Loading appointments...</p>}
        {error && <p style={{ color: "red" }}>{error}</p>}

        {!loading && !error && appointments.length === 0 && (
          <p>No appointments found.</p>
        )}

        {!loading && !error && appointments.length > 0 && (
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr style={{ backgroundColor: "#f0f0f0" }}>
                <th style={thStyle}>Date</th>
                <th style={thStyle}>Time</th>
                <th style={thStyle}>Duration</th>
                <th style={thStyle}>Services</th>
                <th style={thStyle}>Status</th>
                <th style={thStyle}>Notes</th>
                <th style={thStyle}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {appointments.map((appt) => (
                <tr key={appt.id}>
                  <td style={tdStyle}>{appt.date}</td>
                  <td style={tdStyle}>{appt.time.slice(0, 5)}</td>
                  <td style={tdStyle}>{appt.duration}</td>
                  <td style={tdStyle}>
                    {appt.services.map((svc) => svc.name).join(", ")}
                  </td>
                  <td style={tdStyle}>{appt.status}</td>
                  <td style={tdStyle}>{appt.notes}</td>
                  <td style={tdStyle}>
                    <button style={{ marginRight: "10px" }}>Edit</button>
                    <button style={{ color: "red" }}>Cancel</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </main>
    </>
  );
}

// Reusable styles
const thStyle = {
  padding: "10px",
  border: "1px solid #ccc",
};

const tdStyle = {
  padding: "10px",
  border: "1px solid #ccc",
};
