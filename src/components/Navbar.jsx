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
          <a className="text-white duration-75 hover:text-saffron" href="https://github.com/coderman400/ffcs" target="_blank" rel="noopener noreferrer"><svg className="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 0C5.373 0 0 5.373 0 12c0 5.303 3.438 9.8 8.205 11.387.6.113.82-.26.82-.577 0-.285-.01-1.04-.016-2.04-3.338.726-4.042-1.61-4.042-1.61-.546-1.385-1.333-1.755-1.333-1.755-1.09-.745.083-.73.083-.73 1.205.085 1.84 1.238 1.84 1.238 1.07 1.834 2.807 1.304 3.492.996.108-.774.418-1.305.76-1.605-2.665-.304-5.466-1.335-5.466-5.93 0-1.31.468-2.38 1.236-3.22-.124-.303-.536-1.527.116-3.18 0 0 1.01-.323 3.31 1.23a11.55 11.55 0 013.016-.405c1.02.004 2.045.137 3.016.405 2.3-1.553 3.31-1.23 3.31-1.23.652 1.653.24 2.877.118 3.18.77.84 1.236 1.91 1.236 3.22 0 4.61-2.804 5.625-5.474 5.92.43.37.81 1.102.81 2.222 0 1.605-.014 2.896-.014 3.286 0 .32.218.694.824.576C20.565 21.796 24 17.298 24 12 24 5.373 18.627 0 12 0z"/>
            </svg></a>
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
          <a className="text-white duration-75 hover:text-saffron" href="https://github.com/coderman400/ffcs" target="_blank" rel="noopener noreferrer"><svg className="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 0C5.373 0 0 5.373 0 12c0 5.303 3.438 9.8 8.205 11.387.6.113.82-.26.82-.577 0-.285-.01-1.04-.016-2.04-3.338.726-4.042-1.61-4.042-1.61-.546-1.385-1.333-1.755-1.333-1.755-1.09-.745.083-.73.083-.73 1.205.085 1.84 1.238 1.84 1.238 1.07 1.834 2.807 1.304 3.492.996.108-.774.418-1.305.76-1.605-2.665-.304-5.466-1.335-5.466-5.93 0-1.31.468-2.38 1.236-3.22-.124-.303-.536-1.527.116-3.18 0 0 1.01-.323 3.31 1.23a11.55 11.55 0 013.016-.405c1.02.004 2.045.137 3.016.405 2.3-1.553 3.31-1.23 3.31-1.23.652 1.653.24 2.877.118 3.18.77.84 1.236 1.91 1.236 3.22 0 4.61-2.804 5.625-5.474 5.92.43.37.81 1.102.81 2.222 0 1.605-.014 2.896-.014 3.286 0 .32.218.694.824.576C20.565 21.796 24 17.298 24 12 24 5.373 18.627 0 12 0z"/>
            </svg></a>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
