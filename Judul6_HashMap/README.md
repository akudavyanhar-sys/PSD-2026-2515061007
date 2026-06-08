Judul Program: Program pencari nomor telepon

Deskripsi singkat:

Program ini merupakan sistem manajemen nomor telepon yang dikembangkan untuk menyimpan dan mengelola data kontak dengan memanfaatkan struktur data Hash Map. Dalam implementasinya, nama kontak berfungsi sebagai key, sedangkan nomor telepon disimpan sebagai value. Pendekatan ini memungkinkan data diakses secara cepat berdasarkan nama kontak yang dicari.

Untuk menangani kemungkinan terjadinya collision pada proses hashing, program menerapkan metode Open Addressing dengan teknik Linear Probing. Ketika slot yang dituju sudah terisi, sistem akan melakukan pencarian secara berurutan ke slot berikutnya hingga menemukan lokasi kosong yang dapat digunakan untuk menyimpan data baru.

Program ini menyediakan beberapa fitur utama, antara lain menambahkan kontak baru, mencari kontak berdasarkan nama, menghapus kontak yang tersimpan, serta menampilkan seluruh daftar kontak yang ada dalam sistem. Dengan memanfaatkan struktur data Hash Map, proses pencarian, penyimpanan, dan pengelolaan data dapat dilakukan lebih efisien dibandingkan metode pencarian linear yang memeriksa data satu per satu.

Source Code:

<img width="1200" height="4738" alt="image" src="https://github.com/user-attachments/assets/f78b1521-8dcd-4d07-9b4b-eb5281596486" />

Gambaran Umum:

Class Contact

Class Contact berfungsi sebagai cetak biru (blueprint) untuk merepresentasikan satu data kontak. Setiap objek yang dibuat dari class ini memiliki dua atribut utama, yaitu name untuk menyimpan nama kontak dan phone untuk menyimpan nomor telepon. Kedua atribut tersebut diinisialisasi melalui konstruktor __init__ saat objek dibuat.

Selain itu, class ini menyediakan method __str__, yang akan dipanggil secara otomatis ketika objek ditampilkan menggunakan fungsi print(). Method ini menghasilkan representasi teks yang lebih mudah dibaca, misalnya dalam format "Nama: Budi, Nomor: 08123456789", sehingga informasi kontak dapat ditampilkan secara langsung tanpa perlu mengakses atribut satu per satu.

Class HashMap: Konstruktor dan hash_function

Class HashMap merupakan komponen utama yang bertugas menyimpan seluruh data kontak. Konstruktor class ini menerima parameter size dengan nilai bawaan (default) sebesar 10, yang digunakan untuk menentukan kapasitas tabel hash. Selanjutnya, dibuat atribut self.table berupa list yang berisi nilai None sebanyak jumlah slot yang ditentukan.

Method hash_function digunakan untuk mengubah nama kontak yang berupa string menjadi indeks numerik. Proses ini dilakukan dengan menjumlahkan nilai ASCII dari setiap karakter menggunakan fungsi ord(), kemudian hasilnya dibagi menggunakan operasi modulo terhadap ukuran tabel (self.size). Dengan mekanisme tersebut, indeks yang dihasilkan selalu berada dalam rentang yang valid, yaitu antara 0 hingga size - 1.

Method insert

Method insert digunakan untuk menambahkan kontak baru ke dalam tabel hash. Proses dimulai dengan menghitung indeks awal menggunakan hash_function. Jika slot yang dituju masih kosong, data dapat langsung disimpan.

Namun, apabila slot tersebut sudah terisi (collision), program menerapkan teknik Linear Probing, yaitu mencari slot kosong berikutnya secara berurutan menggunakan rumus (index + i) % self.size. Pencarian berlanjut hingga ditemukan lokasi yang tersedia.

Sebelum penyimpanan dilakukan, sistem juga memeriksa apakah nama yang sama sudah ada dalam tabel. Jika ditemukan duplikasi, proses dibatalkan dan pengguna akan menerima pesan bahwa nama tersebut telah digunakan. Apabila seluruh slot telah diperiksa dan tidak ada ruang kosong yang tersedia, program akan menampilkan pesan bahwa tabel hash telah penuh.

Method search

Method search berfungsi untuk mencari data kontak berdasarkan nama. Mekanisme pencariannya serupa dengan proses penyisipan, yaitu dimulai dari indeks hasil hashing dan dilanjutkan menggunakan teknik Linear Probing apabila diperlukan.

Jika selama proses pencarian ditemukan slot kosong (None), pencarian dapat langsung dihentikan karena dalam metode Linear Probing kondisi tersebut menandakan bahwa data yang dicari tidak pernah ditempatkan setelah titik tersebut. Apabila nama yang dicari ditemukan, method akan mengembalikan objek Contact yang sesuai. Sebaliknya, jika seluruh slot telah ditelusuri tanpa hasil, method akan mengembalikan nilai None.

Method delete

Method delete digunakan untuk menghapus data kontak berdasarkan nama. Prosesnya diawali dengan pencarian menggunakan teknik yang sama seperti pada method search.

Jika sistem menemukan slot kosong sebelum menemukan nama yang dicari, proses langsung dihentikan dan program menampilkan pesan bahwa kontak tidak ditemukan. Apabila data berhasil ditemukan, slot tersebut akan diubah menjadi None sebagai penanda bahwa kontak telah dihapus.

Meskipun pendekatan ini sederhana, penghapusan langsung dengan mengembalikan slot ke None berpotensi menimbulkan masalah yang dikenal sebagai cluster break, yaitu terputusnya jalur pencarian pada metode Linear Probing. Namun, untuk implementasi berskala kecil seperti program ini, dampaknya relatif tidak signifikan.

Method display

Method display bertugas menampilkan seluruh isi tabel hash dari indeks pertama hingga indeks terakhir. Setiap slot akan ditampilkan bersama status atau datanya.

Apabila slot masih kosong (None), program akan menampilkan keterangan "Kosong". Sebaliknya, jika slot berisi objek Contact, method __str__ akan dipanggil secara otomatis sehingga informasi nama dan nomor telepon dapat ditampilkan dalam format yang lebih terstruktur dan mudah dibaca.

Program Utama (Main Loop)

Bagian akhir program berisi logika utama yang mengatur interaksi dengan pengguna. Berbeda dengan beberapa implementasi lain, bagian ini tidak dibungkus dalam fungsi main(), melainkan dijalankan secara langsung.

Program diawali dengan membuat objek HashMap yang memiliki kapasitas 10 slot. Selanjutnya, sistem memasuki perulangan while True yang akan terus berjalan hingga pengguna memilih opsi keluar.

Pada setiap iterasi, program menampilkan menu yang berisi beberapa pilihan operasi, seperti menambah kontak, mencari kontak, menghapus kontak, menampilkan seluruh data, dan keluar dari program. Input pengguna dibaca dalam bentuk string sehingga proses pengecekan dilakukan menggunakan nilai seperti "1", "2", "3", dan seterusnya.

Setiap pilihan akan memanggil method yang sesuai pada objek HashMap. Ketika pengguna memilih opsi keluar, program menjalankan perintah break untuk menghentikan perulangan. Jika input yang diberikan tidak sesuai dengan pilihan yang tersedia, sistem akan menampilkan pesan bahwa pilihan yang dimasukkan tidak valid.

Kesimpulan

Secara keseluruhan, program ini menerapkan struktur data Hash Map untuk mengelola data kontak secara efisien. Teknik Open Addressing dengan Linear Probing digunakan untuk menangani collision yang terjadi selama proses hashing. Melalui fitur penyimpanan, pencarian, penghapusan, dan penampilan data kontak, program menunjukkan bagaimana Hash Map dapat digunakan untuk mempercepat pengelolaan data dibandingkan pendekatan pencarian linear. Selain itu, pemisahan fungsi ke dalam beberapa method membuat kode lebih terstruktur, mudah dipahami, dan lebih mudah dikembangkan di masa mendatang.


Output Program:

<img width="415" height="550" alt="Screenshot 2026-06-06 201634" src="https://github.com/user-attachments/assets/7bf521c0-cf31-4f07-8114-d394937b3457" />
<img width="451" height="793" alt="Screenshot 2026-06-06 201645" src="https://github.com/user-attachments/assets/f550a693-d45c-47a3-bde4-2d7479fb8932" />
<img width="490" height="736" alt="Screenshot 2026-06-06 201655" src="https://github.com/user-attachments/assets/b1277bde-e0ce-45a9-ab45-fcae06b90cc6" />


Link Youtube: (https://youtu.be/LS0ggbNmo_0)


