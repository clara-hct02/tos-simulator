export function VotingUI({ game, onContinue }) {
  return (
    <div className="game-container">
      <h1>{game.phase} {game.day}</h1>

      <div className="events-container">
        {game.events.map((event, i) => (
          <p key={i} className="event">
            {event.text}
          </p>
        ))}
      </div>

      <div className="button-group">
        <button onClick={onContinue}>Continue</button>
      </div>
    </div>
  );
}
