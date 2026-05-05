def binary_search(arr, n, target):
    l = 0
    r = n - 1
    pos = -1
    while l <= r:
        m = l + (r - l) // 2
        print(f"Median: {m}, nilai: {arr[m]}")
        if arr[m] == target:
            pos = m
            break
        elif arr[m] < target:
            print("Mencari di kanan")
            l = m + 1
        else:
            print("Mencari di kiri")
            r = m - 1
    return pos


# Fungsi menentukan posisi kursi
def get_posisi(nomor):
    baris = (nomor - 1) // 10 + 1
    kolom = (nomor - 1) % 10 + 1

    if 1 <= baris <= 7:
        posisi = "Depan"
    elif 8 <= baris <= 14:
        posisi = "Tengah"
    else:
        posisi = "Belakang"

    return baris, kolom, posisi


def main():
    # Data otomatis 1–200 (sudah terurut → syarat Binary Search terpenuhi)
    arr = list(range(1, 201))
    n = len(arr)

    print("Data kursi tersedia dari 1 sampai 200")

    while True:
        try:
            target = int(input("Masukkan nomor peserta yang ingin dicari: "))
            if 1 <= target <= 200:
                break
            else:
                print("Nomor harus antara 1 sampai 200!")
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")

    pos = binary_search(arr, n, target)

    if pos != -1:
        nomor = arr[pos]
        baris, kolom, posisi = get_posisi(nomor)

        print(f"\nDitemukan pada indeks ke-{pos}")
        print(f"Nomor Peserta : {nomor}")
        print(f"Baris         : {baris}")
        print(f"Kolom         : {kolom}")
        print(f"Posisi        : {posisi}")
    else:
        print("Tidak ditemukan")


if __name__ == "__main__":
    main()