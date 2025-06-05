import React, { useEffect, useState } from "react";

export default function Staffs() {
  const [staff, setStaff] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchStaff = async () => {
      try {
        const token = localStorage.getItem("token");

        const response = await fetch("http://127.0.0.1:8000/staff/salon/ab1b6778-8000-4367-bddc-9b733120fa0d", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (!response.ok) {
          throw new Error("Failed to fetch services");
        }

        const data = await response.json();
        setStaff(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchStaff();
  }, []);

  return (
    <>
      <main style={{ padding: "20px" }}>

        {loading && <p>Loading services...</p>}
        {error && <p style={{ color: "red" }}>{error}</p>}

        {!loading && !error && staff.length === 0 && (
          <p>No staff found.</p>
        )}

        <div style={gridStyle}>
          {staff.map((staff) => (
            <div key={staff.id} style={cardStyle}>
              <h3>{staff.name}</h3>
              <p>{staff.role}</p>
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
