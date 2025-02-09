# Bevezetés a HTML-be

Mi az a HTML?
A HTML (HyperText Markup Language) a weboldalak alapvető szerkezeti nyelve. Segítségével definiáljuk az oldal tartalmát és struktúráját.
• A HTML nem programozási nyelv, hanem jelölőnyelv.
• A HTML dokumentumok egy böngészőben jelennek meg, amely értelmezi és megjeleníti a HTML kódot.
• A HTML verziói fejlődtek az évek során, a legújabb szabvány a HTML5.

# HTML Dokumentum Szerkezete

Minden HTML dokumentum egy alapvető struktúrával rendelkezik. Az alábbi kód egy egyszerű HTML5 dokumentumot mutat be:

```html
<!DOCTYPE html>
<html lang="hu">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Első HTML Oldal</title>
  </head>
  <body>
    <h1>Üdvözöllek a HTML világában!</h1>
    <p>Ez egy bevezető HTML oldal.</p>
  </body>
</html>
```

Magyarázat:

- `<!DOCTYPE html>` – Meghatározza, hogy HTML5 dokumentummal van dolgunk.
- `<html>` – Ez a HTML dokumentum gyökéreleme.
- `<head>` – Metaadatokat tartalmaz (pl. karakterkódolás, cím).
- `<body>` – Itt található az oldal látható tartalma.
- `<h1>, <p>` – Címsor és bekezdés HTML elemek.

# Népszerű HTML Tagek

## Szöveges elemek

```html
<h1>Főcím</h1>
<h2>Alcím</h2>
<p>Ez egy bekezdés.</p>
<strong>Félkövér szöveg</strong>
<em>Dőlt szöveg</em>
Listaelemek
<ul>
  <li>Listaelem 1</li>
  <li>Listaelem 2</li>
</ul>

<ol>
  <li>Első elem</li>
  <li>Második elem</li>
</ol>
```

## Linkek és képek

```html
<a href="https://www.google.com">Google kereső</a>
<img src="image.jpg" alt="Kép leírása" width="300" />
```

## Táblázatok

<table border="1">
    <tr>
        <th>Név</th>
        <th>Kor</th>
    </tr>
    <tr>
        <td>Péter</td>
        <td>25</td>
    </tr>
</table>

```html
<table border="1">
  <tr>
    <th>Név</th>
    <th>Kor</th>
  </tr>
  <tr>
    <td>Péter</td>
    <td>25</td>
  </tr>
</table>
```

## Űrlapok

```html
<form action="submit.php" method="POST">
  <label for="name">Név:</label>
  <input type="text" id="name" name="name" />
  <input type="submit" value="Küldés" />
</form>
```
