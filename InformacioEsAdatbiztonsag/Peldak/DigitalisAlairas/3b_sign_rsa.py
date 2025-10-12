# sign_rsa.py – Digitális aláírás készítése, PEM fájlba mentéssel (RSA-PSS + SHA-256)
# Használat: python sign_rsa.py
# Létrejön: private_key.pem, public_key.pem, message.txt, signature.bin

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from pathlib import Path

# 1) RSA kulcspár generálása
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# 2) Üzenet (UTF-8), bytes-re konvertáljuk
msg_text = "Az utalas osszege: 10 000 Ft"  # tetszőlegesen írd át
msg = msg_text.encode("utf-8")
Path("message.txt").write_text(msg_text, encoding="utf-8")

# 3) Aláírás létrehozása (RSA-PSS + SHA-256)
signature = private_key.sign(
    msg,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH,
    ),
    hashes.SHA256(),
)

# 4) Kulcsok és aláírás mentése fájlba
Path("private_key.pem").write_bytes(
    private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,  # vagy PKCS8
        encryption_algorithm=serialization.NoEncryption(),      # jelszó nélküli
    )
)

Path("public_key.pem").write_bytes(
    public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
)

Path("signature.bin").write_bytes(signature)

print("✅ Aláírás és kulcsok elmentve: signature.bin, private_key.pem, public_key.pem, message.txt")
