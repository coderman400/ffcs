import React, { useState } from 'react';
import timetableData from '../assets/small-schema.json';
import courseData from '../assets/result.json';


function Result() {
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
      <td className="bg-gray-300 text-black font-bold p-8 border-solid border-gray-100 border text-center">
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
              <td
                className={`bg-${colorSelect} text-white border border-gray-300 font-bold text-center`}
                key={`${day}-${index}`}
              >
                {slotDay1} {slotDay2 ? `/ ${slotDay2}` : ''} <br /> {dispSlot}
              </td>
            );
          }

          // Handling when there's only one slot
          return (
            <td className="bg-cream text-black border border-gray-300 font-bold text-center" key={`${day}-${index}`}>
              {slotDay1} {slotDay2 ? `/ ${slotDay2}` : ''}
            </td>
          );
        }
        return <td key={`${day}-${index}`}>-</td>;
      })}
    </tr>
  );

  return (
    <div>
      <div className="flex justify-center my-4">
        <button
          className={`p-2 m-2 ${timetableIndex === 0?  `bg-gray-400`: `bg-sienna hover:bg-sandy ease-in-out duration-75`} font-bold text-white rounded`}
          disabled={timetableIndex === 0}
          onClick={() => setTimetableIndex(timetableIndex - 1)}
        >
          Previous Timetable
        </button>
        <button
          disabled={timetableIndex === courseData.slots.length - 1}
          className={`p-2 m-2 ${timetableIndex === courseData.slots.length - 1?  `bg-gray-400`: `bg-sienna hover:bg-sandy ease-in-out duration-75`} font-bold  text-white rounded`}
          onClick={() => setTimetableIndex(timetableIndex + 1)}
        >
          Next Timetable
        </button>
      </div>

      <div className="text-center">
        <span className="text-lg font-bold">Viewing Timetable {timetableIndex + 1} of {courseData.slots.length}</span>
      </div>

      {/* Render timetable table */}
      <div className='flex justify-center '>
      <table className="w-11/12  bg-white  m-10 shadow-xl border border-gray-100 rounded-2xl">
        <thead className="p-10 bg-gray-300 text-center">
          <tr>
            <th className="p-10  text-center border border-gray-100 "></th>
            {theoryTimeSlots.map((timeSlot, index) =>
              timeSlot === 'Lunch Break' ? (
                <th key={`lunch-${index}`} className="border border-gray-100 p-4"></th>
              ) : (
                <th key={`theory-${timeSlot}`} className="border border-gray-100 p-4">{timeSlot}</th>
              )
            )}
          </tr>
          <tr>
            <th></th>
            {labTimeSlots.map((timeSlot, index) =>
              timeSlot === 'Lunch Break' ? (
                <th key={`lunch-${index}`} className="border border-gray-100 p-4"></th>
              ) : (
                <th key={`lab-${timeSlot}`} className="border border-gray-100 p-4">{timeSlot}</th>
              )
            )}
          </tr>
        </thead>
        <tbody>{days.map((day) => renderDayRow(day))}</tbody>
      </table>
      </div>
    </div>
  );
}

export default Result;
