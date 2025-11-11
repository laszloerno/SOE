// vulnerable-8.js (info leak)
const express = require('express');
const db = require('../db');
const app = express();
app.get('/profile', (req, res) => {
  const id = req.query.id;
  db.all("SELECT * FROM profiles WHERE id = ?", [id], (err, rows) => {
    if (err) {
      return res.status(500).send(err.message);
    }
    res.json(rows[0] || {});
  });
});
app.listen(3007,()=>console.log('vulnerable-8 listening on 3007'));
