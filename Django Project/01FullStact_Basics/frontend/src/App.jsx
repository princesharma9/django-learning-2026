import { useEffect, useState } from 'react'
import { Route, Router, Routes } from 'react-router-dom'
import './App.css'
import StudentDetail from './components/StudentDetail'
import StudentsList from './components/StudentsList'


function App() {
  const [data, setData] = useState([])

  useEffect(() =>{
    fetch('http://127.0.0.1:8000/stuList/')
    .then((response) => response.json())
    .then((data) => {
      console.log('Data', data);
      setData(data)
      
    })
    .catch((Error) => {
      console.log('Error:', Error);
      
    })

  }, [])

  return (
    <>
      <Routes>

        <Route path='/' element ={<StudentsList data = {data} />} />
        <Route path='/student/:id' element ={<StudentDetail />} />
      
      </Routes>

    </>
  )
}

export default App
