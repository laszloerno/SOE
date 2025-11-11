// vulnerable-4.js (escape-like manual quoting)
const express = require('express');
const db = require('../db');
const app = express();
app.get('/byid', (req, res) => {
  const id = req.query.id;
  // naive escaping by wrapping in quotes
  const safeId = "'" + id + "'";
  db.all('SELECT * FROM data WHERE id = ' + safeId, [], (err, rows) => {
    if (err) return res.status(500).send(err);
    res.json(rows);
  });
});
app.listen(3003, () => console.log('vulnerable-4 listening on 3003'));
