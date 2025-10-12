from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

# 1) Kulcspár
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# 2) Üzenet (lehet str vagy bytes; itt str-ből bytes lesz)
message = "Az utalás összege: 10 000 Ft"
if isinstance(message, str):
    message = message.encode("utf-8")  # <-- FONTOS!

# ------------ Változat A: RSA-PSS (ajánlott) ------------
signature_pss = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH,
    ),
    hashes.SHA256(),
)

# Ellenőrzés
public_key.verify(
    signature_pss,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH,
    ),
    hashes.SHA256(),
)

print("RSA-PSS aláírás érvényes ✅")

# ------------ Változat B: PKCS#1 v1.5 (kompatibilitás) ------------
signature_pkcs1 = private_key.sign(
    message,
    padding.PKCS1v15(),
    hashes.SHA256(),
)

public_key.verify(
    signature_pkcs1,
    message,
    padding.PKCS1v15(),
    hashes.SHA256(),
)

print("PKCS#1 v1.5 aláírás érvényes ✅")

# ---- Tamper teszt ----
try:
    public_key.verify(
        signature_pss,
        "Az utalás összege: 10 000 Ft".encode("utf-8"),  # módosított üzenet
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256(),
    )
    print("HOPP: érvényes lett a módosított üzenet ❌")
except Exception:
    print("Módosított üzenet: aláírás ÉRVÉNYTELEN — helyes viselkedés ✅")
