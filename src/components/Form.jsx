import '../styles/Form.css';
import { useState } from 'react';
import Courses from './Courses.jsx';

function Form() {
  const [slotsArray, setSlotsArray] = useState([]);
  const [courseArray, setCourseArray] = useState([]);
  const [error, setError] = useState('');

 const slotRegex = /^(?:([A-G][1-2]|(TAA[12]|TCC[12]|TBB2|TDD2)|V[1-7]|L([1-5]?[0-9])\+L(\3|[1-5]?[0-9]))(?:\+[TA][A-G][1-2])?)(?:,(?:([A-G][1-2]|(TAA[12]|TCC[12]|TBB2|TDD2)|V[1-7]|L([1-5]?[0-9])\+L(\7|[1-5]?[0-9]))(?:\+[TA][A-G][1-2])?))*$/i;


  const handleAddSlot = (event) => {
    event.preventDefault();
    const slotsInput = document.getElementById('slots');
    const profInput = document.getElementById('prof');
    const slotsValue = slotsInput.value.trim();
    const profValue = profInput.value.trim();

    if (!slotRegex.test(slotsValue)) {
      setError('Invalid slot. Please enter slots separated by commas (Eg: C1,C2,L54+L55,L23+L24)');
      return;
    }

    setError('');

    const newSlot = {
      prof: profValue,
      slots: slotsValue.toUpperCase(),
      id: crypto.randomUUID(),
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
      slots: slotsArray,
    };

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
          {error && <p style={{ color: 'red' }}>{error}</p>}
          <button id="course-add-btn" onClick={handleAddCourse} className="btn">
            ADD COURSE
          </button>
        </form>

        <div className="slots-box">
          {slotsArray.map((slot) => (
            <p key={slot.id}>
              {slot.prof}: {slot.slots}
            </p>
          ))}
        </div>
      </div>
      <Courses courseArray={courseArray} />
    </>
  );
}

export default Form;
