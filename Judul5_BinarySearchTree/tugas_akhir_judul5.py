class Node:
    def __init__(self, nama_barang, harga):
        self.nama_barang = nama_barang
        self.harga = harga
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, nama_barang, harga):
        if root is None:
            return Node(nama_barang, harga)

        if nama_barang.lower() < root.nama_barang.lower():
            root.left = self.insert(root.left, nama_barang, harga)

        elif nama_barang.lower() > root.nama_barang.lower():
            root.right = self.insert(root.right, nama_barang, harga)

        else:
            print("Barang sudah ada!")

        return root

    def search(self, root, nama_barang):
        if root is None:
            return None

        if nama_barang.lower() == root.nama_barang.lower():
            return root

        if nama_barang.lower() < root.nama_barang.lower():
            return self.search(root.left, nama_barang)

        return self.search(root.right, nama_barang)

    def inorder(self, root):
        if root:
            self.inorder(root.left)

            print(f"Nama Barang : {root.nama_barang}")
            print(f"Harga       : Rp{root.harga}")
            print("-" * 30)

            self.inorder(root.right)

    def min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def delete(self, root, nama_barang):
        if root is None:
            return root

        if nama_barang.lower() < root.nama_barang.lower():
            root.left = self.delete(root.left, nama_barang)

        elif nama_barang.lower() > root.nama_barang.lower():
            root.right = self.delete(root.right, nama_barang)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.min_value_node(root.right)

            root.nama_barang = temp.nama_barang
            root.harga = temp.harga

            root.right = self.delete(root.right, temp.nama_barang)

        return root

    def get_all_items(self, root, items):
        if root:
            self.get_all_items(root.left, items)
            items.append(root)
            self.get_all_items(root.right, items)

    def find_successor(self, harga):
        items = []
        self.get_all_items(self.root, items)

        lebih_besar = [item for item in items if item.harga > harga]

        if not lebih_besar:
            return None

        return min(lebih_besar, key=lambda x: x.harga)

    def find_predecessor(self, harga):
        items = []
        self.get_all_items(self.root, items)

        lebih_kecil = [item for item in items if item.harga < harga]

        if not lebih_kecil:
            return None

        return max(lebih_kecil, key=lambda x: x.harga)


def main():
    bst = BinarySearchTree()
    pilih = 0

    while pilih != 7:

        print("\nSistem Informasi Barang")
        print("1. Tambah Barang")
        print("2. Cari Harga Lebih Besar")
        print("3. Cari Harga Lebih Kecil")
        print("4. Cari Barang")
        print("5. Tampilkan Semua Barang")
        print("6. Hapus Barang")
        print("7. Keluar")

        try:
            pilih = int(input("Pilih menu: "))

        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                nama = input("Masukkan nama barang: ")
                harga = int(input("Masukkan harga barang: "))

                bst.root = bst.insert(bst.root, nama, harga)

                print("Barang berhasil ditambahkan!")

            except ValueError:
                print("Input harga tidak valid!")

        elif pilih == 2:
            try:
                harga = int(input("Masukkan harga acuan: "))

            except ValueError:
                print("Input tidak valid!")
                continue

            successor = bst.find_successor(harga)

            if successor:
                print("\nBarang dengan harga lebih besar terdekat:")
                print(f"Nama Barang : {successor.nama_barang}")
                print(f"Harga       : Rp{successor.harga}")

            else:
                print("Tidak ada harga yang lebih besar.")

        elif pilih == 3:
            try:
                harga = int(input("Masukkan harga acuan: "))

            except ValueError:
                print("Input tidak valid!")
                continue

            predecessor = bst.find_predecessor(harga)

            if predecessor:
                print("\nBarang dengan harga lebih kecil terdekat:")
                print(f"Nama Barang : {predecessor.nama_barang}")
                print(f"Harga       : Rp{predecessor.harga}")

            else:
                print("Tidak ada harga yang lebih kecil.")

        elif pilih == 4:
            cari = input("Masukkan nama barang yang ingin dicari: ")

            hasil = bst.search(bst.root, cari)

            if hasil:
                print("\nBarang ditemukan")
                print(f"Nama Barang : {hasil.nama_barang}")
                print(f"Harga       : Rp{hasil.harga}")

            else:
                print("Barang tidak ditemukan!")

        elif pilih == 5:
            if bst.root is None:
                print("Tidak ada barang yang ditambahkan!")

            else:
                print("\nDaftar Barang:")
                bst.inorder(bst.root)

        elif pilih == 6:
            hapus = input("Masukkan nama barang yang ingin dihapus: ")

            if bst.search(bst.root, hapus):
                bst.root = bst.delete(bst.root, hapus)
                print("Barang berhasil dihapus!")

            else:
                print("Barang tidak ditemukan!")

        elif pilih == 7:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()