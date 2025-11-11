# Node.js / Express — Vulnerable Example Snippets (for teaching)

Az alábbi `.md` fájl rövid, jól strukturált példa-kódrészleteket tartalmaz **Node.js / Express** környezetben.

> **Használat:** ne futtasd ezeket éles környezetben. Oktatási demo esetén izolált sandboxot (pl. Docker) használj.

---

## 1) Egyszerű string-összefűzés MySQL-hez

```js
// vulnerable-1.js
const express = require('express');
const mysql = require('mysql2');
const app = express();
app.get('/user', async (req, res) => {
  const username = req.query.username; // pl. ?username=...
  const conn = mysql.createConnection({
    host: 'localhost',
    user: 'app',
    password: 'pw',
    database: 'test',
  });
  const sql =
    "SELECT id, username, email FROM users WHERE username = '" + username + "'";
  conn.query(sql, (err, rows) => {
    if (err) return res.status(500).send('error');
    res.json(rows);
  });
});
app.listen(3000);
```

**Tipp:** nézd meg, hogyan épül a `sql` string — mi történik, ha a `username` tartalma idézőjelet vagy SQL kódot tartalmaz?

---

## 2) Dinamikus ORDER BY

```js
// vulnerable-2.js
app.get('/items', (req, res) => {
  const sort = req.query.sort || 'name'; // pl. ?sort=price
  db.query(
    `SELECT id, name, price FROM items ORDER BY ${sort}`,
    (err, rows) => {
      if (err) return res.status(500).send('error');
      res.json(rows);
    }
  );
});
```

**Tipp:** az `ORDER BY` oszlopnevet nem lehet egyszerűen "paraméterként" preparálni — gondold végig, milyen validáció vagy whitelist kellene ide.

---

## 3) Több-utas lekérdezés / `; DROP TABLE` veszély

```js
// vulnerable-3.js
app.post('/comment', express.urlencoded({ extended: true }), (req, res) => {
  const text = req.body.text;
  const userId = req.body.userId;
  const sql =
    'INSERT INTO comments(user_id, text) VALUES (' +
    userId +
    ", '" +
    text +
    "');";
  // képzeld el, ha a driver engedélyezi az egy híváson belüli több statement feldolgozást...
  db.query(sql, (err) => {
    if (err) return res.status(500).send('error');
    res.send('ok');
  });
});
```

**Tipp:** ellenőrizd, képes-e a DB driver több SQL utasítást egy `query` hívásban lefuttatni — és hogyan lehet ezt megakadályozni.

---

## 4) Parameterizálás helyett `escape` helytelen használata (félmegoldás)

```js
// vulnerable-4.js
const mysql2 = require('mysql2');
const pool = mysql2.createPool({
  host: 'localhost',
  user: 'app',
  password: 'pw',
  database: 'test',
});
app.get('/byid', (req, res) => {
  const id = req.query.id;
  // valaki próbálkozott escape-el, de nem mindig elég:
  const safeId = pool.escape(id);
  pool.query('SELECT * FROM data WHERE id = ' + safeId, (err, rows) => {
    if (err) return res.status(500).send('err');
    res.json(rows);
  });
});
```

**Tipp:** `escape` függvények driverenként másként viselkednek — és a legjobb gyakorlat a prepared statement. Gondold át a tárolt típus és a kezelt input megfelelőségét.

---

## 5) Raw query a Sequelize-ban (nyers string concat)

```js
// vulnerable-5.js
const { Sequelize } = require('sequelize');
const seq = new Sequelize('db', 'user', 'pw', { dialect: 'mysql' });
app.get('/search', async (req, res) => {
  const q = req.query.q || '';
  // raw query string összeillesztve
  const rows = await seq.query(
    "SELECT id, title FROM articles WHERE title LIKE '%" + q + "%'"
  );
  res.json(rows[0]);
});
```

**Tipp:** Sequelize tud parameterizált `replacements`-t — nézd meg, hogyan kellene használni azt.

---

## 6) Mass delete — felhasználói lista közvetlen beillesztése

```js
// vulnerable-6.js
app.post('/delete-many', express.json(), (req, res) => {
  const ids = req.body.ids; // várt: [1,2,3]
  // rossz gyakorlat: JSON tömb átfordítva stringgé és beszúrva az IN-be
  const sql = `DELETE FROM orders WHERE id IN (${ids})`;
  db.query(sql, (err) => {
    if (err) return res.status(500).send('error');
    res.send('deleted');
  });
});
```

**Tipp:** mi történik, ha `ids` tartalma nem tömb, hanem valami más (pl. string)? Gondold meg, hogyan bontanád le és ellenőriznéd a bemenetet.

---

## 7) Secrets/credentials „hardcoded” a forrásban

```js
// vulnerable-7.js
const pool = require('mysql2').createPool({
  host: 'db.example.local',
  user: 'root', // <-- rossz: root használata
  password: 'SuperSecretPassword123!', // <-- rossz: jelszó forráskódban
  database: 'maindb',
});
```

**Tipp:** milyen szerepkör (least privilege) lenne helyes? Hol tároljuk biztonságosan a titkokat produkcióban?

---

## 8) Hibakezelés huzamosan (információszivárgás)

```js
// vulnerable-8.js
app.get('/profile', (req, res) => {
  const id = req.query.id;
  pool.query('SELECT * FROM profiles WHERE id = ?', [id], (err, rows) => {
    if (err) {
      // részletes DB hiba visszaadása a kliensnek — információszivárgás
      return res.status(500).send(err.message);
    }
    res.json(rows[0] || {});
  });
});
```

**Tipp:** mit ne küldj vissza a kliensnek éles környezetben, és hogyan kezeld a logolást helyesen?
