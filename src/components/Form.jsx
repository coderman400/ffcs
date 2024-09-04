import '../styles/Form.css';
import { useState } from 'react';
import Courses from './Courses.jsx';

function Form() {
  const [slotsArray, setSlotsArray] = useState([]);
  const [courseArray, setCourseArray] = useState([]);

  const handleAddSlot = (event) => {
    event.preventDefault();
    const slotsInput = document.getElementById('slots');
    const profInput = document.getElementById('prof');
    const newSlot = {
      prof: profInput.value.trim(),
      slots: slotsInput.value.trim(),
      id: crypto.randomUUID()
    };

    if (newSlot.prof && newSlot.slots) {
      setSlotsArray([...slotsArray, newSlot]);
      slotsInput.value = ''; 
      profInput.value = '';
    }
  };

  const handleAddCourse = (event) => {
    event.preventDefault();
    const titleInput = document.getElementById('title');
    const codeInput = document.getElementById('code');

    const newCourse = {
      title: titleInput.value.trim(),
      code: codeInput.value.trim(),
      slots: slotsArray
    }

    if (newCourse.code && slotsArray.length > 0) {
      setCourseArray([...courseArray, newCourse]);
      titleInput.value = '';
      codeInput.value = '';
      setSlotsArray([]); 
    }
  };

  return (
    <>
      <div className="form-wrapper">
        <form>
          <div>
            <label htmlFor="title">Course Title: </label>
            <input type="text" id="title" name="title" />
          </div>
          <div>
            <label htmlFor="code">Course Code: </label>
            <input type="text" id="code" name="code" required />
          </div>
          <br />
          <div>
            <label htmlFor="prof">Professor: </label>
            <input type="text" id="prof" name="prof" required />
          </div>
          <div>
            <label htmlFor="slots">Enter Slots:</label>
            <input type="text" id="slots" name="slots" required />
            <button id="slot-add-btn" onClick={handleAddSlot}>+</button>
          </div>
          <button id="course-add-btn" onClick={handleAddCourse} className="btn">ADD COURSE</button>
        </form>

        <div className="slots-box">
          {slotsArray.map((slot) => (
            <p key={slot.id}>{slot.prof}: {slot.slots}</p>
          ))}
        </div>
      </div>
      <Courses courseArray={courseArray} />
    </>
  );
}

export default Form;
