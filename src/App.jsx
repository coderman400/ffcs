import { useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'
import {Result, Images} from './components'
function App() {
  return(
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Images />}></Route>
          <Route path="/result" element={<Result />}></Route>
        </Routes>
      </BrowserRouter>
  )
}

export default App
