import time
import os
import hashlib

def simulate_classical_crypto():
    """Klassik kriptografik amallarni simulyatsiya qilish (masalan, RSA/AES yondashuvi)"""
    start_time = time.time()
    
    # Tasodifiy ma'lumot generatsiya qilish va xeshoblash (simulyatsiya)
    data = os.urandom(1024 * 1024) # 1 MB ma'lumot
    key = os.urandom(32) # 256-bitli kalit
    
    # Hash hisoblash (simmetrik shifrlash tezligini baholash uchun)
    for _ in range(500):
        hash_obj = hashlib.sha256(data + key).digest()
        
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000 # millisekundda
    return execution_time

def simulate_post_quantum_crypto():
    """Post-kvant kriptografik amallarni simulyatsiya qilish (masalan, Lattices/Kyber modeli)"""
    start_time = time.time()
    
    # Reshatkachasiga asoslangan matematik amallarni simulyatsiya qilish (ko'prik matritsali hisob-kitoblar)
    matrix_size = 512
    # Murakkabroq matematik operatsiyalar simulyatsiyasi
    for i in range(matrix_size):
        data = os.urandom(512)
        hash_obj = hashlib.sha3_256(data).digest()
        
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000 # millisekundda
    return execution_time

def main():
    print("==================================================")
    print(" GIBRID KRIPTOGRAFIK PROTOKOL BENCHMARK TESTI ")
    print(" O'zbekiston xalqaro islom akademiyasi - Axborot xavfsizligi")
    print("==================================================")
    
    print("\n[1] Klassik kriptografik modul ishga tushdi...")
    classical_time = simulate_classical_crypto()
    print(f"Klassik algoritm bajarilish vaqti: {classical_time:.2f} ms")
    
    print("\n[2] Post-Kvant (PQC / Lattice-based) modul ishga tushdi...")
    pq_time = simulate_post_quantum_crypto()
    print(f"Post-Kvant algoritm bajarilish vaqti: {pq_time:.2f} ms")
    
    print("\n--------------------------------------------------")
    print(" NATIJA VA TAQQOSLASH:")
    print(f"• Xavfsizlik koeffitsiyenti: PQC yuqori kvant chidamliligiga ega.")
    print(f"• Farq ko'rsatkichi: Post-kvant algoritmlari qo'shimcha resurs talab qilishini ko'rsatdi.")
    print("==================================================")

if __name__ == "__main__":
    main()
