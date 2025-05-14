import React from "react";
import Appointments from "../../components/Appointment";

export default function  Appointment() {
  return (
    <>
        <section className="bg-blue-600 text-white py-8 px-6">
          <div className="max-w-6xl mx-auto">
            <h2 className="text-3xl font-semibold">Appointment</h2>
          </div>
        </section>
        <Appointments />
        
    </>
  );
}

