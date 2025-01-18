import React from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

const data = [
  { name: "Page A", uv: 400, pv: 2400 },
  { name: "Page B", uv: 300, pv: 4567 },
  { name: "Page C", uv: 200, pv: 1398 },
  { name: "Page D", uv: 278, pv: 9800 },
];

const ExampleBarChart = () => {
  return (
    <BarChart width={500} height={300} data={data}>
      <CartesianGrid stroke="#ccc" />
      <XAxis dataKey="name" />
      <YAxis />
      <Tooltip />
      <Bar dataKey="uv" fill="#8884d8" />
    </BarChart>
  );
};

export default ExampleBarChart;
