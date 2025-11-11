// solution-5.js (LIKE with placeholder)
const express = require('express');
const db = require('../db');
const app = express();
app.get('/search', (req, res) => {
  const q = req.query.q || '';
  db.all('SELECT id, title FROM articles WHERE title LIKE ?', ['%'+q+'%'], (err, rows) => {
    if (err) return res.status(500).send('error');
    res.json(rows);
  });
});
app.listen(3104,()=>console.log('solution-5 listening on 3104'));
