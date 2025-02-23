import React, {useState} from 'react'
import { 
  Menu, 
  Upload,
  Export 
} from '../dashboard_page/components/button'
// import "../../styles/global.css"

function Navbar() {
  const [theme, setTheme] = useState("dark");

  const handleToggle = (event) => {
    setTheme(event.target.checked ? "light" : "dark");
  };

  return (
    <div className="navbar bg-black shadow-2xl space-x-2">
        <div className="flex-none">
          <Menu/>
        </div>
      <div className="flex-1 space-x-5 items-center">
        <a className="text-white text-xl font-bold" href='/'>Dashboard</a>
        <a className="text-white text-xl font-bold" href='/manage'>Manage</a>
      </div>
      
      {/* Buttons on the right */}
      <div className="flex items-center space-x-2">
        <input 
          type="checkbox" 
          value="synthwave" 
          className="toggle theme-controller" 
          onChange={handleToggle}
        />
      </div>
    </div>
  )
}

export default Navbar
