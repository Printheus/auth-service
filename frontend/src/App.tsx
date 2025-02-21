import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SignInSide from './temp/SignInSide/SignInSide';
import SignIn from './SignIn/SignIn';
// import SignInSide from './SignInSide';



const App: React.FC = () => {
  return (
      <Router>
        <Routes>
          <Route path='/' element={<SignInSide/>}/>
          <Route path="/test" element={<SignIn/>} />
        </Routes>
      </Router>
  );
};

export default App;
