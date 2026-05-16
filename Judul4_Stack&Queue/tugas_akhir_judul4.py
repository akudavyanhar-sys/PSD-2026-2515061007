from collections import deque

antrian = deque()

nomor_antrian = 1

while True:
    print("\nSistem Antrian Pembeli Obat")
    print("1. Tambah Antrian Pembeli")
    print("2. Panggil Pembeli")
    print("3. Lihat Antrian")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama pembeli : ")

        data_pembeli = {
            "nomor": nomor_antrian,
            "nama": nama
        }

        antrian.append(data_pembeli)

        print(
            f"Pembeli {nama} berhasil masuk antrian "
            f"dengan nomor {nomor_antrian}."
        )

        nomor_antrian += 1

    elif pilihan == "2":
        if len(antrian) == 0:
            print("Antrian kosong.")
        else:
            pembeli = antrian.popleft()

            print("\nPembeli yang dipanggil:")
            print(f"Nomor Antrian : {pembeli['nomor']}")
            print(f"Nama Pembeli  : {pembeli['nama']}")

    elif pilihan == "3":
        if len(antrian) == 0:
            print("Antrian masih kosong.")
        else:
            print("\nDaftar Antrian Pembeli:")

            urutan = 1

            for pembeli in antrian:
                print(
                    f"{urutan}. "
                    f"Nomor: {pembeli['nomor']} | "
                    f"Nama: {pembeli['nama']}"
                )

                urutan += 1

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")