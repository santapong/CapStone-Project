import React from 'react'
import Navbar from "./components/main_pages/Navbar"
import Barchart from './components/charts/Barchart'
import Piechart from './components/charts/Piechart'
import Linechart from './components/charts/Linechart'
import Radarchart from './components/charts/Radarchart'
import Example from './components/charts/Treemap'
import "./styles/global.css"

function Dashboard() {
  return (
    <div>
      <Navbar/>
      <Barchart/>
      <Piechart/>
      <Example/>
      <Linechart/>
      <Radarchart/>
    </div>
  )
}

export default Dashboard