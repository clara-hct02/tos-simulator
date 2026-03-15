import { useNavigate } from 'react-router-dom';

const Rules = () => {
  const navigate = useNavigate();
    
  return (
    <div>
      <h1>Rules</h1>
        <button onClick={() => navigate('/')}>
          Back
        </button>

        <h2>Factions</h2>
        <h3>Town</h3>
          The Town is the uninformed majority of the game. 
          <br></br>
          Win condition: Eliminate the Coven and Neutral Killers
        <h3> Coven </h3>
          The coven is the core informed minority. They are aware of all other members of their faction
          and can communicate with each other during the night. 
          <br></br>
          Win condition: Eliminate the Town and Neutral Killers
        <h2>Roles</h2>
        Note: This page will only include roles that are currently available within the simulator.
        <h3>Town</h3>
        <h3>Coven</h3>
      </div>
    );
};

export default Rules;