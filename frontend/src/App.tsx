import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SignInSide from './temp/SignInSide/SignInSide';
// import SignInSide from './SignInSide';



const App: React.FC = () => {
  return (
      <Router>
        <Routes>
          <Route path='/' element={<SignInSide/>}/>
        </Routes>
      </Router>
  );
};

export default App;
