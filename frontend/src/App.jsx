import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './App.css';

function App() {
  const [count, setCount] = useState(0);
  const [data, setData] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:8000/data");
        const jsonData = await response.json();
        setData(jsonData.message);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  function handleRules() {
    alert('You clicked rules');
    navigate('rules');
  }

  function handleStart() {
    alert('You clicked start');
  }

  return (
    <>
      <section id="center">
        <div className="hero">
        </div>
        <div>
          <h1>Welcome to Town of Salem 2 Simulator</h1>
        </div>
        <button
          className="counter"
          onClick={() => setCount((count) => count + 1)}
        >
          Count is {count}
        </button>
        <div>
          <div>{data || "Loading..."}</div>
        </div>
      </section>

      <button id="start" onClick={handleStart}>Start</button>
      <button id="rules" onClick={handleRules}>Rules</button>
    </>
  )
}

export default App
