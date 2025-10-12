# rsa_minipelda.py – Oktatási célú RSA minipélda kis számokkal, lépésenkénti követéssel

from typing import List, Tuple

def egcd_trace(a: int, b: int):
    trace = []
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        trace.append((old_r, r, q, old_s, s, old_t, t))
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t, trace

def print_egcd_trace(a: int, b: int):
    g, x, y, tr = egcd_trace(a, b)
    print("Extended Euclid trace for a =", a, "b =", b)
    print("Columns: (old_r, r, q, old_s, s, old_t, t)")
    for row in tr:
        print(row)
    print(f"gcd({a},{b}) = {g}")
    print(f"Bezout: {a}*({x}) + {b}*({y}) = {g}")
    return g, x, y

def pow_trace(base: int, exp: int, mod: int):
    steps = []
    result = 1
    b = base % mod
    e = exp
    bitpos = 0
    while e > 0:
        bit = e & 1
        steps.append((bitpos, bit, result, b))
        if bit == 1:
            result = (result * b) % mod
        b = (b * b) % mod
        e >>= 1
        bitpos += 1
    return result, steps

def print_pow_trace(base: int, exp: int, mod: int, label=""):
    value, steps = pow_trace(base, exp, mod)
    print(f"\n{label} {base}^{exp} mod {mod} számolása square-and-multiply módszerrel:")
    print("Lépés | bit | eredmény előtte | bázis^2^k előtte")
    for k, bit, res_before, b_before in steps:
        print(f"{k:>5} |  {bit}  | {res_before:>16} | {b_before:>16}")
    print(f"→ Eredmény = {value}")
    return value

# Adott paraméterek
p, q = 11, 13
N = p * q
phi = (p - 1) * (q - 1)
e = 7

print("=== RSA Minipélda lépésenként ===")
print(f"p = {p}, q = {q}")
print(f"N = p * q = {N}")
print(f"φ(N) = (p - 1)(q - 1) = {phi}")
print(f"e = {e}  (gcd(e, φ(N)) = 1)")

# Privát kulcs számítása
g, x, y = print_egcd_trace(e, phi)
d = x % phi
print(f"Privát kitevő d = {d}  (mert {e}*{d} mod {phi} = {(e*d)%phi})")

# Hash-ből származó modellüzenet
m = 9
print(f"\nÜzenet reprezentáció (m) = {m}")

# Aláírás: σ = m^d mod N
sigma = print_pow_trace(m, d, N, label="Aláírás:")
print(f"Aláírás σ = {sigma}")

# Ellenőrzés: σ^e mod N =? m
m_vissza = print_pow_trace(sigma, e, N, label="Ellenőrzés:")
print(f"Visszafejtett m' = {m_vissza}")
print("\nEllenőrzés eredménye:", "✅ HELYES" if m_vissza == m else "❌ HIBÁS")
