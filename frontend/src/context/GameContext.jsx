import { useState, createContext, useContext } from 'react';
import { useNavigate } from 'react-router-dom';

const GameContext = createContext();

export function GameProvider({ children }) {
  const [game, setGame] = useState(null);
  const navigate = useNavigate();

  const startGame = async () => {
    const res = await fetch("/api/setup", { 
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({}) 
    });
    const data = await res.json();
    setGame(data);
    return data;
  };

  const nextPhase = async () => {
    const res = await fetch("api/continue", { method: "POST" });
    const data = await res.json();
    setGame(data);
    navigate(`/${data.phase}`);
  };

  return (
    <GameContext.Provider value={{ game, nextPhase, startGame }}>
      {children}
    </GameContext.Provider>
  );
}

export const useGame = () => useContext(GameContext);