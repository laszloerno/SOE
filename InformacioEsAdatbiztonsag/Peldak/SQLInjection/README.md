# SQLi Workshop — Node.js / Express (SQLite, no external DB required)

Ez a változat **SQLite**-ot használ helyi fájlban (`./data/testdb.sqlite`), így **nem kell MySQL** vagy Docker.
Csak Node.js (>=16) szükséges a futtatáshoz.

## Gyorsstart

1. `npm install`
2. `npm run seed` # létrehozza és feltölti a `./data/testdb.sqlite` fájlt
3. `node index.js` vagy `npm start`
4. Böngésző: http://localhost:3000 (vulnerable-1), 3001 (vulnerable-2), ... vagy DEMO=s_all node index.js

## Tartalom

- `vulnerable/` és `solutions/` – mint korábban, de SQLite-ot használnak
- `seed.js` – init és sample adatok

DEMO=v4 node index.js

node login.js
