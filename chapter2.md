# 2-BOB. POST-KVANT KRIPTOGRAFIYASIGA O'TISH VA NIST STANDARTLARI

## 2.1. Post-kvant kriptografiyasining matematik asoslari (Lattice-based Cryptography)
Kvant kompyuterlari tahdidiga qarshi tura oladigan yangi avlod kriptosistemalari turli matematik murakkab masalalarga tayanadi. Bular jumlasiga quyidagilar kiradi:
* Reshatkachasiga asoslangan kriptografiya (Lattice-based cryptography)
* Kodga asoslangan kriptografiya (Code-based cryptography)
* Ko'phadli xesh-imzolar (Hash-based signatures)
* Ko'p o'zgaruvchili kvadrat tenglamalar (Multivariate cryptography)

Bular ichida eng istiqbolli va keng qo'llaniladigani **Reshatkachasiga asoslangan kriptografiya** bo'lib, uning xavfsizligi ko'p o'lchovli fazodagi eng qisqa vektorlarni qidirish (Shortest Vector Problem - SVP) va yaqin vektorlarni topish kabi qiyin matematik masalalarga asoslanadi. Bu masalalar nafaqat klassik, balki kvant kompyuterlari uchun ham hozircha yechib bo'lmaydigan darajada murakkab hisoblanadi.

## 2.2. NIST tomonidan tasdiqlangan Post-Kvant standartlari (FIPS 203 va FIPS 204)
AQShning Standartlar va texnologiyalar milliy instituti (NIST) ko'p yillik tanlovlardan so'ng kvantdan keyingi davr uchun rasmiy kriptografik standartlarni e'lon qildi:
1. **ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism), avvalgi nomi CRYSTALS-Kyber:** Umumiy kalitli shifrlash va kalit almashish protokollari uchun asosiy standart sifatida tanlandi (FIPS 203). U tarmoq ulanishlarida (masalan, TLS protokollarida) xavfsiz kalit almashinuvini ta'minlaydi.
2. **ML-DSA (Module-Lattice-Based Digital Signature Algorithm), avvalgi nomi CRYSTALS-Dilithium:** Raqamli imzolarni tasdiqlash va autentifikatsiya qilish uchun asosiy standart etib belgilandi (FIPS 204).

## 2.3. Klassik va Post-Kvant algoritmlarining qiyosiy xususiyatlari
Post-kvant algoritmlari kvant xavfsizligini ta'minlasa-da, ularning o'ziga xos muhandislik xususiyatlari mavjud:
* **Kalit hajmi:** Klassik RSA-2048 yoki ECC-256 kalitlariga nisbatan PQC (masalan, Kyber yoki Dilithium) kalitlari va imzolari sezilarli darajada kattaroq hajmni egallaydi. Bu tarmoq paketlari (packet size) hajmining oshishiga olib keladi.
* **Hisoblash unumdorligi:** Zamonaviy protsessorlarda bu algoritmlar yetarlicha tez ishlasa-da, cheklangan resursli qurilmalarda (IoT, quyi darajadagi mikrokontrollerlar) optimizatsiyani talab qiladi.
