import React, { useEffect, useState } from 'react';
import './Dashboardcard.css';

function DashboardCards() {
  const [appointmentCount, setAppointmentCount] = useState(0);
  const [staffCount, setStaffCount] = useState(0);
  const [serviceCount, setServiceCount] = useState(0);

  useEffect(() => {
    fetch('http://localhost:8000/appointments/')
      .then(res => res.json())
      .then(data => {
        if (Array.isArray(data)) {
          setAppointmentCount(data.length);
        } else {
          console.error('Unexpected data format:', data);
        }
      })
      .catch(err => {
        console.error('Failed to load appointments:', err);
      });
  }, []);

  useEffect(() => {
    const token = localStorage.getItem('token');
  
    fetch('http://127.0.0.1:8000/SalonStaff/bca091a9-1bd3-4f80-97e7-11c8d31b088f', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
      .then(res => {
        if (!res.ok) {
          throw new Error('Not authenticated');
        }
        return res.json();
      })
      .then(data => {
        if (Array.isArray(data)) {
          setStaffCount(data.length);
        } else {
          console.error('Unexpected data format:', data);
        }
      })
      .catch(err => {
        console.error('Failed to load staff members:', err);
      });
  }, []);

  useEffect(() => {
    const token = localStorage.getItem('token');
  
    fetch('http://127.0.0.1:8000/service/SalonService/bca091a9-1bd3-4f80-97e7-11c8d31b088f', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
      .then(res => {
        if (!res.ok) {
          throw new Error('Not authenticated');
        }
        return res.json();
      })
      .then(data => {
        if (Array.isArray(data)) {
          setServiceCount(data.length);
        } else {
          console.error('Unexpected data format:', data);
        }
      })
      .catch(err => {
        console.error('Failed to load services:', err);
      });
  }, []);  

  return (
    <div class="dashboard-cards">
      <div class="card">
        <div class="icon">✅</div>
        <div class="text">
          <h4>Total Appointments</h4>
          <p>{appointmentCount}</p>
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
          <p>{staffCount}</p>
        </div>
      </div>

      <div class="card">
        <div class="icon">💇‍♀️</div>
        <div class="text">
          <h4>Total Services</h4>
          <p>{serviceCount}</p>
        </div>
      </div>
    </div>
  );
}

export default DashboardCards;
