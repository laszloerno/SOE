// solution-2.js (whitelist order-by)
const express = require('express');
const db = require('../db');
const app = express();
const ALLOWED = ['name','price','created_at'];
app.get('/items', (req, res) => {
  const sort = req.query.sort;
  const col = ALLOWED.includes(sort) ? sort : 'name';
  db.all(`SELECT id, name, price FROM items ORDER BY ${col}`, [], (err, rows) => {
    if (err) return res.status(500).send('error');
    res.json(rows);
  });
});
app.listen(3101,()=>console.log('solution-2 listening on 3101'));
