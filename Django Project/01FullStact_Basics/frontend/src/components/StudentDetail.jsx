import { useParams } from 'react-router-dom'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

function StudentDetail() {
  const { id } = useParams()
  const [student, setStudent] = useState(null)

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/stuDetails/${id}/`)
      .then(res => res.json())
      .then(data => setStudent(data))
  }, [id])

  if (!student) {
    return <h2>Loading...</h2>
  }

  return (
    <>
      <h1>{student.name}</h1>
      <p>Roll No: {student.roll_no}</p>
      <p>Email: {student.email}</p>
      <Link to={`/`}>
            <button>Back to Students List</button>
          </Link>
    </>
  )
}

export default StudentDetail