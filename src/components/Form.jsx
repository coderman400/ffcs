import '../styles/Form.css';
import { useState } from 'react';
import Courses from './Courses.jsx';

function Form() {
  const [slotsArray, setSlotsArray] = useState([]);
  const [courseArray, setCourseArray] = useState([]);

  const handleAddSlot = (event) => {
    event.preventDefault();
    const slotsInput = document.getElementById('slots');
    const newSlot = {
      name: slotsInput.value.trim(),
      id: crypto.randomUUID()
    };

    if (newSlot) {
      setSlotsArray([...slotsArray, newSlot]); 
      slotsInput.value = ''; 
    }
  };

  const handleAddCourse = (event) => {
    event.preventDefault();
    const titleInput = document.getElementById('title');
    const codeInput = document.getElementById('code');

    const newCourse = {
      title: titleInput.value,
      code: codeInput.value,
      slots: slotsArray
    }

    if(newCourse){
      setCourseArray([...courseArray, newCourse]);
      titleInput.value='';
      codeInput.value='';
      setSlotsArray([]);
    }
  }

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
          <input type="text" id="code" name="code" />
        </div>
        <br />
        <div>
          <label htmlFor="slots">Enter Slots:</label>
          <input type="text" id="slots" name="slots" />
          <button id="slot-add-btn" onClick={handleAddSlot}>+</button>
        </div>
        <button id="course-add-btn" onClick={handleAddCourse}class="btn">ADD COURSE</button>
      </form>

      <div className="slots-box">
        {slotsArray.map((slot) => (
          <p key={slot.id}>{slot.name}</p>
        ))}
      </div>
    </div>
    <Courses courseArray={courseArray}></Courses>
  </>
  );
}

export default Form;
