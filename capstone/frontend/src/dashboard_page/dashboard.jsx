import React, {useEffect, useState} from 'react'
import Navbar from "./components/main_pages/Navbar"

import { 
  Barchart,
  Piechart,
  Linechart,
  Radarchart,
  Treemapchart,
 } from './components/charts'

import { DBQuery } from './components/database'

import "./styles/global.css"

function Dashboard() {
  const [piedata, setPieData] = useState(null);

  // Call DBQuery class
  const query = new DBQuery()
  const width = 200
  const height = 200
  const API_URL = import.meta.env.VITE_API_URL

  useEffect(()=>{
    // Request API From Backend
    fetch(API_URL)
      .then(response => response.json())
      .then(data => setPieData(data))
      .catch(error => console.error('Error request from Backend', error))
  },[])
  return (
  <div>
      <Navbar/>
      <div className='flex flex-wrap space-x-1 gap-2 mt-4'>
        <div className='w-full md:w-1/2 lg:w-1/4'>
          <Barchart width={width} height={height}/>
        </div>
        <div className='w-full md:w-1/2 lg:w-1/4'>
          <Piechart width={width} height={height}/>
        </div>
        <div className='w-full md:w-1/2 lg:w-1/4'>
          <Treemapchart width={width} height={height}/>
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