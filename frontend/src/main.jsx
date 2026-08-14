import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './index.css'
import App from './App.jsx'
import Rules from './rules.jsx'
import About from './about.jsx'
import GamePage from './pages/GamePage.jsx'
import { GameProvider } from './context/GameContext.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <GameProvider>
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/rules" element={<Rules />} />
          <Route path="/about" element={<About />} />
          <Route path="/game" element={<GamePage />} />
        </Routes>
      </GameProvider>
    </BrowserRouter>
  </StrictMode>
)
