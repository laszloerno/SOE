const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');
const dbFile = './data/testdb.sqlite';
if (!fs.existsSync('./data')) fs.mkdirSync('./data');
if (fs.existsSync(dbFile)) {
  console.log('Database file exists:', dbFile);
  process.exit(0);
}
const db = new sqlite3.Database(dbFile);
db.serialize(() => {
  db.run(
    `CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, email TEXT, password TEXT, isadmin INTEGER DEFAULT 0)`
  );
  db.run(
    `CREATE TABLE items (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, created_at TEXT)`
  );
  db.run(
    `CREATE TABLE comments (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, text TEXT)`
  );
  db.run(
    `CREATE TABLE data (id INTEGER PRIMARY KEY AUTOINCREMENT, value TEXT)`
  );
  db.run(
    `CREATE TABLE articles (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT)`
  );
  db.run(
    `CREATE TABLE orders (id INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT)`
  );
  db.run(
    `CREATE TABLE profiles (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, bio TEXT)`
  );
  // insert sample data
  const users = db.prepare(
    'INSERT INTO users (username,email,password, isadmin) VALUES (?,?,?,?)'
  );
  users.run('alice', 'alice@example.com', 'alicepass', 0);
  users.run('bob', 'bob@example.com', 'bobpass', 0);
  users.run('admin', 'admin@example.com', 'adminpass', 1);
  users.run('guest', 'guest@example.com', 'guestpass', 0);
  users.run('user', 'user@example.com', 'userpass', 0);
  users.run('user2', 'user2@example.com', 'user2pass', 0);
  users.run('user3', 'user3@example.com', 'user3pass', 0);
  users.run('user4', 'user4@example.com', 'user4pass', 0);
  users.finalize();
  const items = db.prepare(
    'INSERT INTO items (name,price,created_at) VALUES (?,?,?)'
  );
  items.run('apple', 1.2, new Date().toISOString());
  items.run('banana', 0.8, new Date().toISOString());
  items.finalize();
  const articles = db.prepare('INSERT INTO articles (title) VALUES (?)');
  articles.run('Intro to SQL');
  articles.run('Node.js security');
  articles.finalize();
  const profiles = db.prepare('INSERT INTO profiles (name,bio) VALUES (?,?)');
  profiles.run('Alice', 'Loves code');
  profiles.run('Bob', 'Enjoys databases');
  profiles.finalize();
  db.run("INSERT INTO data (value) VALUES ('one')");
  db.run("INSERT INTO data (value) VALUES ('two')");
  db.run("INSERT INTO orders (description) VALUES ('order 1')");
  db.run("INSERT INTO orders (description) VALUES ('order 2')");
  db.run("INSERT INTO comments (user_id, text) VALUES (1, 'Hello')");
});
db.close(() => console.log('Seed complete. DB at', dbFile));
