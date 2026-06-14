import { Link } from 'react-router-dom'

function StudentsList({ data }) {
  return (
    <>
   
   <div className='body'>
      {data.map((student) => (
            <div key={student.id} className='student'>
          <h3>{student.name}</h3>

          <Link to={`/student/${student.id}`}>
            <button>More Details</button>
          </Link>
        </div>
      ))}
      </div>
    </>
  )
}

export default StudentsList