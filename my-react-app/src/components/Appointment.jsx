import React, { useEffect, useState } from "react";
import DataTable from "react-data-table-component";

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

  // Define columns for DataTable
  const columns = [
    {
      name: "Date",
      selector: (row) => row.date,
      sortable: true,
    },
    {
      name: "Time",
      selector: (row) => row.time.slice(0, 5),
      sortable: true,
    },
    {
      name: "Duration",
      selector: (row) => row.duration,
    },
    {
      name: "Services",
      selector: (row) => row.services.map((svc) => svc.name).join(", "),
    },
    {
      name: "Status",
      selector: (row) => row.status,
    },
    {
      name: "Notes",
      selector: (row) => row.notes,
    },
    {
      name: "Actions",
      cell: (row) => (
        <>
          <button style={{ marginRight: "10px" }}>Edit</button>
          <button style={{ color: "red" }}>Cancel</button>
        </>
      ),
    },
  ];

  return (
    <main style={{ padding: "20px" }}>
      {loading && <p>Loading appointments...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {!loading && !error && (
        <DataTable
          title="Appointments"
          columns={columns}
          data={appointments}
          pagination
          highlightOnHover
          striped
        />
      )}
    </main>
  );
}
