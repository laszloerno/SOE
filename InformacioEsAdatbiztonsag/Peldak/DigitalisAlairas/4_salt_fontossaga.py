#!/usr/bin/env python3
# compare_rsa_pseudopss.py
# Demonstráció: textbook RSA signature vs RSA-PSS
# Nem támadó kód — csak összehasonlítás és szemléltetés.

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.exceptions import InvalidSignature
import hashlib

def sha256_int(msg_bytes, N):
    # SHA-256 digest interpreted as big integer, reduced mod N
    h = hashlib.sha256(msg_bytes).digest()
    return int.from_bytes(h, "big") % N

def main():
    # 1) Kulcspár generálás (2048 bit; valódi alkalmazásnál is használható)
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Kinyerjük N, e, d számokat a demonstrációhoz (textbook használathoz)
    priv_numbers = private_key.private_numbers()
    pub_numbers = private_key.public_key().public_numbers()
    N = pub_numbers.n
    e = pub_numbers.e
    d = priv_numbers.d

    print("RSA modulus N bits:", N.bit_length())
    print("Public exponent e:", e)
    print()

    # 2) Üzenet (bytes)
    message = b"Az utalas osszege: 10 000 Ft"

    # 3) Hash→int (mod N) — ez lesz az m a textbook modellben
    m_int = sha256_int(message, N)
    print("SHA-256(message) as integer mod N (m):", m_int)
    print()

    # -------------------------
    # Textbook signature (modell)
    # -------------------------
    # sigma_textbook = m_int^d mod N
    sigma_textbook = pow(m_int, d, N)
    print("Textbook signature (integer):", sigma_textbook)

    # Verifikáció textbook módra: sigma^e mod N == m_int ?
    recovered_m = pow(sigma_textbook, e, N)
    print("Textbook verify: recovered m == m_int ?", recovered_m == m_int)
    print()

    # Ha újra aláírunk ugyanazzal a módszerrel, ugyanazt kapjuk (deterministic)
    sigma_textbook_again = pow(m_int, d, N)
    print("Textbook signature repeated == same ?", sigma_textbook == sigma_textbook_again)
    print()

    # -------------------------
    # RSA-PSS signature (ajánlott)
    # -------------------------
    # Aláírás PSS-sel (cryptography könyvtár)
    signature_pss_1 = private_key.sign(
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    signature_pss_2 = private_key.sign(
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

    print("PSS signature 1 length (bytes):", len(signature_pss_1))
    print("PSS signature 2 length (bytes):", len(signature_pss_2))
    print("PSS sig1 == sig2 ? (should be False, PSS is randomized):", signature_pss_1 == signature_pss_2)
    print()

    # PSS verification (standard library)
    try:
        public_key.verify(
            signature_pss_1,
            message,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        print("PSS verify sig1: VALID")
    except InvalidSignature:
        print("PSS verify sig1: INVALID")

    # PSS verification (standard library)
    try:
        public_key.verify(
            signature_pss_2,
            message,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        print("PSS verify sig2: VALID")
    except InvalidSignature:
        print("PSS verify sig2: INVALID")

    # -------------------------
    # Tampering test (mindkét aláírásra)
    # -------------------------
    tampered = b"Az utalas osszege: 10 001 Ft"
    print("\n=== Tamper test (modify message) ===")
    # Textbook verify on tampered message
    m_tampered_int = sha256_int(tampered, N)
    recovered_from_textbook = pow(sigma_textbook, e, N)
    print("Textbook: recovered m (from original sig) == m_tampered ?", recovered_from_textbook == m_tampered_int)

    # PSS verify on tampered message
    try:
        public_key.verify(
            signature_pss_2,
            tampered,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        print("PSS verify on tampered: VALID (unexpected!)")
    except InvalidSignature:
        print("PSS verify on tampered: INVALID (expected)")

    # -------------------------
    # Note: cryptographic warnings
    # -------------------------
    print("\nNOTE:")
    print("- 'Textbook' RSA signatures (raw m^d mod N) are NOT recommended in practice.")
    print("- Use RSA-PSS for signatures, and OAEP for RSA encryption.")
    print("- Textbook signatures are deterministic; PSS adds randomness (salt), protecting against several attacks.")

if __name__ == "__main__":
    main()
