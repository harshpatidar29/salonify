import React, { useEffect, useState } from 'react';
import './Dashboardcard.css';

function DashboardCards() {
  const [stats, setStats] = useState({
    todayAppointments: 0,
    totalServices: 0,
    todayRevenue: 0,
    monthlyRevenue: 0,
  });

  useEffect(() => {
    // Replace with your API endpoint
    fetch('http://localhost:8000/appointment')
      .then(res => res.json())
      .then(data => {
        setStats(data);
      })
      .catch(err => {
        console.error('Failed to load stats:', err);
      });
  }, []);

  return (
    <div class="dashboard-cards">
      <div class="card">
        <div class="icon">✅</div>
        <div class="text">
          <h4>Total Appointments</h4>
          <p>45</p>
        </div>
      </div>

      <div class="card">
        <div class="icon">💰</div>
        <div class="text">
          <h4>Today's Revenue</h4>
          <p>$1,250</p>
        </div>
      </div>

      <div class="card">
        <div class="icon">👥</div>
        <div class="text">
          <h4>Total Staff</h4>
          <p>8</p>
        </div>
      </div>

      <div class="card">
        <div class="icon">💇‍♀️</div>
        <div class="text">
          <h4>Services Booked</h4>
          <p>12</p>
        </div>
      </div>
    </div>
  );
}

export default DashboardCards;
