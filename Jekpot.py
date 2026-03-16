import random
import time



simbol = ["🍒", "🔔", "7️⃣", "💎", "🍋", "⭐"]
saldo = 100

def putar_mesin():
    hasil = []
    
    if random.random() < 0.1:  
        simbol_jp = random.choice(simbol)
        hasil = [simbol_jp] * 3
        for s in hasil:
            time.sleep(0.5)
            print(s, end=" | ", flush=True)
        print()
        return hasil

    for i in range(3):
        time.sleep(0.5)
        simbol_acak = random.choice(simbol)
        hasil.append(simbol_acak)
        print(simbol_acak, end=" | ", flush=True)
    print()
    return hasil


def main():
    global saldo
    print("🎰 Selamat datang di Mesin Jackpot!\n")

    while saldo > 0:
        input("Tekan ENTER untuk memutar...")
        saldo -= 10
        print("Memutar...", end=" ", flush=True)
        print("🔄")

        hasil = putar_mesin()

        if hasil[0] == hasil[1] == hasil[2]:
            print("🎉 JACKPOT! Anda menang 60 koin!")
            saldo += 60
        else:
            print("Coba lagi!")

        print(f"Saldo: {saldo} koin\n")

    print("Saldo habis, Depolah.")

main()
