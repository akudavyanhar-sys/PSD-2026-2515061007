Judul Program: Program pencari kursi peserta UTBK

Deskripsi Singkat:

Program ini merupakan aplikasi berbasis Python yang dirancang untuk menentukan posisi nomor peserta dalam susunan kursi ujian sekaligus mengidentifikasi letak kursinya, meliputi baris, kolom, dan kategori posisi. Data kursi disusun dalam bentuk array berisi angka 1 hingga 200 yang sudah terurut, sehingga memungkinkan penerapan metode pencarian yang lebih efisien. Pengguna cukup memasukkan nomor peserta, lalu sistem akan menelusuri data tersebut dan menampilkan informasi posisi duduk secara lengkap.

Proses pencarian memanfaatkan algoritma Binary Search, yang bekerja dengan membagi ruang pencarian menjadi dua bagian secara berulang. Pada setiap langkah, algoritma menentukan elemen tengah sebagai titik pembanding. Jika nilai yang dicari tidak ditemukan pada posisi tersebut, pencarian dilanjutkan ke sisi kiri atau kanan sesuai hasil perbandingan. Pendekatan ini membuat proses pencarian jauh lebih cepat, dengan kompleksitas waktu sebesar O(logn).

Selain pencarian, program juga dilengkapi fungsi untuk menentukan posisi kursi secara lebih spesifik. Nomor peserta yang ditemukan akan dikonversi menjadi koordinat baris dan kolom, kemudian diklasifikasikan ke dalam kategori depan, tengah, atau belakang berdasarkan rentang baris tertentu.

Source Code:

<img width="1494" height="2876" alt="image" src="https://github.com/user-attachments/assets/c3566dda-4b6a-48a9-a3be-449573f49c5a" />

Gambaran Umum

Program ini merupakan aplikasi pencarian nomor kursi peserta ujian yang memanfaatkan algoritma *Binary Search* pada data kursi bernomor 1 hingga 200. Secara struktur, program dibagi menjadi tiga fungsi utama, yaitu binary_search() untuk proses pencarian, get_posisi() untuk menentukan lokasi kursi, dan main() sebagai pengendali utama alur program.

Fungsi binary_search()

Fungsi binary_search() digunakan untuk menemukan nomor kursi dalam sebuah list data. Fungsi ini menerima tiga parameter: arr sebagai kumpulan data, n sebagai jumlah elemen, dan target sebagai nilai yang dicari. Di tahap awal, ditetapkan dua batas pencarian, yaitu batas kiri (l) yang dimulai dari indeks 0 dan batas kanan (r) yang berada pada indeks terakhir. Selain itu, variabel pos diinisialisasi dengan nilai -1 sebagai indikator bahwa data belum ditemukan.

Proses pencarian berlangsung dalam perulangan selama batas kiri belum melampaui batas kanan. Pada setiap iterasi, dihitung indeks tengah (`m`) dari rentang pencarian. Jika nilai pada posisi tersebut sama dengan target, maka indeks disimpan ke dalam pos dan proses dihentikan. Jika nilai tengah lebih kecil dari target, pencarian dilanjutkan ke sisi kanan dengan menggeser batas kiri ke m + 1. Sebaliknya, jika nilai tengah lebih besar, pencarian berpindah ke sisi kiri dengan menggeser batas kanan ke m - 1. Pendekatan ini secara konsisten mempersempit ruang pencarian hingga data ditemukan atau tidak tersedia. Nilai akhir pos kemudian dikembalikan sebagai hasil fungsi.

Fungsi get_posisi()

Fungsi get_posisi() berfungsi untuk menentukan lokasi fisik kursi berdasarkan nomor peserta. Dengan asumsi setiap baris terdiri dari 10 kursi, posisi baris dihitung menggunakan rumus pembagian bulat, sedangkan posisi kolom menggunakan operasi modulo. Setelah baris diketahui, kursi diklasifikasikan ke dalam tiga zona, yaitu depan (baris 1–7), tengah (baris 8–14), dan belakang (baris 15 ke atas). Fungsi ini mengembalikan tiga informasi sekaligus, yaitu baris, kolom, dan kategori posisi.


Fungsi main()

Fungsi main() berperan sebagai pusat eksekusi program. Pada tahap awal, dibuat list berisi angka 1 hingga 200 menggunakan range(). Data ini sudah dalam kondisi terurut, yang merupakan syarat utama agar algoritma Binary Search dapat diterapkan secara optimal.

Selanjutnya, pengguna diminta memasukkan nomor peserta yang ingin dicari. Proses input dilengkapi dengan validasi menggunakan perulangan while True dan mekanisme try/except untuk memastikan bahwa nilai yang dimasukkan berupa angka dan berada dalam rentang yang valid. Jika input tidak sesuai, pengguna akan diminta mengulang hingga benar.

Setelah input valid diperoleh, fungsi binary_search() dipanggil untuk mencari posisi data dalam list. Jika nilai yang dikembalikan bukan -1, program akan melanjutkan dengan memanggil fungsi get_posisi()
 untuk memperoleh detail lokasi kursi. Informasi yang ditampilkan mencakup indeks data, nomor peserta, baris, kolom, dan kategori posisi. Sebaliknya, jika data tidak ditemukan, program akan menampilkan pesan yang sesuai.

Kesimpulan

Secara keseluruhan, program ini menunjukkan penerapan algoritma *Binary Search* sebagai metode pencarian yang efisien dengan cara mempersempit ruang pencarian secara bertahap. Selain itu, program juga mengintegrasikan perhitungan matematis sederhana untuk menentukan posisi kursi, serta validasi input yang membuat sistem lebih andal dan tidak mudah mengalami kesalahan saat dijalankan.

Output Program:

<img width="491" height="599" alt="Screenshot 2026-05-05 201854" src="https://github.com/user-attachments/assets/527a5fa0-5cd8-495a-99dd-5dd7b7435c5f" />
<img width="514" height="232" alt="Screenshot 2026-05-05 201905" src="https://github.com/user-attachments/assets/16ae4738-1d4e-457d-8d12-217496b1d3eb" />
<img width="503" height="597" alt="Screenshot 2026-05-05 201916" src="https://github.com/user-attachments/assets/5962553f-a9bc-4256-9791-aaac1b718c15" />

Link Youtube: Penjelasan per kode


