import { Outlet } from "react-router-dom";
import { 
  Footer, 
  Navbar 
} from "./components";
import Chatbot  from "./components/Chatbot";

const Layout = () => {
  return (
    <div>
      <Navbar /> {/* Global Navbar */}
      <main>
        <Outlet /> {/* This renders the current page */}
      </main>
      <Chatbot/>
      <Footer/>
    </div>
  );
};

export default Layout;
