import React from "react";
import ReactDOM from "react-dom/client";
import App from "./show_page/page";
import Dashboard from "./dashboard_page/dashboard";
import Layout from "./Layout";
import "./index.css";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom"
import Manage from "./manage_page/manage";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />, // Wrap pages with Layout
    children: [
      { index: true, element: <Dashboard /> }, // Default homepage
      { path: "Manage", element: <Manage /> }, // Manage Page
    ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>
);
