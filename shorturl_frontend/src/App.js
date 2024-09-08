import logo from './logo.svg';
import './App.css';
import React from 'react';
import './index.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          <div className="text-3xl font-bold underline font-sans bg-green-400">
            Hello worlddd
          </div>
          <p>
            <MyButton />
          </p>
        </a>
      </header>
    </div>
  );
}

function MyButton() {
  return (
    <button className="text-3xl font-bold bg-green-200">I'm a button</button>
  );
}

export default App;
