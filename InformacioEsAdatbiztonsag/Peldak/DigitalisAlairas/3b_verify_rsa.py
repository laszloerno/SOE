# verify_rsa.py – Digitális aláírás ellenőrzése PEM kulcsból (RSA-PSS + SHA-256)
# Használat: python verify_rsa.py
# Bemenetek: public_key.pem, signature.bin, message.txt

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
from pathlib import Path

# 1) Fájlok beolvasása
msg = Path("message.txt").read_text(encoding="utf-8").encode("utf-8")
signature = Path("signature.bin").read_bytes()
public_pem = Path("public_key.pem").read_bytes()

# 2) Nyilvános kulcs betöltése
public_key = serialization.load_pem_public_key(public_pem)

# 3) Aláírás ellenőrzése (RSA-PSS + SHA-256)
try:
    public_key.verify(
        signature,
        msg,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )
    print("✅ Ellenőrzés: aláírás ÉRVÉNYES")
except InvalidSignature:
    print("❌ Ellenőrzés: aláírás ÉRVÉNYTELEN")
