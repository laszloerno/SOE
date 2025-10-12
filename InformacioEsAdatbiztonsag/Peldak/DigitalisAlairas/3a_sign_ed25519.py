# sign_ed25519.py – Digitális aláírás Ed25519-zel (PEM mentéssel)
# Használat: python sign_ed25519.py
# Létrejön: ed25519_private.pem, ed25519_public.pem, message.txt, ed25519_signature.bin

from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
from pathlib import Path

# 1) Ed25519 kulcspár
private_key = ed25519.Ed25519PrivateKey.generate()
public_key = private_key.public_key()

# 2) Üzenet
msg_text = "Az utalas osszege: 10 000 Ft"  # tetszoleges szoveg
msg = msg_text.encode("utf-8")
Path("message.txt").write_text(msg_text, encoding="utf-8")

# 3) Aláírás (Ed25519: nincs padding konfiguracio)
signature = private_key.sign(msg)

# 4) Kulcsok és aláírás mentése
Path("ed25519_private.pem").write_bytes(
    private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,  # javasolt formátum
        encryption_algorithm=serialization.NoEncryption(),
    )
)

Path("ed25519_public.pem").write_bytes(
    public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
)

Path("ed25519_signature.bin").write_bytes(signature)

print("✅ Ed25519 aláírás és kulcsok elmentve: ed25519_signature.bin, ed25519_private.pem, ed25519_public.pem, message.txt")
