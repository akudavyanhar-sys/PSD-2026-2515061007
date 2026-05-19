Judul Program: Program antrean pengambbilan obat

Deskripsi Singkat:

Program antrian pengambilan obat ini dikembangkan menggunakan struktur data Queue dengan konsep FIFO (First In, First Out), yaitu pembeli yang datang lebih awal akan dilayani terlebih dahulu. Konsep ini membuat proses antrean berjalan secara teratur dan sesuai urutan kedatangan.

Program dirancang untuk membantu pengelolaan antrean pembeli obat secara otomatis. Pengguna dapat menambahkan pembeli ke dalam antrean, memanggil antrean berikutnya, melihat daftar antrean yang sedang menunggu, serta keluar dari program melalui menu yang tersedia. Setiap pembeli yang masuk akan memperoleh nomor antrean secara otomatis, sehingga pengguna tidak perlu memasukkan nomor secara manual.

Penyimpanan data antrean memanfaatkan deque dari Python yang mendukung proses penambahan dan penghapusan data secara efisien. Operasi append() digunakan untuk menambahkan pembeli ke bagian belakang antrean, sedangkan popleft() digunakan untuk memanggil pembeli yang berada di posisi paling depan.

Secara keseluruhan, program ini menerapkan prinsip dasar struktur data Queue yang banyak digunakan dalam sistem pelayanan sehari-hari, seperti antrean di apotek, bank, rumah sakit, maupun kasir.

Source Code:

<img width="1172" height="2762" alt="image" src="https://github.com/user-attachments/assets/767734e4-115e-4152-bbc4-b6ae29526348" />

Gambaran Umum

Program ini merupakan aplikasi sistem antrean pembeli obat yang memanfaatkan struktur data Deque (Double Ended Queue) dari modul bawaan Python, yaitu collections. Program berjalan secara interaktif melalui menu pilihan dan menerapkan konsep FIFO (First In, First Out), sehingga pembeli yang lebih dahulu masuk antrean akan dipanggil lebih dulu.

Inisialisasi Awal

Sebelum masuk ke menu utama, program melakukan beberapa tahap persiapan. Pertama, deque diimpor dari library collections untuk digunakan sebagai struktur data antrean. Setelah itu, dibuat objek antrian yang masih kosong sebagai tempat penyimpanan data pembeli. Program juga menginisialisasi variabel nomor_antrian dengan nilai awal 1, yang nantinya digunakan untuk memberikan nomor antrean secara otomatis kepada setiap pembeli baru.

Menu Utama

Program dijalankan dalam perulangan while True, sehingga menu akan terus ditampilkan sampai pengguna memilih keluar. Pada setiap iterasi, sistem menampilkan empat pilihan utama, yaitu menambah antrean, memanggil pembeli, melihat daftar antrean, dan keluar dari program. Setelah itu, program menunggu input pilihan dari pengguna.

Menu 1 — Tambah Antrean Pembeli

Saat pengguna memilih menu pertama, program meminta nama pembeli melalui input. Nama tersebut kemudian digabungkan dengan nomor antrean saat ini ke dalam sebuah dictionary bernama data_pembeli. Data tersebut dimasukkan ke dalam deque menggunakan method append(), yaitu proses penambahan data di bagian belakang antrean sesuai prinsip FIFO.

Setelah data berhasil disimpan, program menampilkan konfirmasi berupa nama pembeli dan nomor antreannya. Selanjutnya, variabel nomor_antrian akan bertambah satu secara otomatis untuk mempersiapkan nomor antrean berikutnya.

Menu 2 — Panggil Pembeli

Pada menu ini, program terlebih dahulu memeriksa apakah antrean masih kosong menggunakan kondisi len(antrian) == 0. Jika antrean kosong, sistem akan menampilkan pesan peringatan.

Sebaliknya, jika masih terdapat data dalam antrean, program menggunakan method popleft() untuk mengambil sekaligus menghapus data pembeli yang berada di posisi paling depan. Informasi pembeli yang dipanggil, seperti nomor antrean dan nama, kemudian ditampilkan ke layar.

Menu 3 — Lihat Antrean

Ketika pengguna memilih menu ketiga, program kembali melakukan pengecekan terhadap kondisi antrean. Jika antrean kosong, sistem akan menampilkan pesan bahwa belum ada data antrean.

Namun, jika antrean berisi data, program akan menampilkan seluruh daftar pembeli menggunakan perulangan for. Setiap data ditampilkan lengkap dengan posisi antrean saat ini, nomor antrean resmi, dan nama pembeli. Untuk menjaga urutan tetap akurat, variabel urutan akan bertambah pada setiap iterasi.

Menu 4 — Keluar

Jika pengguna memilih menu keluar, program akan menampilkan pesan penutup, kemudian menjalankan perintah break untuk menghentikan perulangan while True. Setelah itu, program selesai dijalankan sepenuhnya.

Penanganan Input Tidak Valid

Program juga dilengkapi mekanisme penanganan input yang tidak sesuai. Jika pengguna memasukkan pilihan selain 1, 2, 3, atau 4, sistem akan masuk ke blok else dan menampilkan pesan bahwa pilihan tidak valid. Setelah itu, program kembali ke menu utama tanpa menghentikan proses yang sedang berjalan.

Kesimpulan

Secara keseluruhan, program ini mengimplementasikan struktur data deque sebagai mekanisme antrean berbasis FIFO. Penggunaan method append() untuk menambahkan data di bagian belakang dan popleft() untuk mengambil data dari bagian depan menjadi inti utama sistem antrean tersebut. Selain itu, adanya penomoran otomatis dan validasi kondisi antrean membuat program berjalan lebih teratur, aman, dan mudah digunakan.

Output Program:

<img width="626" height="921" alt="Screenshot 2026-05-16 201843" src="https://github.com/user-attachments/assets/2578d12d-40df-4b22-880e-79dca5158f80" />

<img width="353" height="782" alt="Screenshot 2026-05-16 201853" src="https://github.com/user-attachments/assets/5c5519fc-6c6c-440d-aba4-c5b1721fa621" />

Link Youtube: (https://youtu.be/xYBLr4g8VEM)




