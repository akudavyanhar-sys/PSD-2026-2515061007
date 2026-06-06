class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Nama: {self.name}, Nomor: {self.phone}"


class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, name, phone):
        index = self.hash_function(name)

        for i in range(self.size):
            probe = (index + i) % self.size

            if self.table[probe] is None:
                self.table[probe] = Contact(name, phone)
                print("Kontak berhasil ditambahkan.")
                return

            elif self.table[probe].name == name:
                print("Nama sudah digunakan")
                return

        print("Hash Table penuh!")

    def search(self, name):
        index = self.hash_function(name)

        for i in range(self.size):
            probe = (index + i) % self.size

            if self.table[probe] is None:
                return None

            if self.table[probe].name == name:
                return self.table[probe]

        return None

    def delete(self, name):
        index = self.hash_function(name)

        for i in range(self.size):
            probe = (index + i) % self.size

            if self.table[probe] is None:
                print("Kontak tidak ditemukan.")
                return

            if self.table[probe].name == name:
                self.table[probe] = None
                print("Kontak berhasil dihapus.")
                return

        print("Kontak tidak ditemukan.")

    def display(self):
        print("\nDaftar Kontak:")

        for i in range(self.size):
            print(f"Index {i}: ", end="")

            if self.table[i] is None:
                print("Kosong")
            else:
                print(self.table[i])


# Program Utama
hash_map = HashMap(10)

while True:
    print("\nMenu:")
    print("1. Tambah Kontak")
    print("2. Cari Kontak")
    print("3. Hapus Kontak")
    print("4. Tampilkan Semua Kontak")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama: ")
        nomor = input("Masukkan nomor telepon: ")
        hash_map.insert(nama, nomor)

    elif pilihan == "2":
        nama = input("Masukkan nama yang dicari: ")
        hasil = hash_map.search(nama)

        if hasil:
            print(hasil)
        else:
            print("Kontak tidak ditemukan.")

    elif pilihan == "3":
        nama = input("Masukkan nama yang akan dihapus: ")
        hash_map.delete(nama)

    elif pilihan == "4":
        hash_map.display()

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")