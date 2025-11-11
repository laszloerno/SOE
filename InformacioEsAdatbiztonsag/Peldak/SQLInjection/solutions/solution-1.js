// solution-1.js (prepared using ? placeholders)
const express = require('express');
const db = require('../db');
const app = express();
app.get('/user', (req, res) => {
  const username = req.query.username || '';
  db.all('SELECT id, username, email FROM users WHERE username = ?', [username], (err, rows) => {
    if (err) return res.status(500).send('error');
    res.json(rows);
  });
});
app.listen(3100,()=>console.log('solution-1 listening on 3100'));
