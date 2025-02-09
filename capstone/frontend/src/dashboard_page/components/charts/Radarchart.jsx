import React from 'react';
import { RadarChart, Radar, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Tooltip, Legend } from 'recharts';

// Sample data for the Radar chart
const data = [
  {
    subject: 'Math',
    A: 120,
    fullMark: 150,
  },
  {
    subject: 'Chinese',
    A: 98,
    fullMark: 150,
  },
  {
    subject: 'English',
    A: 86,
    fullMark: 150,
  },
  {
    subject: 'Geography',
    A: 99,
    fullMark: 150,
  },
  {
    subject: 'Physics',
    A: 85,
    fullMark: 175,
  },
];

const Radarchart = () => {
  return (
    <div>
      <h2>Radar Chart Example</h2>
      <RadarChart outerRadius={90} width={400} height={400} data={data}>
        <PolarGrid />
        <PolarAngleAxis dataKey="subject" />
        <PolarRadiusAxis angle={30} domain={[0, 150]} />
        <Radar name="Student A" dataKey="A" stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
        <Tooltip />
        <Legend />
      </RadarChart>
    </div>
  );
};

export default Radarchart;
