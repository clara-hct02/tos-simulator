export function WinUI({ game, onRestart }) {
  return (
    <div className="game-container">
      <h1>{game.winner} Wins!!</h1>

      <div className="button-group">
        <button onClick={onRestart}>Restart</button>
      </div>
    </div>
  );
}
