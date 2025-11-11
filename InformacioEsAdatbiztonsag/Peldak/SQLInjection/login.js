// vulnerable-login.js
// Oktatási cél: sebezhető példa — NE használd éles környezetben!
const express = require('express');
const db = require('./db'); // vagy '../db' ha a vulnerable mappában van
const app = express();
app.use(express.urlencoded({ extended: true }));

// egyszerű route betöltéshez (ha frontend nem ugyanazon porton)
app.get('/', (req, res) => {
  res.sendFile(require('path').resolve(__dirname, 'login.html'));
});

// SEBEZHETŐ login: string concat-tal építjük az SQL-t
app.post('/login', (req, res) => {
  const username = req.body.username || '';
  const password = req.body.password || '';
  // *** Itt a rossz gyakorlat: közvetlen beillesztés a SQL-be ***
  const sql =
    "SELECT id, username FROM users WHERE username = '" +
    username +
    "' AND password = '" +
    password +
    "' LIMIT 1";
  // (Megjegyzés: a 'password' mező itt demo célból email-ként van használva a seed szerkezetével összeillő egyszerűség miatt.)

  db.get(sql, [], (err, row) => {
    if (err) {
      // logold, de ne add túl részletesen vissza éles környezetben
      console.error('DB error (vulnerable):', err.message);
      return res.status(500).send('Internal server error (see server log)');
    }
    if (row) {
      res.send(`Sikeres belépés. Üdv, ${row.username}`);
    } else {
      res.status(401).send('Hibás belépési adatok');
    }
  });
});

app.listen(4000, () =>
  console.log('Vulnerable login demo listening on http://localhost:4000')
);
