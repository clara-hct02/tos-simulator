import { useNavigate } from 'react-router-dom';

const Rules = () => {
    const navigate = useNavigate();
    
    return (
        <div>
            <h1>Rules</h1>

            <button onClick={() => navigate(-1)}>
                Go Back Home
            </button>
        </div>
    );
};

export default Rules;