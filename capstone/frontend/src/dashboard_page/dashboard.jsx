import React, {useEffect, useState} from 'react'
import {
  Navbar,
  Footer
} from "./components/main_pages"

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

  // useEffect(()=>{
  //   // Request API From Backend
  //   fetch(API_URL)
  //     .then(response => response.json())
  //     .then(data => setPieData(data))
  //     .catch(error => console.error('Error request from Backend', error))
  // },[])
  
  return (
  <div className='root_page' >
      <Navbar/>
      <div className='menu_container'></div>
      <div className='chart_container'>
        <div className='chart_box'>
          <Barchart width={width} height={height}/>
        </div>
        <div className='chart_box'>
          <Piechart width={width} height={height}/>
        </div>
        <div className='chart_box'>
          <Treemapchart width={width} height={height}/>
        </div>
        <div className='chart_box'>
          <Linechart width={width} height={height}/>
        </div>
        <div className='chart_box'>
          <Radarchart width={width} height={height}/>
        </div>  
      </div>

      <Footer/>
    </div>
  )
}

export default Dashboard