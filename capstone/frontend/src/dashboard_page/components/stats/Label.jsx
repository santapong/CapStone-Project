import React from 'react'

function Label() {
  return (
    <div className="grid grid-cols-4 gap-6 my-6">
    {[
      { label: "Sessions", value: "24k" },
      { label: "Avg Sessions", value: "00:18" },
      { label: "Bounce Rate", value: "$2400" },
      { label: "Avg Watch Time", value: "45.42" },
    ].map((stat, index) => (
      <div
        key={index}
        className="bg-white shadow-md rounded-xl p-4 text-center"
      >
        <p className="text-gray-500">{stat.label}</p>
        <h2 className="text-xl font-bold text-purple-700">{stat.value}</h2>
      </div>
    ))}
  </div>
  )
}

export default Label