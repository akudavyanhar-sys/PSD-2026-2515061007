Deskripsi Singkat:

Program ini merupakan aplikasi sederhana berbasis Python yang dirancang untuk mengurutkan total nilai siswa SMA dari Semester 1 hingga Semester 5. Pengguna diminta memasukkan jumlah siswa, nama masing-masing siswa, serta nilai pada setiap semester. Data tersebut kemudian diolah untuk menghitung total nilai tiap siswa, yang selanjutnya disimpan dalam struktur data berupa list berisi dictionary (pasangan antara nama dan total nilai).
Setelah seluruh data terkumpul, program melakukan proses pengurutan menggunakan algoritma Bubble Sort. Algoritma ini bekerja dengan cara membandingkan elemen yang bersebelahan secara berulang, lalu menukarnya apabila urutan yang dihasilkan tidak sesuai. Proses tersebut berlangsung dalam beberapa iterasi hingga seluruh data tersusun dengan benar. Dalam implementasinya, pengurutan dilakukan secara descending, sehingga siswa dengan total nilai tertinggi akan menempati posisi teratas.
Hasil akhir ditampilkan dalam bentuk peringkat siswa berdasarkan total nilai yang diperoleh. Selain itu, program juga menerapkan pendekatan modular dengan memisahkan fungsi penukaran data (tukar), proses pengurutan (bubble_sort), dan fungsi utama (main). Pemisahan ini bertujuan untuk meningkatkan keterbacaan kode sekaligus mempermudah proses pengelolaan dan pengembangan program di masa mendatang.


Source Code:

<img width="813" height="1454" alt="image" src="https://github.com/user-attachments/assets/53df1071-42d4-4fd7-9ad6-0aa78b864ac9" />


Gambaran Umum

Fungsi tukar()

Fungsi tukar() digunakan untuk menukar posisi dua elemen dalam sebuah array. Prosesnya diawali dengan menyimpan nilai pada indeks pertama ke dalam variabel sementara (temp) agar tidak hilang saat dilakukan penimpaan. Selanjutnya, nilai pada indeks kedua dipindahkan ke indeks pertama, dan nilai yang disimpan di temp ditempatkan kembali ke indeks kedua. Mekanisme ini dapat dianalogikan seperti menukar isi dua wadah yang membutuhkan satu wadah tambahan sebagai penampung sementara. Fungsi bubble_sort()

Fungsi bubble_sort() berperan dalam mengurutkan data menggunakan algoritma Bubble Sort. Proses pengurutan dilakukan melalui dua perulangan bertingkat (nested loop). Perulangan luar berjalan sebanyak n-1kali, yang menandakan jumlah tahapan pengurutan. Pada setiap tahap, satu elemen dengan nilai terbesar akan “naik” ke posisi yang semestinya. Sementara itu, perulangan dalam bertugas membandingkan elemen-elemen yang bersebelahan. Jumlah perbandingan akan semakin berkurang pada setiap iterasi karena sebagian data di bagian akhir sudah dalam kondisi terurut. Jika ditemukan bahwa nilai di posisi kiri lebih kecil dibandingkan dengan posisi kanan (dalam konteks pengurutan descending), maka kedua elemen tersebut akan ditukar menggunakan fungsi tukar(). Sebagai ilustrasi, misalkan terdapat tiga data siswa dengan total nilai: Aldi (416), Bella (444), dan Cindy (473). Pada iterasi pertama, Aldi dan Bella dibandingkan lalu ditukar, diikuti dengan perbandingan Aldi dan Cindy yang juga menghasilkan pertukaran. Iterasi berikutnya memastikan bahwa Cindy berada di posisi teratas karena sudah memiliki nilai tertinggi. Hasil akhirnya adalah urutan: Cindy, Bella dan Aldi.

Fungsi main()

Input Jumlah Siswa

Program terlebih dahulu meminta jumlah siswa yang akan dimasukkan. Untuk menjaga keandalan, digunakan mekanisme try/except guna menangani kesalahan input, seperti ketika pengguna memasukkan data non-numerik.

Input Data Siswa

Data siswa disimpan dalam sebuah list kosong. Program kemudian melakukan perulangan sebanyak jumlah siswa untuk menginput nama dan nilai. Nilai dimasukkan untuk lima semester secara berurutan, dengan validasi input pada setiap langkah agar hanya menerima angka. Seluruh nilai tersebut dijumlahkan dan disimpan sebagai total nilai. Setiap data siswa direpresentasikan dalam bentuk dictionary yang berisi pasangan nama dan total nilai, lalu ditambahkan ke dalam list.

Menampilkan Data Awal

Sebelum proses pengurutan, program menampilkan seluruh data siswa sesuai urutan input. Hal ini bertujuan untuk memberikan gambaran kondisi data sebelum diolah lebih lanjut.

Proses Pengurutan dan Penentuan Ranking

Setelah fungsi bubble_sort() dijalankan, data siswa akan tersusun dari nilai tertinggi ke terendah. Program kemudian menampilkan daftar peringkat berdasarkan posisi masing-masing siswa dalam list yang telah terurut.

Blok Eksekusi Utama

Struktur ini memastikan bahwa fungsi main() hanya dijalankan ketika program dieksekusi secara langsung, bukan saat file digunakan sebagai modul dalam program lain.

Kesimpulan

Program ini mengintegrasikan beberapa konsep dasar dalam pemrograman, yaitu penggunaan algoritma Bubble Sort untuk pengurutan secara descending, struktur data dictionary untuk menyimpan pasangan nama dan nilai, serta list sebagai wadah utama data. Selain itu, validasi input dilakukan melalui mekanisme try/except untuk mencegah kesalahan saat eksekusi. Proses pengurutan memanfaatkan nested loop, sedangkan perhitungan total nilai dilakukan melalui teknik akumulasi secara bertahap.


Link Youtube: https://youtu.be/bvZx_jm7X_g

