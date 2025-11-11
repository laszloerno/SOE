const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const dbFile = path.resolve(__dirname, './data/testdb.sqlite');
const DBSOURCE = dbFile;
const db = new sqlite3.Database(DBSOURCE, (err) => {
  if (err) {
    console.error('Could not connect to SQLite', err);
  } else {
    console.log('Connected to SQLite DB at', DBSOURCE);
  }
});
module.exports = db;
