// vulnerable-2.js (ORDER BY concat)
const express = require('express');
const db = require('../db');
const app = express();
app.get('/items', (req, res) => {
  const sort = req.query.sort || 'name';
  const sql = `SELECT id, name, price FROM items ORDER BY ${sort}`;
  db.all(sql, [], (err, rows) => {
    if (err) return res.status(500).send('error');
    res.json(rows);
  });
});
app.listen(3001,()=>console.log('vulnerable-2 listening on 3001'));
