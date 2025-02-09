import React from "react";
import ReactDOM from "react-dom/client";
import App from "./show_page/page";
import Error from "./error_page/error";
import "./index.css";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom"

const router = createBrowserRouter([
  {
    path: "/",
    element: <App/>,
  },
  {
    path: "/error",
    element: <Error/>
  }
]
)

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>
);
