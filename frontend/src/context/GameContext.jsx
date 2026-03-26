import { useState, createContext } from 'react';

const GameContext = createContext();

export function GameProvider({ children }) {
  const [game, setGame] = useState(null);

  const nextPhase = async () => {
    const res = await fetch("api/continue", { method: "POST" });
    const data = await res.json();
    setGame(data);
    // navigate(`/${data.phase}`);
  };

  return (
    <GameContext.Provider value={{ game, nextPhase }}>
      {children}
    </GameContext.Provider>
  );
}

export const useGame = () => useContext(GameContext);