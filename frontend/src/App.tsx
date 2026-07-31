// App.tsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { CssBaseline, ThemeProvider } from '@mui/material';
import theme from './theme';

import SignIn from './SignIn/SignIn';
import Home from './Home';

const App: React.FC = () => {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/auth" element={<SignIn />} />
          <Route path="*" element={<div>404 Route Not Found</div>} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
};

export default App;
