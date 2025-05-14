import React, { useEffect, useState } from "react";
import Navbar from "../components/Navbar";

export default function Services() {
  const [services, setServices] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchServices = async () => {
      try {
        const token = localStorage.getItem("token");

        const response = await fetch("http://127.0.0.1:8000/service/all_service/", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (!response.ok) {
          throw new Error("Failed to fetch services");
        }

        const data = await response.json();
        setServices(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchServices();
  }, []);

  return (
    <>
      <Navbar />
      <main style={{ padding: "20px" }}>
        <h1>Our Services</h1>

        {loading && <p>Loading services...</p>}
        {error && <p style={{ color: "red" }}>{error}</p>}

        {!loading && !error && services.length === 0 && (
          <p>No services found.</p>
        )}

        <div style={gridStyle}>
          {services.map((service) => (
            <div key={service.id} style={cardStyle}>
              <h3>{service.name}</h3>
              <p>{service.description}</p>
              <p><strong>Price:</strong> ₹{service.price}</p>
              <p><strong>Duration:</strong> {service.duration}</p>
              <p><strong>Gender:</strong> {service.gender}</p>
              <p><strong>Status:</strong> {service.is_active ? "Active" : "Inactive"}</p>
            </div>
          ))}
        </div>
      </main>
    </>
  );
}

// CSS-in-JS styles
const gridStyle = {
  display: "grid",
  gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))",
  gap: "20px",
  marginTop: "20px",
};

const cardStyle = {
  border: "1px solid #ddd",
  borderRadius: "8px",
  padding: "16px",
  boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
  backgroundColor: "#fff",
};
