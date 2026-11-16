# Hybrid PQC Secure Tunnel & Key Exchange Protocol
> **Bitiruv Malakaviy Ishi (BMI) Amaliy Moduli**  
> **Yo'nalish:** Axborot xavfsizligi (4-kurs)  
> **Muallif:** Xasanov Jasurbek (O'zbekiston xalqaro islom akademiyasi)

---

## 📌 Loyihaning Maqsadi
Ushbu loyiha kvant kompyuterlarining kelajakdagi tahdidlariga qarshi turish uchun **Klassik (ECDH / AES)** va **NIST tomonidan tasdiqlangan Post-Kvant (PQC / Lattice-based)** kriptografik algoritmlarini birlashtiruvchi gibrid prototip arxitekturasini ishlab chiqish va sinovdan o'tkazishga bag'ishlangan.

## 🏛 Arxitektura va Ishlash Prinsipi
Loyiha quyidagi asosiy modullardan iborat:
1. **Gibrid Kalit Almashinuvi (`core/hybrid_exchange.py`):** Klassik va post-kvant entropiya manbalarini birlashtirib, xavfsiz sessiya kalitini hosil qiladi (HKDF yondashuvi).
2. **Shifrlash Moduli (`AES-256-GCM`):** Hosil qilingan kalit yordamida uzatilayotgan ma'lumotlarning maxfiyligi va butunligini (authenticity) ta'minlaydi.

## 📂 Repozitoriy Tuzilmasi
- `chapter1.md` — 1-Bob: Klassik kriptografik tizimlar va kvant tahdidlari
- `chapter2.md` — 2-Bob: Post-kvant kriptografiyasi va NIST standartlari
- `chapter3.md` — 3-Bob: Amaliy qism va gibrid simulyatsiya tahlili
- `hybrid_exchange.py` — Gibrid protokollarning asosiy dasturiy yadrosi
- `plan.md` — Ishning kalendar rejasi va mundarijasi

## 🚀 Ishga Tushirish (Quick Start)
Dasturni sinovdan o'tkazish uchun Python 3 va `cryptography` kutubxonasi talab qilinadi. Terminalda quyidagi buyruqni bajaring:

```bash
# Kerakli kutubxonani o'rnatish
pip install cryptography

# Gibrid protokoll yadrosini ishga tushirish
python3 hybrid_exchange.py
