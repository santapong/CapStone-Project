import React from "react";
import ReactDOM from "react-dom/client";
import App from "./show_page/page";
import Dashboard from "./dashboard_page/dashboard";
import "./index.css";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom"
import Manage from "./manage_page/manage";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App/>,
  },
  {
    path: "/error",
    element: <Manage/>
  },
  {
    path:"/dashboard",
    element: <Dashboard/>
  }
])

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>
);
