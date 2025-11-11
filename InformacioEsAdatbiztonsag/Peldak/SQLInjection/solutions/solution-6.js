// solution-6.js (validated ids + prepared IN)
const express = require('express');
const db = require('../db');
const app = express();
app.use(express.json());
app.post('/delete-many', (req, res) => {
  let ids = req.body.ids;
  if (!Array.isArray(ids)) return res.status(400).send('ids must be array');
  ids = ids.map(i => parseInt(i,10)).filter(i => !Number.isNaN(i));
  if (ids.length === 0) return res.status(400).send('no valid ids');
  const placeholders = ids.map(_=>'?').join(', ');
  const sql = `DELETE FROM orders WHERE id IN (${placeholders})`;
  db.run(sql, ids, function(err) {
    if (err) return res.status(500).send('error');
    res.send('deleted');
  });
});
app.listen(3105,()=>console.log('solution-6 listening on 3105'));
