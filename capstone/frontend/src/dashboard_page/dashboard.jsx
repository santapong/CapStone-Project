import React, { useState } from "react";
import './styles/global.css'
import {
  Navbar, 
  Footer
} from "./components/main_pages";
import Label from "./components/stats/Label";
import { 
  Linechart,
  DraggableChart 
} from './components/charts'

// Dashboard Component
const Dashboard = () => (
  <div className="flex h-screen">
    {/* <Sidebar /> */}
    <div className="flex-1 bg-gray-100">
      <Navbar />
      <div className="p-6">
        <Label />
      </div>
      <Footer/>
    </div>
    
  </div>
);

export default Dashboard;