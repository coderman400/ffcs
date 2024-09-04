import '../styles/Courses.css'

function Courses({courseArray}) {
    const courses = courseArray;
return(
    <div style={{ display: courseArray.length === 0 ? 'none' : 'block' }} class="courses-wrapper">

        <div style = {{fontWeight: 'bolder'}}class='course'>
            <p>CODE</p>
            <p>TITLE</p>
            <p>SLOTS</p>
            <br></br>
        </div>

        {courseArray.map((course) => (
          <div class='course'>
            <p>{course.code}</p>
            <p>{course.title}</p>
            <div class="slots">
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