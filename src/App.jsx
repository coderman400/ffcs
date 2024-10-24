import { useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'
import {Result, Images, Edit, Navbar} from './components'
function App() {
  return(
      <BrowserRouter>
      <Navbar />
        <Routes>
          <Route path="/" element={<Images />}></Route>
          <Route path="/result" element={<Result />}></Route>
          <Route path="/edit" element={<Edit />}></Route>
        </Routes>
      </BrowserRouter>
  )
}

export default App
