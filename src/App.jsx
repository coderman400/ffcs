import { useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'
import Form from './components/Form.jsx'
import Courses from './components/Courses.jsx'
import Result from './components/Result.jsx'
function App() {
  return(
    <div className='container'>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Form />}></Route>
          <Route path="/result" element={<Result />}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
