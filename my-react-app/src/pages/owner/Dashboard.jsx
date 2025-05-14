import React from "react";

import DashboardCards from "../../components/DashboardCards";

export default function  OwnerDashboard() {
  return (
    <>
        <section className="bg-blue-600 text-white py-8 px-6">
          <div className="max-w-6xl mx-auto">
            <h2 className="text-3xl font-semibold">Dashboard</h2>
          </div>
        </section>
        <DashboardCards />
        
    </>
  );
}

