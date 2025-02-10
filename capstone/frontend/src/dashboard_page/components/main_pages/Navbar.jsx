import React from 'react'
import "../../styles/global.css"

function Navbar() {
  return (
    <div className="navbar bg-black shadow-2xl space-x-2">
        <div className="flex-none">
          <button className="btn btn-square">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              className="inline-block h-5 w-5 stroke-current">
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
      <div className="flex-1 space-x-5 items-center">
        <a className="text-white text-xl font-bold" href='/dashboard'>Dashboard</a>
        <a className="text-white text-xl font-bold" href='/'>Home</a>
      </div>
      
      {/* Buttons on the right */}
      <div className="flex items-center space-x-4">
        <button className="btn btn-accent">Export</button>
        <button className="btn btn-accent">Upload Docs</button>
        <button className="btn btn-square">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            className="inline-block h-5 w-5 stroke-current">
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z"></path>
          </svg>
        </button>
      </div>
    </div>
  )
}

export default Navbar
