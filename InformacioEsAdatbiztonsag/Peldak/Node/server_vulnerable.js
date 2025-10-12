// server_vulnerable.js
// Demo vulnerable server: shows explicit padding errors (DO NOT use in production)
// Usage: node server_vulnerable.js
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());

// Fake 'decrypt' that treats 'good' as valid ciphertext, anything else invalid
function fakeDecrypt(ciphertext) {
  // In real life you'd call crypto.privateDecrypt or similar. Here we simulate.
  if (ciphertext === 'good') {
    return { ok: true, plaintext: 'SENSITIVE: account=Alice;amount=1000' };
  } else {
    return { ok: false, error: 'PKCS1 padding invalid' };
  }
}

app.post('/decrypt', (req, res) => {
  const ct = req.body && req.body.ciphertext;
  if (!ct) return res.status(400).json({ error: 'missing ciphertext' });

  const r = fakeDecrypt(ct);
  if (!r.ok) {
    // VULNERABLE: returning specific padding error leaks information
    return res.status(400).json({ error: 'Padding error: ' + r.error });
  }
  return res.status(200).json({ ok: true, data: r.plaintext });
});

const PORT = 3000;
app.listen(PORT, () => console.log('Vulnerable server listening on', PORT));
