# Node
class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

# Linked List
class ToDoList:
    def __init__(self):
        self.head = None

    def add_front(self, task):
        new_node = Node(task)
        new_node.next = self.head
        self.head = new_node

    def add_back(self, task):
        new_node = Node(task)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_front(self):
        if not self.head:
            print("Tidak ada tugas lagi!")
            return
        
        print(f"Tugas '{self.head.task}' selesai dan dihapus.")
        self.head = self.head.next

    def show_tasks(self):
        temp = self.head
        if not temp:
            print("Daftar tugas kosong.")
            return
        
        print("\nDaftar Tugas:")
        while temp:
            print("- " + temp.task)
            temp = temp.next


# Program Utama
todo = ToDoList()

print("Input Tugas Anda (ketik 'selesai' untuk berhenti):")

# Tahap 1: Input tugas
while True:
    task = input("Masukkan tugas (atau ketik 'selesai'): ")
    
    if task.lower() == "selesai":
        break

    print("Pilih posisi:")
    print("1. Tambah di Depan")
    print("2. Tambah di Belakang")
    posisi = input("Pilihan (1/2): ")

    if posisi == "1":
        todo.add_front(task)
    elif posisi == "2":
        todo.add_back(task)
    else:
        print("Pilihan tidak valid, otomatis ditaruh di belakang.")
        todo.add_back(task)

# Tampilkan hasil input
todo.show_tasks()

# Tahap 2: Hapus tugas 
print("\nSelesaikan tugas satu per satu")

while True:
    lanjut = input("Selesaikan tugas terdepan? (y/n): ")

    if lanjut.lower() == "y":
        todo.delete_front()
        todo.show_tasks()
    elif lanjut.lower() == "n":
        print("Selesai.")
        break
    else:
        print("Input tidak valid!")