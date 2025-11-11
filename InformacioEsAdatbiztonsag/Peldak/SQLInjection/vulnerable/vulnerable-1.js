// vulnerable-1.js (sqlite string concat)
const express = require('express');
const db = require('../db');
const app = express();
app.get('/user', (req, res) => {
  const username = req.query.username;
  const sql =
    "SELECT id, username, email FROM users WHERE username = '" + username + "'";
  db.all(sql, [], (err, rows) => {
    if (err) return res.status(500).send(err);
    res.json(rows);
  });
});
app.listen(3000, () => console.log('vulnerable-1 listening on 3000'));
