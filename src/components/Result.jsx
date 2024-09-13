import { useLocation } from "react-router-dom"
import timetableData from '../assets/small-schema.json'
import '../styles/Result.css'
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
      <td>{day.toUpperCase()}</td>
      {theorySlots.map((slot, index) => {
        if (slot.days && slot.days[day]) {
          let dispSlot;
          let bgColor;
          let txtColor;
          // Check for both slots
          const slotDay1 = slot.days[day][0];
          const slotDay2 = slot.days[day][1];

          if (resultSlots[slotDay1]) {
            dispSlot = resultSlots[slotDay1];
            bgColor= thTakenSlotColor;
            txtColor = thtakenSlotText;
          } else if (resultSlots[slotDay2]) {
            dispSlot = resultSlots[slotDay2];
            bgColor= labTakenSlotColor;
            txtColor = labtakenSlotText;
          }

          console.log(slot.days[day]);

          if (dispSlot) {
            return (
              <td style={{ backgroundColor: bgColor, color: txtColor }} key={`${day}-${index}`}>
                {slotDay1} {slotDay2 ? `/ ${slotDay2}` : ''} <br /> {dispSlot}
              </td>
            );
          }

          // Handling when there's only one slot
          return <td key={`${day}-${index}`}>{slotDay1} {slotDay2 ? `/ ${slotDay2}` : ''}</td>;
        }
        return <td key={`${day}-${index}`}>-</td>;
      })}
    </tr>
    </>

  );

  return (
    <div>
      <h2>Timetable</h2>
      <table>
      <thead>
          <tr>
            <th>Day</th>
            {theoryTimeSlots.map((timeSlot, index) => (
              timeSlot === 'Lunch Break' ? (
                <th key={`lunch-${index}`} className="lunch"></th>
              ) : (
                <th key={`theory-${timeSlot}`}>{timeSlot}</th>
              )
            ))}
          </tr>
          <tr>
            <th></th>
            {labTimeSlots.map((timeSlot, index) => (
              timeSlot === 'Lunch Break' ? (
                <th key={`lunch-${index}`} className="lunch"></th>
              ) : (
                <th key={`lab-${timeSlot}`}>{timeSlot}</th>
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