import React from 'react'
import './styles/edit.css'
import { ChevronDownIcon, ChevronUpIcon } from '@heroicons/react/16/solid'
import { useState } from 'react'
import axios from 'axios'
const Edit = () => {
  const [expandedRows, setExpandedRows] = useState({});
  const [mandatory , setMandatory] = useState({});

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
  
  const handleSubmit = async()=> {
    let result = courses.map((course,index) => ({
      code: course.code,
      name: course.name,
      slots: course.slots,
      mandatory: mandatory[index] || false,
    }))
    
    // try{
    //   const response = await axios.post('API URL', result)
    //   alert("data submitted!")
    // }catch{
    //   alert("error!")
    // }
  }

  let courses = [
    {
      code: "CSI3003",
      name: "Introduction to Frontend Development",
      slots: ["G1+TG1"]
    },
    {
      code: "CSI3001",
      name: "Cloud Computing Methodologies",
      slots: ["B1+TB1", "B2+TB2", "A1+TA1+L51+L52"]
    }
  ]

  return (
    <div className='flex flex-col items-center mt-20 justify-center'>
      <table className='w-3/4 border shadow-md bg-white'>
        <thead className='bg-gray-800 text-white'> 
          <tr>
            <th>Course Code</th>
            <th>Course Name</th>
            <th className='w-56'>Slots</th>
            <th>Mandatory</th>
          </tr>
        </thead>
        <tbody>
          {courses.map((course,index) => (
            <tr key={index}>
              <td>{course.code}</td>
              <td>{course.name}</td>
              <td>
                <div className='flex flex-row mr-2 justify-between'>
                  <p>{course.slots[0]}</p>
                  {course.slots.length>1 && 
                  <button className='font-bold' onClick={()=>toggleExpansion(index)}>
                    {expandedRows[index]? <ChevronUpIcon className='w-5 h-5' />: <ChevronDownIcon className='w-5 h-5' />}
                  </button>}
                </div>
                {expandedRows[index] && (
                  <div>
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
      <div className='w-3/4 flex justify-end'>
        <button className='m-4 py-2 px-4  bg-white rounded-md shadow-md hover:bg-persian hover:text-white duration-150' onClick={()=>handleSubmit()}>Submit</button>
      </div>
      
    </div>
  )
}

export default Edit