// solution-8.js (no info leak)
const express = require('express');
const db = require('../db');
const app = express();
app.get('/profile', (req, res) => {
  const id = req.query.id;
  db.all('SELECT * FROM profiles WHERE id = ?', [id], (err, rows) => {
    if (err) {
      console.error('DB error', err);
      return res.status(500).send('internal server error');
    }
    res.json(rows[0] || {});
  });
});
app.listen(3107,()=>console.log('solution-8 listening on 3107'));
