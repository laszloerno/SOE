# verify_ed25519.py – Ed25519 aláírás ellenőrzése PEM-ből
# Használat: python verify_ed25519.py
# Bemenetek: ed25519_public.pem, ed25519_signature.bin, message.txt

from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature
from pathlib import Path

# 1) Fájlok beolvasása
msg = Path("message.txt").read_text(encoding="utf-8").encode("utf-8")
signature = Path("ed25519_signature.bin").read_bytes()
public_pem = Path("ed25519_public.pem").read_bytes()

# 2) Nyilvános kulcs betöltése
public_key = serialization.load_pem_public_key(public_pem)

# 3) Ellenőrzés
try:
    public_key.verify(signature, msg)
    print("✅ Ellenőrzés: Ed25519 aláírás ÉRVÉNYES")
except InvalidSignature:
    print("❌ Ellenőrzés: Ed25519 aláírás ÉRVÉNYTELEN")
