import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './App.css';

function App() {
  const [data, setData] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("api/setup");
      const jsonData = await response.json();
      setData(jsonData.message);
    };

    fetchData();
  }, []);

  return (
    <>
      <section id="center">
        <div className="hero">
        </div>
        <div>
          <h1>Welcome to Town of Salem 2 Simulator</h1>
        </div>
        <div>
          <div>{data || "Loading..."}</div>
        </div>
      </section>

      <button onClick={() => navigate('day', {
          state: { day: 1 }
        })}>
        Start
      </button>
      
      <button onClick={() => navigate('rules')}>
        Rules
      </button>
    </>
  )
}

export default App
