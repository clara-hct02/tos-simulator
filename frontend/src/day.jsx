import { useNavigate } from 'react-router-dom';
import { useLocation } from 'react-router';

const Day = () => {
  let location = useLocation();

  const navigate = useNavigate();
  const day = location.state?.day;
    
  return (
    <div>
      <h1>Day {day}</h1>
        <button onClick={() => navigate('/')}>
          Back
        </button>

        <button onClick={() => navigate('')}>
          Continue
        </button>
      </div>
    );
};

export default Day;