# tugas 1
kendaraan = ["honda", "motor", "150", "hitam", "roda dua"]
print(kendaraan)  # Menghapus tanda "=" yang tidak perlu

kendaraan.append("300000")  # Menambahkan elemen "300000" ke dalam list kendaraan
kendaraan.append("matic")   # Menambahkan elemen "matic" ke dalam list kendaraan
print(kendaraan)  # Mencetak list kendaraan

kendaraan.insert(1, "pcx")  # Menyisipkan elemen "pcx" ke dalam indeks ke-1 (setelah "honda")
print(kendaraan)  # Mencetak list kendaraan setelah sisipan

# tugas 2
def hitung_luas_persegi(sisi):
    return sisi * sisi

def hitung_luas_lingkaran(jari_jari):
    import math
    return math.pi * (jari_jari ** 2)

def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def main():
    print("selamat datang di python luas bangun datar gw")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Segitiga")

    pilihan = input("Pilih bangun datar (1/2/3): ")

    match pilihan:
        case "1":
            sisi = float(input("Masukkan panjang sisi persegi: "))
            luas = hitung_luas_persegi(sisi)
        case "2":
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            luas = hitung_luas_lingkaran(jari_jari)
        case "3":
            alas = float(input("Masukkan panjang alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            luas = hitung_luas_segitiga(alas, tinggi)
        case _:
            print("Pilihan tidak valid!")
            return

    print(f"Luas bangun datar adalah: {luas}")

if __name__ == "__main__":
    main()
