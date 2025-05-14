import React from "react";
import Services from "../../components/Service";

export default function  Service() {
  return (
    <>
        <section className="bg-blue-600 text-white py-8 px-6">
          <div className="max-w-6xl mx-auto">
            <h2 className="text-3xl font-semibold">Service</h2>
          </div>
        </section>
        <Services />
        
    </>
  );
}

