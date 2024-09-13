import { useLocation } from "react-router-dom"
import timetableData from '../assets/schema.json'
import '../styles/Result.css'
import courseData from '../assets/result.json'

const takenSlotColor = '#8b635c'
const takenSlotText = 'white'
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


  const renderDayRow = (day) => (
    <>
    <tr key={day}>
      <td>{day.toUpperCase()}</td>
      {theorySlots.map((slot, index) => {
        if(slot.days && slot.days[day] && resultSlots[slot.days[day]]){
          return(
            <td style={{backgroundColor:takenSlotColor, color:takenSlotText} }key={`${day}-${index}`}>{slot.days[day]} <br></br> {resultSlots[slot.days[day]]} </td>
          )
        }
        else if (slot.days && slot.days[day]) {
          return (
          <td key={`${day}-${index}`}>{slot.days[day]}</td>
        );
        }
        return <td key={`${day}-${index}`}>-</td>;
      })}
    </tr>
    <tr key={day}>
      <td>{day.toUpperCase()}</td>
      {labSlots.map((slot, index) => {

        if (slot.days && slot.days[day]) {
          return <td key={`${day}-${index}`}>{slot.days[day]}</td>;
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