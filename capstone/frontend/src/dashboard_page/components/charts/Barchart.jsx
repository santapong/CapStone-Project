import React from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid, Legend } from "recharts";

const data = [
  { name: "A", value: 400 },
  { name: "B", value: 300 },
  { name: "C", value: 300 },
  { name: "D", value: 200 },
];

const Barchart = ({width, height, data}) => {
  return (
    <div>
      <h2>Bar Chart</h2>
      <BarChart width={width} height={height} data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="value" fill="#8884d8" />
      </BarChart>
    </div>
  );
};

export default Barchart;
