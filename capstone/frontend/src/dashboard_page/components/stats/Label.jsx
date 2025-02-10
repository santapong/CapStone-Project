import React, { useState } from 'react'

function Label() {
  const [data , setData] = useState([]);

  return (
    <div className="grid grid-cols-4 gap-6 my-6">
    {[
      { label: "Usage", value: "24", unit: 'time' },
      { label: "Avg Sessions", value: "00:18", unit: 'time' },
      { label: "Most Ask", value: "Process", unit: 'Ask' },
      { label: "Avg Watch Time", value: "45.42", unit: 'time' },
    ].map((stat, index) => (
      <div
        key={index}
        className="bg-white shadow-md rounded-xl p-4 text-center"
      >
        <p className="text-gray-500">{stat.label}</p>
        <h2 className="text-xl font-bold text-purple-700">{stat.value}</h2>
        <div>{stat.unit}</div>
      </div>
    ))}
    
  </div>
  )
}

export default Label