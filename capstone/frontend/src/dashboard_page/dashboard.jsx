import React, { useState } from "react";
import './styles/global.css'
import {
  Navbar, 
  Footer
} from "./components/main_pages";
import Label from "./components/stats/Label";
import { 
  Linechart,
  DraggableChart, 
  Piechart,
  Barchart
} from './components/charts'

// Dashboard Component
const Dashboard = () => (
  <div className="flex h-screen bg-black">
    {/* <Sidebar /> */}
    <div className="flex-1 bg-white">
      <div className="bg-gray-200">
      <Navbar />
      <div className="px-6">
        <Label />
      </div>
      {/* Chart Zone */}
      <div className="grid grid-cols-3 px-6 py-5 space-x-5">
        <div className="bg-white rounded-2xl shadow-2xl p-4">
          <Linechart height={400} width={400}/>
        </div>
        <div className="bg-white rounded-2xl shadow-2xl p-4">
          <Piechart />
        </div>
        <div className="bg-white rounded-2xl shadow-2xl p-4">
          <Barchart />
        </div>
      </div>
      {/* Chart Zone */}
      <div className="grid grid-cols-3 px-6 py-5 space-x-5">
        <div className="bg-white rounded-2xl shadow-2xl p-4">
          <Linechart height={400} width={400}/>
        </div>
        <div className="bg-white rounded-2xl shadow-2xl p-4">
          <Piechart />
        </div>
        <div className="bg-white rounded-2xl shadow-2xl p-4">
          <Barchart />
        </div>
      </div>
      <Footer/>
      </div>
    </div>
  </div>
);

export default Dashboard;