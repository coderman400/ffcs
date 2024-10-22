import React from 'react'
import './styles/edit.css'
import { ChevronDownIcon, ChevronUpIcon } from '@heroicons/react/16/solid'
import { useState } from 'react'
const Edit = () => {
  const [expandedRows, setExpandedRows] = useState({});

  const toggleExpansion = (index) => {
    setExpandedRows((prev) => ({
      ...prev,
      [index]: !prev[index]
    }))
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
    <div className='flex items-center mt-20 justify-center'>
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
              <td className='text-center'><input  className='w-20' type="checkbox"></input></td>
            </tr>
          ))
          }
        </tbody>
      </table>
    </div>
  )
}

export default Edit