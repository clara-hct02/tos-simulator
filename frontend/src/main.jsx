import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './index.css'
import App from './App.jsx'
import Rules from './rules.jsx'
import Day from './day.jsx'
import { GameProvider } from './context/GameContext.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <GameProvider>
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/rules" element={<Rules />} />
          <Route path="/day" element={<Day />} />
        </Routes>
      </GameProvider>
    </BrowserRouter>
  </StrictMode>
)