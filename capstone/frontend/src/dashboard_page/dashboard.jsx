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
  Barchart,
  Radarchart
} from './components/charts'
import { 
  Chatbot 
} from "./components/button";
import { RadialBar } from "recharts";

// Dashboard Component
const Dashboard = () => (
  <div className="flex h-screen bg-black">
    {/* <Sidebar /> */}
    <div className="flex-1 bg-white">
      <div className="bg-gray-200">
      <Navbar />
      {/* Stats Show */}
      {/* <div className="px-6 space-x-2"> */}
      <div className="grid grid-cols-4 gap-4 my-4 px-6">
          <Label />
      </div>
      {/* </div> */}
      {/* Chart Zone */}
      <div className="grid grid-cols-3 grid-rows-3 px-6 py-5 gap-4 h-full">
        <div className="bg-white rounded-2xl shadow-2xl p-4 items-center justify-center h-[300px]">
          <Radarchart />
        </div>
        <div className="bg-white rounded-2xl shadow-2xl p-4 items-center justify-center h-[300px]">
          <Piechart />
        </div>
        <div className="bg-white rounded-2xl shadow-2xl p-4 items-center justify-center h-[300px]">
          <Barchart />
        </div>
        <div className="col-span-2 row-span-2 bg-white rounded-2xl shadow-2xl p-4 items-center justify-center h-[450px]">
          <Linechart />
        </div>
        <div className="row-span-2 bg-white rounded-2xl shadow-2xl p-4 items-center justify-center h-[450px]">
          <Piechart Radius_size={90}/>
        </div>
      </div>
      {/* Chart Zone */}
      {/* <div className="grid grid-cols-3 px-6 py-5 space-x-5">
        <div className="bg-white rounded-2xl shadow-2xl p-4">
          
        </div>
        <div className="bg-white rounded-2xl shadow-2xl p-4">
          <Piechart />
        </div>
        <div className="bg-white rounded-2xl shadow-2xl p-4">
          <Barchart />
        </div>
      </div> */}
      <Chatbot/>
      <Footer/>
      </div>
    </div>
  </div>
);

export default Dashboard;