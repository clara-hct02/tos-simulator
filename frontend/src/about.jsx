import { useNavigate } from 'react-router-dom';

const About = () => {
  const navigate = useNavigate();
    
  return (
    <div className="game-container">
        <h1> About </h1>
        Town of Salem 2 simulator is a passion project by <a href="https://github.com/clara-hct02">Clara</a>, 
        also known as Kana in social deduction game circles. It was started in 2024 as a console project 
        that can be viewed <a href="https://github.com/clara-hct02/tos-simulator-old">here</a>. 

        <br></br>
        <br></br>

        The github repo for this project can be viewed <a href="https://github.com/clara-hct02/tos-simulator">here</a>.

        <br></br>
        <br></br>

        This project was inspired by Bransteele's Hunger Games simulator.

        <div className="button-group">
            <button onClick={() => navigate('/')}>
            Back
            </button>
        </div>
      </div>
    );
};

export default About;