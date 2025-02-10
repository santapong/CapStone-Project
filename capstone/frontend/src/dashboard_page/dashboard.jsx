import React, { useState } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from "recharts";
import { Rnd } from "react-rnd";
import './styles/global.css'

// Sidebar Component
const Sidebar = () => (
  <div className="sidebar_root">
    <h1 className="sidebar_header">KMITL Dashboard</h1>
    <nav className="space-y-4">
      <a href="/" className="sidebar_menu ">Home</a>
      <a href="#" className="sidebar_menu ">Profile</a>
      <a href="#" className="sidebar_menu ">Analytics</a>
      <a href="#" className="sidebar_menu ">Settings</a>
      <a href="#" className="sidebar_menu ">Messages</a>
    </nav>
  </div>
);

// Header Component
const Header = () => (
  <div className="bg-white shadow-md h-16 flex items-center justify-between px-6">
    <input
      type="text"
      placeholder="Search..."
      className="border rounded-lg px-4 py-2 w-1/3"
    />
    <div className="flex items-center space-x-4">
      <span className="font-medium">Mike Lock</span>
      <img
        src="https://via.placeholder.com/40"
        alt="Profile"
        className="w-10 h-10 rounded-full"
      />
    </div>
  </div>
);

// Stats Component
const Stats = () => (
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
);

// Chart Component using Recharts
const Chart = () => {
  const data = [
    { name: "Mon", uv: 400, pv: 2400, amt: 2400 },
    { name: "Tue", uv: 300, pv: 1398, amt: 2210 },
    { name: "Wed", uv: 200, pv: 9800, amt: 2290 },
    { name: "Thu", uv: 278, pv: 3908, amt: 2000 },
    { name: "Fri", uv: 189, pv: 4800, amt: 2181 },
    { name: "Sat", uv: 239, pv: 3800, amt: 2500 },
    { name: "Sun", uv: 349, pv: 4300, amt: 2100 },
  ];

  return (
    <div className="bg-white shadow-md rounded-xl w-full h-full p-6">
      <ResponsiveContainer width="100%" height="100%">
        <LineChart
          data={data}
          margin={{ top: 5, right: 20, left: 10, bottom: 5 }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="uv" stroke="#8884d8" />
          <Line type="monotone" dataKey="pv" stroke="#82ca9d" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

// Draggable Chart Container
const DraggableChart = () => {
  const [position, setPosition] = useState({ x: 0, y: 0 });

  return (
    <Rnd
      bounds="parent"
      size={{ width: 400, height: 300 }}
      position={position}
      onDragStop={(e, d) => setPosition({ x: d.x, y: d.y })}
      className="shadow-md bg-white rounded-xl"
    >
      <Chart />
    </Rnd>
  );
};

// Dashboard Component
const Dashboard = () => (
  <div className="flex h-screen">
    <Sidebar />
    <div className="flex-1 bg-gray-100">
      <Header />
      <div className="p-6">
        <Stats />
        <div className="relative w-full h-[500px] bg-gray-200 rounded-lg">
          <DraggableChart />
          <DraggableChart/>
        </div>
      </div>
    </div>
  </div>
);

export default Dashboard;
