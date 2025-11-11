// vulnerable-5.js (raw LIKE concat)
const express = require('express');
const db = require('../db');
const app = express();
app.get('/search', (req, res) => {
  const q = req.query.q || '';
  const sql = "SELECT id, title FROM articles WHERE title LIKE '%" + q + "%'";
  db.all(sql, [], (err, rows) => {
    if (err) return res.status(500).send('error');
    res.json(rows);
  });
});
app.listen(3004,()=>console.log('vulnerable-5 listening on 3004'));
