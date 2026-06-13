import { useState, createContext, useContext } from 'react';

const GameContext = createContext();

export function GameProvider({ children }) {
  const [game, setGame] = useState(null);
  const [gameId, setGameId] = useState(null);

  const startGame = async (names = []) => {
    const res = await fetch("/api/setup", { 
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ names }) 
    });
    const data = await res.json();
    setGameId(data.id);
    setGame(data);
    return data;
  };

  const nextPhase = async () => {
    const res = await fetch(`api/continue?game_id=${gameId}`, { method: "POST" });
    const data = await res.json();
    setGame(data);
    return data;
  };

  return (
    <GameContext.Provider value={{ game, gameId, nextPhase, startGame }}>
      {children}
    </GameContext.Provider>
  );
}

export const useGame = () => useContext(GameContext);