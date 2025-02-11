import React, {useState} from "react";
import { 
    ResponsiveContainer,
    Line,
    LineChart,
    CartesianGrid,
    XAxis,
    YAxis,
    Tooltip,
    Legend
 } from "recharts";
import { Rnd } from "react-rnd";

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
  
export default DraggableChart