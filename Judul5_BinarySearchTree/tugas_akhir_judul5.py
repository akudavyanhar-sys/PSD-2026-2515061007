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

    def find_successor(self, root, harga):
        successor = None
        while root:
            if harga < root.harga:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor

    def find_predecessor(self, root, harga):
        predecessor = None
        while root:
            if harga > root.harga:
                predecessor = root
                root = root.right
            else:
                root = root.left
        return predecessor

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
        elif pilih == "2":
            try:
                harga = int(input("Masukkan harga acuan: "))
            except ValueError:
                print("Input tidak valid!")
                continue
            successor = bst.find_successor(bst.root, harga)
            if successor:
                print("\nBarang dengan harga lebih besar terdekat:")
                print(f"Nama Barang : {successor.nama_barang}")
                print(f"Harga       : Rp{successor.harga}")
            else:
                print("Tidak ada harga yang lebih besar.")
        elif pilih == "3":
            try:
                harga = int(input("Masukkan harga acuan: "))
            except ValueError:
                print("Input tidak valid!")
                continue
            predecessor = bst.find_predecessor(bst.root, harga)
            if predecessor:
                print("\nBarang dengan harga lebih kecil terdekat:")
                print(f"Nama Barang : {predecessor.nama_barang}")
                print(f"Harga       : Rp{predecessor.harga}")
            else:
                print("Tidak ada harga yang lebih kecil.")
        elif pilih == "4":
            try:                
                cari = input("Masukkan nama barang yang ingin dicari: ")
            except ValueError:                
                print("Input tidak valid!")                
                continue
            hasil = bst.search(bst.root, cari)
            if hasil:
                print("\nBarang ditemukan")
                print(f"Nama Barang : {hasil.nama_barang}")
                print(f"Harga       : Rp{hasil.harga}")
            else:
                print("Barang tidak ditemukan!")
        elif pilih == "5":
            try:            
                if bst.root is None:
                    print("Tidak ada barang yang ditambahkan!")
                else:
                    print("\nDaftar Barang:")
                bst.inorder(bst.root)
            except ValueError:
                print("Input tidak valid!")
        elif pilih == "6":
            try:    
                hapus = input("Masukkan nama barang yang ingin dihapus: ")
                bst.root = bst.delete(bst.root, hapus)
                print("Barang berhasil dihapus!")
            except ValueError:
                print("Input tidak valid!")
                continue
        elif pilih == "7":
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")
        

if __name__ == "__main__":
    main()