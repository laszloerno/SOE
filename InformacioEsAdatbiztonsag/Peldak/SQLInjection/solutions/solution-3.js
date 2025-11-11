// solution-3.js (prepared + int check)
const express = require('express');
const db = require('../db');
const app = express();
app.use(express.urlencoded({extended:true}));
app.post('/comment', (req, res) => {
  const text = req.body.text || '';
  const userId = parseInt(req.body.userId, 10);
  if (Number.isNaN(userId)) return res.status(400).send('invalid userId');
  db.run('INSERT INTO comments(user_id, text) VALUES (?, ?)', [userId, text], function(err) {
    if (err) return res.status(500).send('error');
    res.send('ok');
  });
});
app.listen(3102,()=>console.log('solution-3 listening on 3102'));
