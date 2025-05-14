import { Link } from 'react-router-dom';
import './Navbar.css';  // Import the CSS file

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <Link to="/">Salonify</Link>
      </div>
      <div className="navbar-links">
        <Link to="/contact"><i className="fa fa-user-o"></i></Link>
        <Link to="/signout"><i class="fa fa-sign-out" aria-hidden="true"></i></Link>
      </div>
    </nav>
  );
}
