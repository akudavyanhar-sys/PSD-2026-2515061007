def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            # Urutkan berdasarkan total nilai (descending)
            if arr[j]["total"] < arr[j + 1]["total"]:
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Masukkan jumlah siswa: "))
    except ValueError:
        print("Input tidak valid!")
        return

    siswa = []

    print("\nMasukkan data siswa:")
    for i in range(n):
        print(f"\nData siswa ke-{i+1}")
        nama = input("Nama: ")

        total = 0
        for semester in range(1, 6):
            while True:
                try:
                    nilai = float(input(f"Nilai Semester {semester}: "))
                    total += nilai
                    break
                except ValueError:
                    print("Input tidak valid, masukkan angka!")

        siswa.append({
            "nama": nama,
            "total": total
        })

    print("\nData sebelum diurutkan:")
    for s in siswa:
        print(f"{s['nama']} - {s['total']}")

    bubble_sort(siswa, n)

    print(f"\nHasil dari pengurutan {n} siswa:")
    for i in range(n):
        print(f"Ranking {i+1}")
        print(f"Nama  : {siswa[i]['nama']}")
        print(f"Total : {siswa[i]['total']}")
        print("-" * 30)


if __name__ == "__main__":
    main()