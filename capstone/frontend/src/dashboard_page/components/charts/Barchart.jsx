import React from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Legend,
  ResponsiveContainer,
} from "recharts";

const Barchart = ({ chartName, data = [], barColor = "#006600" }) => {
  // ตรวจสอบว่า `data` มีค่าหรือไม่
  const chartData = data.length ? data : [
    { day: "2025-02-10", user: 120 },
    { day: "2025-02-11", user: 150 },
    { day: "2025-02-12", user: 90 },
  ];

  // จัดอันดับวันที่มีการใช้งานสูงสุด
  const sortedData = [...chartData].sort((a, b) => b.user - a.user);
  const top3 = sortedData.slice(0, 3);

  return (
    <div>
      {chartName && (
        <div className="mb-2 text-center font-bold">{chartName}</div>
      )}
      <ResponsiveContainer width="100%" height={280}>
        <BarChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="datetime" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="usage" fill={barColor} />
        </BarChart>
      </ResponsiveContainer>
      <div className="mt-4">
        {/* <h3 className="text-lg font-bold text-center">
          Top 3 วันที่มีผู้ใช้เยอะที่สุด
        </h3> */}
        {/* <ol className="list-decimal list-inside text-center">
          {top3.map((item, index) => (
            <li key={index}>
              {item.datetime}: {item.us} ครั้ง
            </li>
          ))}
        </ol> */}
      </div>
    </div>
  );
};

export default Barchart;
