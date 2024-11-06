import React, { useState } from 'react';
import timetableData from '../assets/small-schema.json';
// import courseData from '../assets/result.json';
import { ArrowLeftIcon} from '@heroicons/react/16/solid';
import { useNavigate, useLocation } from 'react-router-dom';
function Result() {
  const location = useLocation();
  const courseData = location.state || {}
  if (!courseData.slots) {
    alert('NO TIMETABLES MAN');
  }
  const navigate = useNavigate();
  

  const days = ['mon', 'tue', 'wed', 'thu', 'fri'];
  const [timetableIndex, setTimetableIndex] = useState(0);

  const resultSlots = courseData.slots[timetableIndex];
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
  const handleBackClick = () => {
    if (window.confirm("This will take you back to the edit page. Are you sure?")) {
      navigate(-1);
    }
  };

  const renderDayRow = (day) => (
    <tr key={day}>
      <td className="bg-gray-300 text-black font-bold p-2 sm:p-4 border-solid border-gray-100 border text-center">
        {day.toUpperCase()}
      </td>
      {theorySlots.map((slot, index) => {
        if (slot.days && slot.days[day]) {
          let dispSlot;
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
                style={{ backgroundColor: colorSelect === 'persian' ? '#2A9D8F' : '#264653' }}
                className="text-white border border-gray-200 font-bold text-center p-2 sm:p-4"
                key={`${day}-${index}`}
              >
                {slotDay1} {slotDay2 ? `/ ${slotDay2}` : ''} <br /> {dispSlot}
              </td>
            );
          }

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
      <div className="flex justify-between items-center mt-20 w-10/12 mx-auto">
        <button
          className="p-2 m-2 bg-sienna hover:bg-sandy ease-in-out duration-75 font-bold text-white rounded"
          onClick={() => handleBackClick()} 
        >
          <ArrowLeftIcon height={30} width={60} />
        </button>

        <div className="flex justify-center">
          <button
            className={`p-2 m-2 ${timetableIndex === 0 ? 'bg-gray-400' : 'bg-sienna hover:bg-sandy ease-in-out duration-75'} font-bold text-white rounded`}
            disabled={timetableIndex === 0}
            onClick={() => setTimetableIndex(timetableIndex - 1)}
          >
            Previous Timetable
          </button>
          <button
            disabled={timetableIndex === courseData.slots.length - 1}
            className={`p-2 m-2 ${timetableIndex === courseData.slots.length - 1 ? 'bg-gray-400' : 'bg-sienna hover:bg-sandy ease-in-out duration-75'} font-bold text-white rounded`}
            onClick={() => setTimetableIndex(timetableIndex + 1)}
          >
            Next Timetable
          </button>
        </div>
      </div>

      <div className="text-center">
        <span className="text-lg font-bold">Viewing Timetable {timetableIndex + 1} of {courseData.slots.length}</span>
      </div>
      <div className="flex justify-center items-center gap-4 mt-6">
        <div className="flex items-center gap-2">
          <div style={{ backgroundColor: '#2A9D8F' }} className="w-4 h-4 rounded"></div>
          <span>Theory</span>
        </div>
        <div className="flex items-center gap-2">
          <div style={{ backgroundColor: '#264653' }} className="w-4 h-4 rounded"></div>
          <span>Lab</span>
        </div>
      </div>
    
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
        <div className='flex justify-center mb-4 w-10/12'>
          <p className={`text-xl font-bold ${resultSlots.credits==27 ? 'bg-saffron text-black': 'bg-persian text-white' } p-2 rounded-md`}>{resultSlots.credits} CREDITS</p>
        </div>
        <table className='w-8/12 bg-white rounded-md mb-8'>
          <thead className='text-xl border-b text-white bg-charcoal'>
            <tr>
              <th>Code</th>
              <th>Title</th>
              <th>Slot</th>
            </tr>
          </thead>
          <tbody className='text-center'>
            {resultSlots.info.map((data, index) => (
              <tr className='border-b-gray-00 border-2' key={index}>
                <td>{data.code}</td>
                <td>{data.title}</td>
                <td>{data.slot[0]}{data.slot[1] ? '+' + data.slot[1] : ''}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Result;
