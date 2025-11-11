# Tesztesetek a SQLite változathoz

1. seed: futtasd `node seed.js` egyszer, hogy létrejöjjön a ./data/testdb.sqlite fájl
2. vulnerable-1: http://localhost:3000/user?username=akarmi' or '1'='1
3. vulnerable-2: http://localhost:3001/items?sort=price vagy ?sort=nonexistent
4. vulnerable-3: POST /comment form body text=I'm fine, userId=1
5. vulnerable-4: http://localhost:3003/byid?id=123abc. http://localhost:3003/byid?id=' or ''='
   byid?id=' union SELECT 1,name FROM sqlite_master WHERE ''='
6. vulnerable-5: http://localhost:3004/search?q=O'Reilly
7. vulnerable-6: POST /delete-many ids: ["1","2"]
8. vulnerable-8: http://localhost:3007/profile?id=not-a-number
