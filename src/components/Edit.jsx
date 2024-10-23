import React from 'react'
import './styles/edit.css'
import { ChevronDownIcon, ChevronUpIcon } from '@heroicons/react/16/solid'
import { useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom';
import  {useLocation} from 'react-router-dom';
const apiAddress = 'http://192.168.204.109:8000/process3';


const Edit = () => {
  const [expandedRows, setExpandedRows] = useState({});
  const [mandatory , setMandatory] = useState({});
  const [credits, setCredits] = useState('');
  const [creditsError, setCreditsError] = useState('');
  const [timing, setTiming] = useState('morning');

  const navigate = useNavigate();
  const location = useLocation();
  const courses = location.state || {}

  //   let courses = [
  //   {
  //     code: "CSI3003",
  //     title: "Introduction to Frontend Development",
  //     slots: ["G1+TG1"]
  //   },
  //   {
  //     code: "CSI3001",
  //     title: "Cloud Computing Methodologies",
  //     slots: ["B1+TB1", "B2+TB2", "A1+TA1+L51+L52"]
  //   }
  // ]

  const toggleExpansion = (index) => {
    setExpandedRows((prev) => ({
      ...prev,
      [index]: !prev[index]
    }))
  }

  const selectMandatory = (index) => {
    setMandatory((prev) => ({
      ...prev,
      [index]: !prev[index]
    }))
  }

  const handleCreditsChange = (event) => {
    setCredits(event.target.value);
  };
  const handleTimingChange = (event) => {
    setTiming(event.target.value);
  };
  
  const handleSubmit = async()=> {
    const creditsValue = parseInt(credits, 10);
    if (creditsValue < 16 || creditsValue > 27 || isNaN(creditsValue)) {
      setCreditsError('Credits value must be between 16 and 27.');
      return;
    }
    setCreditsError('')

    let formData = new FormData()

    formData.append('credits',credits)
    formData.append('timing', timing)

    let result = courses.map((course,index) => ({
      code: course.code,
      title: course.title,
      slots: course.slots,
      mandatory: mandatory[index] || false,
    }))

    formData.append('courses',JSON.stringify(result))
    try{
      const response = await axios.post(`${apiAddress}`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      console.log(response.data)
      // navigate('/result', { state: response.data });
    }catch{
      alert("error!")
    }
  }



  return (
    <div className='flex flex-col items-center mt-10 justify-center'>
      <table className='w-3/4 border shadow-md bg-white'>
        <thead className='bg-gray-800 text-white'> 
          <tr>
            <th>Code</th>
            <th className='md:block sm:hidden'>Course title</th>
            <th className='w-56'>Slots</th>
            <th>Mandatory</th>
          </tr>
        </thead>
        <tbody>
          {courses.map((course,index) => (
            <tr key={index}>
              <td>{course.code}</td>
              <td className='md:block sm:hidden'>{course.title}</td>
              <td>
                <div className='flex flex-row mr-2 justify-between'>
                  <p>{course.slots[0]}</p>
                  {course.slots.length>1 && 
                  <button className='font-bold' onClick={()=>toggleExpansion(index)}>
                    {expandedRows[index]? <ChevronUpIcon className='w-5 h-5' />: <ChevronDownIcon className='w-5 h-5' />}
                  </button>}
                </div>
                {expandedRows[index] && (
                  <div className='max-w-56 break-words'>
                    {course.slots.slice(1).map((slot,i) => (
                      <p key={i}>{slot}</p>
                    ))}
                  </div>
                ) }
              </td>
              <td className='text-center'><input onClick={()=> selectMandatory(index)} className='w-20' type="checkbox"></input></td>
            </tr>
          ))
          }
        </tbody>
      </table>
      <div className='flex md:flex-row sm:flex-col justify-between w-3/4 m-4'>
          <div className="flex-1 mr-4 p-8 md:w-1/2 sm:w-full shadow-md bg-white rounded-lg">
            <h2 className="text-3xl font-bold text-gray-800 mb-6">Timetable Preferences</h2>
            <form className="space-y-4">
              <div>
                <label htmlFor="credits" className="block text-gray-600 font-medium mb-1">
                  Credits:
                </label>
                <input
                  type="number"
                  value={credits}
                  onChange={handleCreditsChange}
                  id="credits"
                  className={`w-1/2 px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 
                  ${creditsError ? 'border-red-500' : 'border-gray-300'}`}
                  placeholder="Enter credits (16 - 27)"
                />
                {creditsError && (
                  <p className="text-red-500 text-sm mt-1">{creditsError}</p>
                )}
              </div>
              <div>
                <label htmlFor="time" className="block text-gray-600 font-medium mb-1">
                  Preferred Timing:
                </label>
                <select
                  id="time"
                  className="w-1/2 px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
                  onChange={handleTimingChange}
                >
                  <option value="morning">Morning</option>
                  <option value="afternoon">Afternoon</option>
                </select>
              </div>
            </form>
          </div>
          
          <div className="flex-1 p-8 md:w-1/2 sm:w-full md:mt-0 sm:mt-4 shadow-md bg-white rounded-lg">
            <h2 className="text-3xl font-bold text-gray-800 mb-6">Advanced Options</h2>
            <form className="space-y-4">
              <div>
                <label htmlFor="input" className="block text-gray-600 font-medium mb-1">
                  Skibidi
                </label>
                <input
                  id="input"
                  className={`w-1/2 px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400`}
                  placeholder='weowoeoo'
                />
              </div>
              <div>
                <label htmlFor="input2" className="block text-gray-600 font-medium mb-1">
                  Rizz
                </label>
                <input
                  id="input2"
                  className={`w-1/2 px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400`}
                  placeholder='weowoeoo'
                />
              </div>
            </form>
          </div>
      </div>
      
      <div className='w-3/4 flex justify-end'>
        <button className='m-4 py-2 px-4  bg-white rounded-md shadow-md hover:bg-persian hover:text-white duration-150' onClick={()=>handleSubmit()}>Submit</button>
      </div>
      
    </div>
  )
}

export default Edit