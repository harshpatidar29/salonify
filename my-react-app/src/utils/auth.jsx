// src/utils/auth.js
import jwt_decode from "jwt-decode";

// Function for validating the token
export function isTokenValid() {
  const token = localStorage.getItem("token");
  if (!token) return false;

  try {
    const decoded = jwt_decode(token);
    const now = Date.now() / 1000;
    return decoded.exp > now;
  } catch (e) {
    return false;
  }
}
