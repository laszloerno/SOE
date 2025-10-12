// server_fixed.js
// Demo fixed server: returns GENERAL error messages and uses blinding simulation
// Usage: node server_fixed.js
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());

// synchronous sleep (blocks event loop) used here only for deterministic demo timing
function sleepSync(ms) {
  const t0 = Date.now();
  while (Date.now() - t0 < ms) {}
}

// simulate decryption with blinding & normalized timing
function fakeDecryptWithBlinding(ciphertext) {
  const start = Date.now();
  const ok = ciphertext === 'good';
  const internal = ok
    ? { ok: true, plaintext: 'SENSITIVE: account=Alice;amount=1000' }
    : { ok: false };
  const MIN_MS = 50; // ensure minimum processing time to reduce timing leakage
  const elapsed = Date.now() - start;
  if (elapsed < MIN_MS) sleepSync(MIN_MS - elapsed);
  return internal;
}

app.post('/decrypt', (req, res) => {
  const ct = req.body && req.body.ciphertext;
  if (!ct) return res.status(400).json({ error: 'Invalid request' });

  const r = fakeDecryptWithBlinding(ct);

  if (!r.ok) {
    // GOOD: generic error, no padding details
    return res.status(400).json({ error: 'Invalid request' });
  }
  return res.status(200).json({ ok: true, data: r.plaintext });
});

const PORT = 3000;
app.listen(PORT, () => console.log('Fixed server listening on', PORT));
