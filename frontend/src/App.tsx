import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SignInSide from './temp/SignInSide/SignInSide';
import SignIn from './SignIn/SignIn';
import { CssBaseline } from '@mui/material';
import { ThemeProvider } from '@emotion/react';
import theme from './theme';
// import SignInSide from './SignInSide';



const App: React.FC = () => {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Routes>
          <Route path='/test' element={<SignInSide/>}/>
          <Route path="/sign-in" element={<SignIn/>} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
};

export default App;
