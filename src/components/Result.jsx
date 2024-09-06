import { useLocation } from "react-router-dom"
function Result(){
    const location = useLocation();
    const {data} = location.state || {};
    console.log(data)
    return(
        <>
        {data && data.map((course) => (
          <div key={course.code}>
            <h1>{course.code} {course.title}</h1>
            {course.slots.map((slot, index) => (
              <h2 key={index}>{slot.prof}: {slot.slots}</h2>
            ))}
          </div>
        ))}
      </>
    )
}
export default Result