// solution-login.js
const express = require('express');
const db = require('./db'); // vagy '../db' ha máshol
const app = express();
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.sendFile(require('path').resolve(__dirname, 'login.html'));
});

// Javított: parametrizált lekérdezés és alap input-ellenőrzés
app.post('/login', (req, res) => {
  const username = (req.body.username || '').trim();
  const password = (req.body.password || '').trim();

  if (!username || !password)
    return res.status(400).send('Kérlek töltsd ki a mezőket');

  const sql =
    'SELECT id, username FROM users WHERE username = ? AND password = ? LIMIT 1';
  db.get(sql, [username, password], (err, row) => {
    if (err) {
      console.error('DB error (solution):', err.message);
      return res.status(500).send('Internal server error');
    }
    if (row) {
      res.send(`Sikeres belépés (secure). Üdv, ${row.username}`);
    } else {
      res.status(401).send('Hibás belépési adatok');
    }
  });
});

app.listen(4100, () =>
  console.log('Solution login demo listening on http://localhost:4100')
);
