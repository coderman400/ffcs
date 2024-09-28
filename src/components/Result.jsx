import { useLocation } from "react-router-dom"
import timetableData from '../assets/small-schema.json'
// import '../styles/Result.css'
import courseData from '../assets/result.json'

const thTakenSlotColor = '#8b635c'
const thtakenSlotText = 'white'

const labTakenSlotColor = '#DCBF85'
const labtakenSlotText = 'white'

function Result(){
   const days = ['mon', 'tue', 'wed', 'thu', 'fri'];

  const resultSlots = courseData.slots

  const allSlots = [
    ...timetableData.theory.filter(slot => slot.days), 
    ...timetableData.lab.filter(slot => slot.days)
  ];

  const theorySlots = [...timetableData.theory]
  const labSlots = [...timetableData.lab]

  const theoryTimeSlots = timetableData.theory.map(slot => slot.lunch ? 'Lunch Break' : `${slot.start} - ${slot.end}`);
  const labTimeSlots = timetableData.lab.map(slot => slot.lunch ? 'Lunch Break' : `${slot.start} - ${slot.end}`);
  let dispSlot;

  const renderDayRow = (day) => (
    <>
    <tr key={day}>
      <td className="bg-gray-300 text-black font-bold p-8 border-solid border-gray-100 border text-center">{day.toUpperCase()}</td>
      {theorySlots.map((slot, index) => {
        if (slot.days && slot.days[day]) {
          let dispSlot;
          let bgColor;
          let txtColor;
          // Check for both slots
          const slotDay1 = slot.days[day][0];
          const slotDay2 = slot.days[day][1];

          let colorSelect = 'charcoal'

          if (resultSlots[slotDay1]) {
            dispSlot = resultSlots[slotDay1];
            colorSelect='charcoal'
            txtColor = thtakenSlotText;
          } else if (resultSlots[slotDay2]) {
            dispSlot = resultSlots[slotDay2];
            colorSelect='persian'
            txtColor = labtakenSlotText;
          }
          
          console.log(slot.days[day]);

          if (dispSlot) {
            return (
              <td className={`bg-${colorSelect} text-white border border-gray-300 font-bold text-center`} key={`${day}-${index}`}>
                {slotDay1} {slotDay2 ? `/ ${slotDay2}` : ''} <br /> {dispSlot}
              </td>
            );
          }

          // Handling when there's only one slot
          return <td className='bg-cream text-black border border-gray-300 font-bold text-center'key={`${day}-${index}`}>{slotDay1} {slotDay2 ? `/ ${slotDay2}` : ''}</td>;
        }
        return <td key={`${day}-${index}`}>-</td>;
      })}
    </tr>
    </>

  );

  return (
    <div>
      <table className="w-11/12  bg-white  m-20 shadow-xl border border-gray-100 rounded-2xl">
      <thead className="p-10 bg-gray-300 text-center">
          <tr>
            <th className="p-10  text-center border border-gray-100 "></th>
            {theoryTimeSlots.map((timeSlot, index) => (
              timeSlot === 'Lunch Break' ? (
                <th key={`lunch-${index}`} className="border   border-gray-100 p-4"></th>
              ) : (
                <th key={`theory-${timeSlot}`} className="border   border-gray-100 p-4">{timeSlot}</th>
              )
            ))}
          </tr>
          <tr>
            <th></th>
            {labTimeSlots.map((timeSlot, index) => (
              timeSlot === 'Lunch Break' ? (
                <th key={`lunch-${index}`} className="border   border-gray-100 p-4" ></th>
              ) : (
                <th key={`lab-${timeSlot}`} className="border border-gray-100 p-4  ">{timeSlot}</th>
              )
            ))}
          </tr>
        </thead>
        <tbody>
          {days.map((day) => renderDayRow(day))}
        </tbody>
      </table>
    </div>
  );
}
export default Result