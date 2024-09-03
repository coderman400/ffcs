import '../styles/Form.css';
import { useState } from 'react';
import Courses from './Courses.jsx';

function Form() {
  const [slotsArray, setSlotsArray] = useState([]);

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

  return (
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
        <div>
          <label htmlFor="type">Type:</label>
          <select id="type" name="type">
            <option value="eth">Embedded Lab + Theory</option>
            <option value="th">Theory Only</option>
          </select>
        </div>
        <br />
        <div>
          <label htmlFor="slots">Enter Slots:</label>
          <input type="text" id="slots" name="slots" />
          <button id="slot-add-btn" onClick={handleAddSlot}>+</button>
        </div>
      </form>

      <div className="slots-box">
        {slotsArray.map((slot) => (
          <p key={slot.id}>{slot.name}</p>
        ))}
      </div>
    </div>
  );
}

export default Form;
