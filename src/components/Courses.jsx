import '../styles/Courses.css'

function Courses({courseArray}) {
    const courses = courseArray;
return(
    <div style={{ display: courseArray.length === 0 ? 'none' : 'block' }} className="courses-wrapper">

        <div style = {{fontWeight: 'bolder'}}className='course-head'>
            <p>CODE</p>
            <p>TITLE</p>
            <p>SLOTS</p>
            <br></br>
        </div>

        {courseArray.map((course) => (
          <div className='course'>
            <p>{course.code}</p>
            <p>{course.title}</p>
            <div className="slots">
            {course.slots.map((slot)=> (
                <p>{slot.prof}: {slot.slots}</p>
            ))}
            </div>
            <br></br>
          </div>
        ))}
    </div>
)
}

export default Courses