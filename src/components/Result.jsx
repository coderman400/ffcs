import React, { useState } from 'react';
import timetableData from '../assets/small-schema.json';
// import courseData from '../assets/result.json';
import { useLocation } from 'react-router-dom';

function Result() {
  const location = useLocation();
  const courseData = location.state || {}
  if (!courseData.slots) {
    alert('NO TIMETABLES MAN');
  }
  const days = ['mon', 'tue', 'wed', 'thu', 'fri'];
  const [timetableIndex, setTimetableIndex] = useState(0);  // State for current timetable index

  const resultSlots = courseData.slots[timetableIndex];  // Get current timetable based on index

  const allSlots = [
    ...timetableData.theory.filter((slot) => slot.days),
    ...timetableData.lab.filter((slot) => slot.days),
  ];

  const theorySlots = [...timetableData.theory];
  const labSlots = [...timetableData.lab];

  const theoryTimeSlots = timetableData.theory.map((slot) =>
    slot.lunch ? 'Lunch Break' : `${slot.start} - ${slot.end}`
  );
  const labTimeSlots = timetableData.lab.map((slot) =>
    slot.lunch ? 'Lunch Break' : `${slot.start} - ${slot.end}`
  );

  const renderDayRow = (day) => (
    <tr key={day}>
      <td className="bg-gray-300 text-black font-bold p-2 sm:p-4 border-solid border-gray-100 border text-center">
        {day.toUpperCase()}
      </td>
      {theorySlots.map((slot, index) => {
        if (slot.days && slot.days[day]) {
          let dispSlot;
          // Check for both slots
          const slotDay1 = slot.days[day][0];
          const slotDay2 = slot.days[day][1];

          let colorSelect = 'persian';

          if (resultSlots[slotDay1]) {
            dispSlot = resultSlots[slotDay1];
          } else if (resultSlots[slotDay2]) {
            colorSelect = 'charcoal';
            dispSlot = resultSlots[slotDay2];
          }

          if (slotDay1.slice(0, 1) === 'L') {
            colorSelect = 'charcoal';
          }

          if (dispSlot) {
            return (
              // Update the className to dynamically generate the class using template literals
              <td
                style={{ backgroundColor: colorSelect === 'persian' ? '#2A9D8F' : '#264653' }}
                className="text-white border border-gray-200 font-bold text-center p-2 sm:p-4"
                key={`${day}-${index}`}
              >
                {slotDay1} {slotDay2 ? `/ ${slotDay2}` : ''} <br /> {dispSlot}
              </td>
            );
          }

          // Handling when there's only one slot
          return (
            <td className="bg-cream text-black border border-gray-200 font-bold text-center p-2 sm:p-4" key={`${day}-${index}`}>
              {slotDay1} {slotDay2 ? `/ ${slotDay2}` : ''}
            </td>
          );
        }
        return <td key={`${day}-${index}`} className="p-2 sm:p-4">-</td>;
      })}
    </tr>
  );

  return (
    <div>
      <div className="flex justify-center mt-20 mb-4">
        <button
          className={`p-2 m-2 ${timetableIndex === 0 ? `bg-gray-400` : `bg-sienna hover:bg-sandy ease-in-out duration-75`} font-bold text-white rounded`}
          disabled={timetableIndex === 0}
          onClick={() => setTimetableIndex(timetableIndex - 1)}
        >
          Previous Timetable
        </button>
        <button
          disabled={timetableIndex === courseData.slots.length - 1}
          className={`p-2 m-2 ${timetableIndex === courseData.slots.length - 1 ? `bg-gray-400` : `bg-sienna hover:bg-sandy ease-in-out duration-75`} font-bold text-white rounded`}
          onClick={() => setTimetableIndex(timetableIndex + 1)}
        >
          Next Timetable
        </button>
      </div>

      <div className="text-center">
        <span className="text-lg font-bold">Viewing Timetable {timetableIndex + 1} of {courseData.slots.length}</span>
      </div>

      {/* Render timetable table */}
      <div className="flex flex-col items-center justify-center overflow-x-auto">
        <table className="w-1/12 sm:w-10/12 bg-white m-10 shadow-xl b rounded-2xl">
          <thead className="bg-gray-300 text-center">
            <tr>
              <th className="text-center border border-gray-100 p-2 sm:p-4"></th>
              {theoryTimeSlots.map((timeSlot, index) =>
                timeSlot === 'Lunch Break' ? (
                  <th key={`lunch-${index}`} className="border border-gray-100 p-2 sm:p-4"></th>
                ) : (
                  <th key={`theory-${timeSlot}`} className="border border-gray-100 p-2 sm:p-4">{timeSlot}</th>
                )
              )}
            </tr>
            <tr>
              <th></th>
              {labTimeSlots.map((timeSlot, index) =>
                timeSlot === 'Lunch Break' ? (
                  <th key={`lunch-${index}`} className="border border-gray-100 p-2 sm:p-4"></th>
                ) : (
                  <th key={`lab-${timeSlot}`} className="border border-gray-100 p-2 sm:p-4">{timeSlot}</th>
                )
              )}
            </tr>
          </thead>
          <tbody>{days.map((day) => renderDayRow(day))}</tbody>
        </table>
        {/* <table className='w-8/12 bg-white rounded-md mb-8'>
          <thead className='text-xl border-b text-white bg-charcoal'>
            <tr className=''>
              <th>Code</th>
              <th>Title</th>
              <th>Slot</th>
              <th>Professor</th>
            </tr>
          </thead>
          <tbody className='text-center'>
            {resultSlots.info.map((data,index)=>(
              <tr className='border-b-gray-00 border-2' key={index}>
              <td>{data.code}</td>
              <td>{data.title}</td>
              <td>{data.slot}</td>
              <td>{data.professor}</td>
              </tr>
            ))}
            
          </tbody>
        </table> */}
      </div>
    </div>
  );
}

export default Result;
