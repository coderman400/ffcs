import React, { useState } from 'react';
import { Link } from 'react-router-dom'; 

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <nav className="bg-charcoal p-4 shadow-md fixed top-0 z-50 w-full flex flex-col">
      <div className="container mx-auto flex justify-between items-center">
        <div className="text-white text-xl font-bold">
          <Link to="/">SkibidiFFCS</Link>
        </div>
        <div className="hidden md:flex space-x-6 font-bold">
          <Link to="/" className="text-white duration-75 hover:text-saffron">Upload</Link>
          <a className="text-white duration-75 hover:text-saffron" href="https://m.media-amazon.com/images/I/41RSnrYaaaL._AC_UF894,1000_QL80_.jpg" target="_blank" rel="noopener noreferrer">Cat</a>
        </div>
        <div className="md:hidden">
          <button onClick={toggleMenu} className="text-white">
            {/* Icon for hamburger menu */}
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d={isOpen ? "M6 18L18 6M6 6l12 12" : "M4 6h16M4 12h16M4 18h16"}></path>
            </svg>
          </button>
        </div>
      </div>

      {/* Mobile Menu */}
      {isOpen && (
        <div className="md:hidden bg-persian p-4 mt-2 rounded-lg w-3/4 self-center">
          <Link to="/" className="text-white duration-75 hover:text-saffron mb-2 block">Upload</Link>
          <a className="text-white duration-75 hover:text-saffron" href="https://m.media-amazon.com/images/I/41RSnrYaaaL._AC_UF894,1000_QL80_.jpg" target="_blank" rel="noopener noreferrer">Cat</a>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
