
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import axios from "axios";

function Submit(props) {
  const [loading, setLoading] = useState(false);
  const show = props.show;
  const courseArray = props.courseArray;
  const navigate = useNavigate();

 async function handleSubmit() {
    console.log("CLICKED RESULT");
    setLoading(true)
    try{
      const response = await axios.post('http://192.168.59.109:8000/apis/combined/',{
        courses: courseArray
      });

      const resultData = await response.data;

      navigate('/result', {state: {data: resultData}})
    }catch(e){
      console.error('ERROR SENDING DATA: ', e)
    }finally{
      setLoading(false)
    }
    
  }

  return (
    <button
      onClick={handleSubmit}
      style={{ display: show ? 'block' : 'none', justifySelf: 'center', marginLeft: '100%', disabled: {loading} } }>
      {loading ? 'Loading... ': 'SUBMIT COURSES' }
    </button>
  );
}

export default Submit;
