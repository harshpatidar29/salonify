import { Link } from 'react-router-dom';
import './Navbar.css';  // Import the CSS file

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <Link to="/">SalonApp</Link>
      </div>
      <div className="navbar-links">
        <Link to="/">Home</Link>
        <Link to="/services">Services</Link>
        <Link to="/appointments">Appointments</Link>
        <Link to="/contact">Contact</Link>
      </div>
    </nav>
  );
}
