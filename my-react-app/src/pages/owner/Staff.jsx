import React from "react";
import Staffs from "../../components/Staff";

export default function  Staff() {
  return (
    <>
        <section className="bg-blue-600 text-white py-8 px-6">
          <div className="max-w-6xl mx-auto">
            <h2 className="text-3xl font-semibold">Staff</h2>
          </div>
        </section>
        <Staffs />
        
    </>
  );
}
