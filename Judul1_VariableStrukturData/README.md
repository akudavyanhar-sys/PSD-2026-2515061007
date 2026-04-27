
Judul Program: Program daftar tugas (to do list sederhana)

Deskripsi Singkat: 

Program daftar tugas tersebut berfungsi sebagai aplikasi sederhana untuk mengelola aktivitas harian secara dinamis dan terorganisir. Pengguna dapat menambahkan tugas satu per satu, lalu menentukan prioritasnya dengan menempatkan tugas di bagian depan (prioritas tinggi) atau di bagian belakang (prioritas biasa). Setelah daftar tersusun, tugas diselesaikan secara berurutan dari posisi terdepan, sehingga alurnya mencerminkan proses kerja yang sistematis. Program juga menyediakan fitur untuk menampilkan daftar tugas terkini agar pengguna dapat melihat urutan pekerjaan yang harus dilakukan dengan jelas.
Dari perspektif algoritma dan struktur data, program ini memanfaatkan Linked List sebagai media penyimpanan. Setiap tugas direpresentasikan sebagai node yang saling terhubung melalui pointer. Penambahan data dilakukan melalui dua metode, yaitu penyisipan di depan (insert at head) dan di belakang (insert at tail), yang keduanya efisien karena tidak memerlukan pergeseran elemen seperti pada array. Sementara itu, penghapusan hanya dilakukan dari bagian depan, sehingga mengikuti prinsip Queue (FIFO – First In, First Out), di mana tugas yang lebih dulu masuk akan diselesaikan lebih dahulu. Kombinasi pendekatan ini membuat sistem tetap fleksibel saat menambah tugas, namun tetap terarah dalam proses penyelesaiannya.


Source Code: 

<img width="1340" height="3674" alt="image" src="https://github.com/user-attachments/assets/e2b4ab6d-2aeb-422d-8790-f06e682c0cab" />

Gambaran Umum

Program ini merupakan aplikasi To-Do List sederhana yang dibangun menggunakan struktur data Linked List dalam bahasa Python. Secara umum, program terbagi menjadi dua komponen utama: definisi struktur data melalui class, dan bagian utama yang menangani interaksi dengan pengguna.

Class Node

Class Node berfungsi sebagai elemen dasar dalam linked list. Setiap node menyimpan dua atribut, yaitu self.task sebagai isi tugas dan self.next sebagai penunjuk ke node berikutnya. Saat node pertama kali dibuat, self.next bernilai None karena belum terhubung dengan node lain. Secara sederhana, node dapat dianalogikan seperti catatan berisi tugas yang memiliki penunjuk ke catatan berikutnya.

Class ToDoList

Class ToDoList bertugas mengelola keseluruhan struktur linked list. Pada saat inisialisasi (__init__), atribut self.head diatur ke None, menandakan bahwa daftar masih kosong. self.head menjadi titik awal untuk mengakses seluruh data dalam list.
Class ini menyediakan empat method utama. Pertama, add_front(), yang menambahkan tugas di bagian depan dengan menjadikan node baru sebagai head. Kedua, add_back(), yang menambahkan tugas di bagian belakang dengan menelusuri node hingga mencapai elemen terakhir sebelum menyambungkan node baru.
Ketiga, delete_front(), yang menghapus tugas dari bagian depan sesuai prinsip FIFO (First In, First Out). Jika list kosong, program akan memberikan peringatan; jika tidak, head akan dipindahkan ke node berikutnya sehingga node sebelumnya terhapus secara efektif.
Keempat, show_tasks(), yang menampilkan seluruh isi daftar. Untuk menjaga posisi head tetap, digunakan variabel sementara (temp) yang menelusuri node satu per satu hingga mencapai akhir list.

Program Utama

Alur utama program dibagi menjadi dua tahap. Tahap pertama adalah proses input tugas menggunakan perulangan while True. Pengguna memasukkan tugas, lalu menentukan apakah tugas tersebut ditempatkan di depan atau belakang. Proses ini berlangsung hingga pengguna mengetik "selesai", kemudian seluruh daftar ditampilkan.
Tahap kedua adalah proses penyelesaian tugas. Program kembali menggunakan perulangan dan menanyakan apakah pengguna ingin menyelesaikan tugas terdepan. Jika jawabannya "y", maka tugas dihapus menggunakan delete_front() dan daftar diperbarui. Jika "n", program dihentikan dengan pesan penutup.

Kesimpulan

Program ini mengimplementasikan linked list secara manual tanpa memanfaatkan struktur bawaan Python seperti list. Setiap tugas direpresentasikan sebagai node yang saling terhubung melalui pointer. Mekanisme penghapusan mengikuti prinsip FIFO, sehingga tugas yang pertama dimasukkan akan diselesaikan terlebih dahulu. Secara keseluruhan, program ini memberikan gambaran konkret tentang cara kerja linked list dalam konteks aplikasi sederhana.

Output Program: 

<img width="779" height="581" alt="Screenshot 2026-04-27 201326" src="https://github.com/user-attachments/assets/bd80fd4a-a515-491f-94cc-0602c22a692b" />
<img width="648" height="433" alt="Screenshot 2026-04-27 201156" src="https://github.com/user-attachments/assets/0ffc5fcd-5eee-4de1-a48e-efeee9cbf752" />

Link Youtube: Penjelasan kode melalui video presentasi
