import React from 'react';
import { HashRouter, Route, Routes } from 'react-router-dom';
import { StatusBar } from '@capacitor/status-bar';

import './App.css';

//import the different pages from the pages folder
//add your own pages here
import { Home, Settings } from './Pages';

const hideStatusBar = async () => {
  await StatusBar.hide();
};

const App = () => {
  hideStatusBar();
  return (
    <HashRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </HashRouter>
  );
};

export default App;
