# Mesin Jackpot Python (Terminal Game)

Program ini adalah game mesin jackpot sederhana berbasis terminal yang dibuat menggunakan bahasa Python.  
Pemain memutar mesin slot, mempertaruhkan koin, dan berpeluang mendapatkan JACKPOT jika tiga simbol yang muncul sama.

---
## cara menginstall

clone repository
```bash
git clone https://github.com/MIKAgata/JEKPOT.git

```
cek apakah python sudah terinstal jika belum install dari python.org
```bash
python --version
```



---

---

## Fitur Utama
- Tampilan emoji slot machine 🍒 🔔 7️⃣ 💎 🍋 ⭐
- Sistem saldo (koin)
- Animasi sederhana menggunakan time.sleep()
- Peluang jackpot khusus (10%)
- Logika acak menggunakan modul random
- Berjalan langsung di terminal / command prompt

---

## Cara Kerja Program
1. Pemain memulai dengan saldo 100 koin
2. Setiap putaran:
   - Biaya: 10 koin
   - Mesin akan memutar 3 simbol secara acak
3. Jika ketiga simbol sama:
   - Pemain mendapatkan +60 koin
4. Jika saldo habis:
   - Game otomatis berhenti

---

## Aturan Jackpot
Program memiliki peluang 10% untuk memaksa jackpot.  
Saat jackpot:
- Satu simbol dipilih secara acak
- Ditampilkan 3 kali berturut-turut
- Pemain dijamin menang

Contoh logika jackpot:
```python
if random.random() < 0.1:
    simbol_jp = random.choice(simbol)
    hasil = [simbol_jp] * 3
