import React from 'react'
import Navbar from "./components/main_pages/Navbar"
import Barchart from './components/charts/Barchart'
import Piechart from './components/charts/Piechart'
import Linechart from './components/charts/Linechart'
import Radarchart from './components/charts/Radarchart'
import Example from './components/charts/Treemap'
import "./styles/global.css"

function Dashboard() {

  const width = 200 
  const height = 200 

  return (
  <div>
      <Navbar/>
      <div className='flex flex-wrap space-x-4 gap-10 mt-4'>
        <div className='w-full md:w-1/2 lg:w-1/4'>
          <Barchart width={width} height={height}/>
        </div>
        <div className='w-full md:w-1/2 lg:w-1/4'>
          <Piechart width={width} height={height}/>
        </div>
        <div className='w-full md:w-1/2 lg:w-1/4'>
          <Example width={width} height={height}/>
        </div>
        <div className='w-full md:w-1/2 lg:w-1/4'>
          <Linechart width={width} height={height}/>
        </div>
        <div className='w-full md:w-1/2 lg:w-1/4'>
          <Radarchart width={width} height={height}/>
        </div>
      </div>
    </div>
  )
}

export default Dashboard