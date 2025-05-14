// src/App.jsx
import { Routes, Route } from 'react-router-dom';
import OwnerLayout from './layout/OwnerLayout';
import Dashboard from './pages/owner/Dashboard';
import Login from './pages/Login';
import Logout from './components/Logout';
import Appointment from './pages/owner/Appointment';
import Service from './pages/owner/Service';


function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/logout" element={<Logout />} />

      <Route path="/owner" element={<OwnerLayout />}>
        <Route path="dashboard" element={<Dashboard />} />
        <Route path="appointment" element={<Appointment />} />
        <Route path="service" element={<Service />} />

      </Route>
    </Routes>
  );
}

export default App;
