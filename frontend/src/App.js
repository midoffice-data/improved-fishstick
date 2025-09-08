import React from 'react';
import logo from './logo.svg';
import axios from 'axios';
import './App.css';

require('dotenv').config()

function detectCodespacesApiBase() {
  try {
    const { protocol, host } = window.location;
    // Codespaces hosts look like: 3000-<id>.<domain>
    if (host.includes('-') && (host.endsWith('.github.dev') || host.endsWith('.app.github.dev') || host.endsWith('githubpreview.dev'))) {
      const firstDash = host.indexOf('-');
      const prefix = host.substring(0, firstDash);
      const rest = host.substring(firstDash + 1);
      if (/^\d+$/.test(prefix)) {
        return `${protocol}//8000-${rest}`;
      }
    }
  } catch (e) {}
  return '';
}

const API_BASE = (process.env.REACT_APP_API_BASE_URL || detectCodespacesApiBase()).replace(/\/$/, '');

function handleSubmit(event) {
  const text = document.querySelector('#char-input').value

  axios
    .get(`${API_BASE}/char_count?text=${encodeURIComponent(text)}`).then(({data}) => {
      document.querySelector('#char-count').textContent = `${data.count} characters!`
    })
    .catch(err => console.log(err))
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div>
        <label htmlFor='char-input'>How many characters does </label>
        <input id='char-input' type='text' placeholder="my string"/><span> </span>
        <button onClick={handleSubmit}>have?</button>
        <div>
          <h3 id='char-count' data-testid="char-count"> </h3>
        </div>
      </div>
      </header>
    </div>
  );
}

export default App;
