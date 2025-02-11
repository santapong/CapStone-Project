import React, { useState } from "react";
import Label from "./components/stats/Label";
import {
  Navbar, 
  Footer
} from "./components/main_pages";
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
import './styles/global.css'

// Dashboard Component
const Dashboard = () => (
  
  <div className="flex-auto h-screen bg-black">
    {/* <Sidebar /> */}
    <div className="flex-1 bg-white">
      <Navbar />
      <div className="bg-gray-200">
      {/* Stats Show */}
      {/* <div className="px-6 space-x-2"> */}
      <div className="grid grid-cols-4 gap-4 my-4 px-6">
          <Label />
      </div>
      {/* </div> */}
      {/* Chart Zone */}
      <div className="grid grid-cols-3 grid-rows-3 px-6 py-5 gap-4">
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
      <Chatbot/>
      <Footer/>
      </div>
    </div>
  </div>
);

export default Dashboard;