# Bevezetés a CSS-be

## Mi az a CSS?

A CSS (Cascading Style Sheets) egy stíluslap nyelv, amelyet a HTML dokumentumok megjelenésének formázására használnak.

- A HTML szerkezeti alapot biztosít, míg a CSS a vizuális megjelenést határozza meg.
- A CSS lehetővé teszi az oldalak elrendezését, színezését, animációkat és reszponzív dizájnt.
- A legújabb szabvány a CSS3, amely további fejlett vizuális lehetőségeket biztosít.

## CSS Kapcsolási módok

A CSS-t háromféleképpen lehet csatolni egy HTML dokumentumhoz:

### Inline CSS – az adott HTML elemben definiálva a style attribútummal.

```html
<p style="color: red; font-size: 20px;">Ez egy piros szöveg.</p>
```

### Belső (internal) CSS –

A `<style>` blokkban a HTML dokumentum `<head>` részében.

```html
<head>
  <style>
    p {
      color: blue;
      font-size: 18px;
    }
  </style>
</head>
```

### Külső (external) CSS – egy külön .css fájlban, amelyet a `<link>` segítségével csatolunk.

```html
<head>
  <link rel="stylesheet" href="styles.css" />
</head>
```

## Alap CSS Tulajdonságok

Szövegformázás

```css
p {
  font-size: 16px;
  color: #333;
  font-family: Arial, sans-serif;
  text-align: center;
}
```

Háttér és színezés

```css
body {
  background-color: lightgray;
}

h1 {
  color: navy;
  background-color: yellow;
}
```

Elrendezések és dobozmodell

```css
.container {
  width: 80%;
  margin: 0 auto;
  padding: 20px;
  border: 2px solid black;
}
```

# Feladat 1 : Flexbox - Mondriani festmény elkészítése

A CSS Flexbox segít rugalmas elrendezéseket készíteni, például Piet Mondrian híres festményét is.

```html
<div class="mondrian">
  <div class="box red"></div>
  <div class="box blue"></div>
  <div class="box yellow"></div>
  <div class="box white"></div>
  <div class="box black"></div>
</div>
```

CSS Stílusok

```css
.mondrian {
  display: flex;
  flex-wrap: wrap;
  width: 400px;
  height: 400px;
  background-color: white;
  gap: 5px;
}

.box {
  flex: 1;
  min-width: 100px;
  height: 100px;
  border: 5px solid black;
}

.red {
  background-color: red;
  flex: 2;
}

.blue {
  background-color: blue;
}

.yellow {
  background-color: yellow;
}

.white {
  background-color: white;
}

.black {
  background-color: black;
}
```

Ez a CSS kód egy egyszerűbb Mondrian-festményt hoz létre div elemekkel és flexbox elrendezéssel.

5. Gyakorlati Feladatok
   Feladat 1: Egyszerű weblap stílusozása
   Hozz létre egy HTML oldalt és adj hozzá egy külső CSS fájlt, amelyben megadod:
   • Az oldal háttérszínét
   • Egy h1 elem színét és betűméretét
   • Egy bekezdés igazítását és betűtípusát
   Feladat 2: Flexbox alapú elrendezés készítése
   Hozz létre egy rugalmasan igazodó elrendezést Flexbox segítségével, amely tartalmaz:
   • Egy fejléctartományt
   • Két oldalsávot
   • Egy fő tartalmi részt
   Ezek az alapok segítenek megérteni a CSS működését, és biztosítják a weblapok megfelelő vizuális megjelenését!
