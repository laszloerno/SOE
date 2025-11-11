// solution-4.js (int casting + placeholder)
const express = require('express');
const db = require('../db');
const app = express();
app.get('/byid', (req, res) => {
  const id = parseInt(req.query.id, 10);
  if (Number.isNaN(id)) return res.status(400).send('invalid id');
  db.all('SELECT * FROM data WHERE id = ?', [id], (err, rows) => {
    if (err) return res.status(500).send('err');
    res.json(rows);
  });
});
app.listen(3103,()=>console.log('solution-4 listening on 3103'));
