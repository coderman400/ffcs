
import { useNavigate } from "react-router-dom";

function Submit(props) {
  const show = props.show;
  const courseArray = props.courseArray;
  const navigate = useNavigate();

  function handleSubmit() {
    console.log("CLICKED RESULT");
    navigate('/result');
  }

  return (
    <button
      onClick={handleSubmit}
      style={{ display: show ? 'block' : 'none', justifySelf: 'center', marginLeft: '100%' }}
    >
      SUBMIT COURSES
    </button>
  );
}

export default Submit;
