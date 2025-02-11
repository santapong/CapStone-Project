import React, { useEffect, useState } from 'react'

function Label() {
  const [data , setData] = useState([]);
  const API = "http://localhost:8000/dashboard/data"

  useEffect(() => {
    fetch(API, {
      method: "GET",
    })
      .then((Response) => Response.json())
      .then((data) => setData(data.data))
  }, [])

  return (
    <>
    {data.map((stat, index) => (
      <div
        key={index}
        className="bg-white shadow-md rounded-xl p-4 text-center"
      >
        <p className="text-gray-500">{stat.label}</p>
        <h2 className="text-xl font-bold text-purple-700">{stat.value}</h2>
        <div>{stat.unit}</div>
      </div>
    ))}
    </>
  )
}

export default Label