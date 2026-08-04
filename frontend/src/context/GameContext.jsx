import { useState, createContext, useContext } from 'react';

const GameContext = createContext();

export function GameProvider({ children }) {
  const [game, setGame] = useState(null);
  const [isGameOver, setIsGameOver] = useState(false);
  const [winner, setWinner] = useState(null);
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
    setIsGameOver(false);
    setWinner(null);
    return data;
  };

  const nextPhase = async () => {
    const res = await fetch(`/api/continue?game_id=${gameId}`, { method: "POST" });
    const data = await res.json();
    setGame(data);

    if (data.isOver) {
      setIsGameOver(true);
      setWinner(data.winner);
    }

    return data;
  };

  const resetGame = () => {
    setGame(null);
    setGameId(null);
    setIsGameOver(false);
    setWinner(null);
  };

  return (
    <GameContext.Provider value={{ game, gameId, isGameOver, winner, nextPhase, startGame, resetGame }}>
      {children}
    </GameContext.Provider>
  );
}

export const useGame = () => useContext(GameContext);
