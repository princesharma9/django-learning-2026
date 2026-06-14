import { useState, useEffect } from 'react'
 
import './App.css'

function App() {
  const [message, setMessage] = useState('')
useEffect(() => {
  fetch('http://localhost:8000/api/')
    .then(response => response.json())
    .then(data => setMessage(data))
    .catch(error => console.error('Error fetching data:', error));
}, [])
  return (
    <>
    <h1>Students Data from backend</h1>
       {/* <p>{JSON.stringify(message) || 'Loading...'}</p> */}
       <p>Name: { (message.name) || 'Loading...'}</p>
       <p>Age: { (message.age) || 'Loading...'}</p> 
       <p>Grade: { (message.grade) || 'Loading...'}</p>
       {/* {message.name && message.age && message.grade ? (
        <div>
          <p>Name: {message.name}</p>
          <p>Age: {message.age}</p>
          <p>Grade: {message.grade}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )} */}
    </>
  )
}

export default App
