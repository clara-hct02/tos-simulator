import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './index.css'
import App from './App.jsx'
import Rules from './rules.jsx'
import Day from '../phases/Day.jsx'
import Voting from '../phases/Voting.jsx'
import Judgement from '../phases/Judgement.jsx'
import Night from '../phases/Night.jsx'
import Win from './win.jsx'
import { GameProvider } from './context/GameContext.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <GameProvider>
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/rules" element={<Rules />} />
          <Route path="/day" element={<Day />} />
          <Route path="/voting" element={<Voting />} />
          <Route path="/judgement" element={<Judgement />}/>
          <Route path="/night" element={<Night />} />
          <Route path="/win" element={<Win />} />
        </Routes>
      </GameProvider>
    </BrowserRouter>
  </StrictMode>
)