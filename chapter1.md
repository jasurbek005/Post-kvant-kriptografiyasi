# 1-BOB. KLASSIK KRIPTOGRAFIK TIZIMLAR VA ULARNING KVANT TAHDIDLARI

## 1.1. Asimmetrik shifrlash algoritmlari (RSA va ECC) va ularning matematik asosi
Hozirgi kunda raqamli ma'lumotlarni uzatish va elektron raqamli imzolarni (ERI) tasdiqlash jarayonlarida asosan ikki turdagi asimmetrik kriptosistemalar keng qo'llaniladi:
1. **RSA (Rivest–Shamir–Adleman):** Xavfsizligi katta butun sonlarni tub ko'paytuvchilarga ajratish (Integer Factorization Problem) qiyinligiga asoslangan.
2. **ECC (Elliptic Curve Cryptography):** Xavfsizligi elliptik egri chiziqlar ustidagi diskret logarifm masalasiga (Elliptic Curve Discrete Logarithm Problem - ECDLP) tayanadi. 

ECC algoritmi RSA'ga nisbatan qisqaroq kalit uzunligida ham yuqori darajadagi xavfsizlikni ta'minlagani uchun zamonaviy tarmoqlarda (TLS/SSL, VPN, mobil ilovalar) ustunlik qiladi.

## 1.2. Kvant kompyuterlarining klassik kriptografiyaga tahdidi
Klassik kompyuterlar bitlar (0 va 1) ustida ketma-ket amallarni bajarsa, kvant kompyuterlari **qubitlar** yordamida superpozisiya va kvant ilashish (entanglement) qonuniyatlariga tayanib ishlaydi. Bu esa hisoblash tezligini eksponensial ravishda oshiradi.

Kvant kompyuterlarining amaliyotga joriy etilishi mavjud asimmetrik shifrlash tizimlari uchun halokatli xavf tug'diradi:
* **Shor algoritmi:** Kvant kompyuterida ishlovchi ushbu algoritm katta sonlarni tub ko'paytuvchilarga ajratish va diskret logarifmni hisoblash murakkabligini to'g'ridan-to'g'ri ko'pxadli vaqtga ($O((log N)^3)$) keltirib qo'yadi. Natijada, **RSA va ECC algoritmlari to'liq fosh bo'ladi** (buziladi).
* **Grover algoritmi:** Simmetrik shifrlash algoritmlari (masalan, **AES-128 / AES-256**) va xesh-funksiyalarga (SHA-256) ta'sir ko'rsatib, ularning kalit uzunligining samaradorligini ikki barobar kamaytiradi (masalan, AES-128 ning xavfsizligi AES-64 darajasiga tushib qoladi). Biroq, simmetrik shifrlashni kalit hajmini oshirish (AES-256 ga o'tish) orqali saqlab qolish mumkin.

## 1.3. Muammoning dolzarbligi va "Hozir yozib ol, keyin shifrini yech" (Harvest Now, Decrypt Later) hujumlari
Bugungi kunda tajovuzkorlar shifrlangan maxfiy davlat, moliyaviy va korporativ tarmoq trafigini saqlab qo'ymoqdalar. Ularning maqsadi — kelajakda kuchli kvant kompyuterlari yaratilganda, o'sha paytda yozib olingan eskirgan klassik shifrlangan ma'lumotlarni orqaga qarab o'qishdir. Shu sababli, infratuzilmani hozirdanoq post-kvant standartlariga o'tkazish dolzarb vazifa hisoblanadi.
