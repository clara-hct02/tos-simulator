export function JudgementUI({ game, onContinue }) {
  return (
    <div className="game-container">
      <h1>{game.phase} {game.day}</h1>

      <div className="events-container">
        {game.events.map((event, i) => (
          <div key={i} className="event">
            <p>{event.text}</p>
          </div>
        ))}
      </div>

      <div className="button-group">
        <button onClick={onContinue}>Continue</button>
      </div>
    </div>
  );
}
