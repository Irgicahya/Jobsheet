import random

class GameTebakAngka:
    def __init__(self):
        self.angka_tertentu = random.randint(1, 100)
        self.tebakan_terakhir = None

    def tebak(self, tebakan):
        self.tebakan_terakhir = tebakan

        if tebakan == self.angka_tertentu:
            return "Selamat! Anda menebak dengan benar."
        elif tebakan < self.angka_tertentu:
            return "Angka terlalu kecil. Coba lagi."
        else:
            return "Angka terlalu besar. Coba lagi."

if __name__ == "__main__":
    game = GameTebakAngka()

    while True:
        tebakan = int(input("Masukkan tebakan Anda (1-100): "))
        hasil_tebakan = game.tebak(tebakan)
        print(hasil_tebakan)

        if hasil_tebakan.startswith("Selamat"):
            break
