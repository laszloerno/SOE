// vulnerable-3.js (INSERT concat)
const express = require('express');
const db = require('../db');
const app = express();
app.use(express.urlencoded({ extended: true }));
app.post('/comment', (req, res) => {
  const text = req.body.text;
  const userId = req.body.userId;
  const sql =
    'INSERT INTO comments(user_id, text) VALUES (' +
    userId +
    ", '" +
    text +
    "');";
  db.run(sql, function (err) {
    if (err) return res.status(500).send(err);
    res.send('ok');
  });
});
app.listen(3002, () => console.log('vulnerable-3 listening on 3002'));
