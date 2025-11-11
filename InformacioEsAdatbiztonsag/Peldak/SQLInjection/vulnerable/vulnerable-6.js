// vulnerable-6.js (IN concat)
const express = require('express');
const db = require('../db');
const app = express();
app.use(express.json());
app.post('/delete-many', (req, res) => {
  const ids = req.body.ids;
  const sql = `DELETE FROM orders WHERE id IN (${ids})`;
  db.run(sql, function(err) {
    if (err) return res.status(500).send('error');
    res.send('deleted');
  });
});
app.listen(3005,()=>console.log('vulnerable-6 listening on 3005'));
