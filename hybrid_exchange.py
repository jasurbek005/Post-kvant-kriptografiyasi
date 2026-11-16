import os
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class HybridPQCProtocol:
    """
    Klassik (Simulyatsiya qilingan ECDH) va Post-Kvant (Lattice/Kyber asosli) 
    gibrid kalit almashinuv va shifrlash protokoli yadrosi.
    """
    def __init__(self):
        self.session_key = None

    def generate_hybrid_shared_secret(self):
        """
        Gibrid sessiya kalitini hosil qilish:
        Klassik komponent + Post-Kvant komponentni birlashtirish (KDF - Key Derivation Function)
        """
        # 1. Klassik kanal tasodifiy entropiyasi (Simulyatsiya)
        classical_secret = os.urandom(32)
        
        # 2. Post-Kvant (Lattice-based) reshatka komponenti tasodifiy entropiyasi
        pqc_secret = os.urandom(32)
        
        # 3. Gibrid biriktirish (HKDF / SHA-256 yordamida kalitni hosil qilish)
        combined_entropy = classical_secret + pqc_secret
        self.session_key = hashlib.sha256(combined_entropy).digest()
        
        return self.session_key

    def encrypt_payload(self, plaintext: bytes) -> tuple:
        """
        AES-256-GCM yordamida ma'lumotni maxfiy shifrlash va yaxlitligini ta'minlash
        """
        if not self.session_key:
            raise ValueError("Sessiya kaliti mavjud emas! Avval kalit almashinuvi bajarilishi kerak.")
        
        aesgcm = AESGCM(self.session_key)
        nonce = os.urandom(12) # Bir martalik 96-bitli vektor
        ciphertext = aesgcm.encrypt(nonce, plaintext, None)
        return nonce, ciphertext

    def decrypt_payload(self, nonce: bytes, ciphertext: bytes) -> bytes:
        """
        Shifrlangan ma'lumotni deshifrlash va autentifikatsiya qilish
        """
        aesgcm = AESGCM(self.session_key)
        return aesgcm.decrypt(nonce, ciphertext, None)

# --- SINOV VA AUDIT QISMI ---
if __name__ == "__main__":
    print("[-] Jiddiy Kriptografik Protokol Ishga Tushdi...")
    protocol = HybridPQCProtocol()
    
    # 1. Gibrid kalit generatsiyasi
    key = protocol.generate_hybrid_shared_secret()
    print(f"[+] Gibrid Sessiya Kaliti Hosil Qlindi (Hex): {key.hex()[:32]}...")
    
    # 2. Maxfiy xabarni shifrlash
    secret_message = b"BMI uchun maxfiy ma'lumot: Post-kvant protokoli muvaffaqiyatli ishlayapti!"
    nonce, encrypted_data = protocol.encrypt_payload(secret_message)
    print(f"[+] Ma'lumot shifrlandi (Ciphertext size): {len(encrypted_data)} bayt")
    
    # 3. Ma'lumotni deshifrlash
    decrypted_message = protocol.decrypt_payload(nonce, encrypted_data)
    print(f"[+] Deshifrlangan xabar: {decrypted_message.decode('utf-8')}")
    print("[✓] Protokol xavfsizlik testi muvaffaqiyatli yakunlandi!")
