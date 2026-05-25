Judul Program: Program informasi barang

Deskripsi Singkat:

Program ini merupakan sistem inventaris gudang sederhana yang dibangun menggunakan struktur data Binary Search Tree (BST) dengan bahasa pemrograman Python. Sistem dirancang untuk membantu pengelolaan data barang berdasarkan nama dan harga barang sehingga proses penyimpanan maupun pencarian data dapat dilakukan dengan lebih teratur.

Melalui program ini, pengguna dapat melakukan beberapa operasi utama, seperti menambahkan data barang, mencari barang tertentu, menampilkan seluruh daftar barang secara terurut, hingga menghapus data barang dari inventaris. Seluruh data disimpan dalam bentuk struktur pohon biner yang terorganisasi berdasarkan urutan alfabetis nama barang.

Selain menyediakan operasi dasar BST seperti insert, search, delete, dan traversal inorder, program ini juga dilengkapi fitur find successor dan find predecessor. Kedua fitur tersebut digunakan untuk mencari barang dengan harga yang paling mendekati nilai acuan, baik harga yang lebih besar maupun lebih kecil.

Penerapan BST pada program ini membuat proses pengelolaan data menjadi lebih efisien dibandingkan penyimpanan linear biasa. Setiap proses pencarian, penambahan, dan penghapusan data dapat dilakukan secara lebih cepat karena sistem hanya menelusuri cabang tertentu yang relevan, bukan memeriksa seluruh data satu per satu. Dengan demikian, program tidak hanya berfungsi sebagai media penyimpanan inventaris, tetapi juga sebagai implementasi nyata konsep struktur data BST dalam pengelolaan informasi barang secara terstruktur dan sistematis.

Source Code:

<img width="1402" height="7284" alt="image" src="https://github.com/user-attachments/assets/1b8b9b65-74a3-4302-aadc-4704cc41eb1f" />

 
Gambaran Umum:

Program ini dirancang sebagai sistem inventaris gudang sederhana yang memanfaatkan struktur data Binary Search Tree (BST) menggunakan bahasa Python. Seluruh data barang disimpan berdasarkan urutan nama barang sehingga proses pengelolaan data menjadi lebih rapi dan efisien. Melalui sistem ini, pengguna dapat menambahkan barang, mencari data barang, menampilkan daftar barang secara terurut, hingga menghapus data dari inventaris. Selain operasi dasar BST, program juga menyediakan fitur pencarian harga terdekat yang lebih besar (successor) dan lebih kecil (predecessor) dari suatu nilai tertentu.

Class Node

Class Node berfungsi sebagai komponen dasar dalam pembentukan BST. Setiap node merepresentasikan satu data barang yang terdiri atas atribut nama_barang dan harga. Selain menyimpan informasi utama barang, node juga memiliki atribut left dan right yang digunakan untuk menunjuk child kiri dan child kanan pada pohon. Kedua atribut tersebut diinisialisasi dengan nilai None karena node baru belum memiliki cabang. Dengan struktur ini, setiap data barang dapat saling terhubung membentuk pohon biner yang terorganisasi.

Class BinarySearchTree

Class BinarySearchTree bertugas mengelola seluruh struktur BST beserta operasi-operasi yang berjalan di dalamnya. Ketika objek BST dibuat, atribut self.root diatur bernilai None sebagai tanda bahwa pohon masih kosong. Root menjadi titik awal dari seluruh proses karena setiap operasi seperti pencarian, penambahan, maupun penghapusan node selalu dimulai dari bagian tersebut.

Method insert()

Method insert() digunakan untuk menambahkan data barang baru ke dalam BST secara rekursif. Proses dimulai dengan membandingkan nama barang yang akan dimasukkan dengan nama pada node saat ini menggunakan fungsi lower() agar perbandingan tidak dipengaruhi huruf kapital maupun huruf kecil. Jika nama barang lebih kecil secara alfabetis, data akan ditempatkan pada cabang kiri. Sebaliknya, jika lebih besar, data akan diarahkan ke cabang kanan. Apabila nama barang sudah tersedia, program akan menampilkan pesan bahwa data tidak dapat ditambahkan kembali. Pendekatan ini menjaga struktur BST tetap terurut sehingga proses pencarian menjadi lebih cepat dan efisien.

Method find_successor()

Method find_successor() digunakan untuk mencari barang dengan harga yang lebih besar namun paling mendekati nilai acuan tertentu. Proses pencarian dilakukan secara iteratif mulai dari root. Jika harga acuan lebih kecil dari harga node saat ini, node tersebut disimpan sebagai kandidat successor dan traversal dilanjutkan ke subtree kiri untuk mencari nilai yang lebih dekat. Jika harga acuan lebih besar atau sama, pencarian bergerak ke kanan. Dengan mekanisme ini, program dapat menemukan harga minimum yang masih lebih besar dari nilai referensi.

Method find_predecessor()

Method find_predecessor() memiliki fungsi yang berlawanan dengan find_successor(). Method ini digunakan untuk mencari barang dengan harga yang lebih kecil tetapi paling mendekati nilai acuan. Jika harga acuan lebih besar dari node saat ini, node tersebut dicatat sebagai kandidat predecessor lalu pencarian bergerak ke kanan. Sebaliknya, jika harga lebih kecil atau sama, traversal diarahkan ke kiri. Hasil akhirnya adalah node dengan harga terbesar yang masih berada di bawah nilai referensi.

Method search()

Method search() berfungsi mencari data barang berdasarkan nama secara rekursif. Jika node yang sedang diperiksa bernilai None, berarti barang tidak ditemukan dan method akan mengembalikan nilai kosong. Jika nama barang cocok dengan node saat ini, node tersebut langsung dikembalikan sebagai hasil pencarian. Apabila nama yang dicari lebih kecil secara alfabetis, pencarian dilanjutkan ke subtree kiri, sedangkan jika lebih besar proses berpindah ke subtree kanan. Pola ini membuat pencarian lebih efisien karena setiap langkah hanya memeriksa cabang yang relevan.

Method inorder()

Method inorder() digunakan untuk menampilkan seluruh data barang menggunakan teknik inorder traversal. Traversal dilakukan dengan urutan mengunjungi subtree kiri, kemudian node saat ini, lalu subtree kanan. Karena BST tersusun berdasarkan urutan alfabetis nama barang, metode ini secara otomatis menghasilkan tampilan data yang sudah terurut dari A sampai Z. Selain itu, method juga menampilkan nama barang dan harga dengan format yang lebih rapi sehingga mudah dibaca pengguna.

Method min_value_node()

Method min_value_node() merupakan method pembantu yang digunakan dalam proses penghapusan node. Fungsinya adalah mencari node dengan nilai terkecil dalam suatu subtree. Proses dilakukan dengan terus bergerak ke cabang kiri hingga tidak ada lagi child kiri yang tersedia. Node paling kiri tersebut dianggap sebagai node dengan nilai minimum dan digunakan sebagai pengganti dalam proses penghapusan node yang memiliki dua child.

Method delete()

Method delete() digunakan untuk menghapus data barang dari BST secara rekursif. Pertama, sistem mencari node yang akan dihapus menggunakan pola traversal yang sama seperti method search(). Setelah node ditemukan, terdapat tiga kondisi yang harus ditangani. Jika node tidak memiliki child kiri, posisinya akan digantikan oleh child kanan. Jika node tidak memiliki child kanan, maka digantikan oleh child kiri. Namun, jika node memiliki dua child, sistem akan mencari node pengganti menggunakan min_value_node() pada subtree kanan. Data dari node pengganti kemudian disalin ke node yang dihapus, lalu node pengganti dihapus dari posisi awalnya. Cara ini memastikan struktur BST tetap valid setelah proses penghapusan berlangsung.

Fungsi main()

Fungsi main() menjadi pusat kendali seluruh program dan mengatur interaksi antara pengguna dengan sistem inventaris. Pada awal program, dibuat objek BST bernama bst, kemudian variabel pilih diinisialisasi dengan nilai 0. Program berjalan menggunakan perulangan while hingga pengguna memilih menu keluar.
Di setiap iterasi, sistem menampilkan daftar menu dan meminta pengguna memasukkan pilihan. Input menu dibungkus menggunakan try/except untuk menangani kesalahan input, misalnya ketika pengguna memasukkan karakter selain angka. Jika terjadi kesalahan, program akan menampilkan pesan error lalu kembali ke menu utama tanpa menghentikan eksekusi program.
Setiap menu memiliki fungsi yang berbeda:

•	Menu 1 digunakan untuk menambahkan barang baru menggunakan method insert().

•	Menu 2 digunakan untuk mencari harga yang lebih besar terdekat menggunakan find_successor().

•	Menu 3 digunakan untuk mencari harga yang lebih kecil terdekat menggunakan find_predecessor().

•	Menu 4 digunakan untuk mencari barang berdasarkan nama menggunakan search().

•	Menu 5 digunakan untuk menampilkan seluruh data barang menggunakan traversal inorder().

•	Menu 6 digunakan untuk menghapus barang menggunakan method delete().

•	Menu 7 digunakan untuk mengakhiri program.

Dengan struktur menu tersebut, pengguna dapat mengelola data inventaris secara interaktif, sistematis, dan lebih mudah dipahami.

Kesimpulan

Secara keseluruhan, program ini merupakan implementasi Binary Search Tree dalam sistem inventaris barang berbasis Python. BST digunakan untuk menyimpan data barang secara terurut sehingga proses pencarian, penambahan, dan penghapusan dapat dilakukan lebih efisien dibandingkan struktur linear biasa. Program ini juga memperlihatkan penerapan konsep rekursi pada hampir seluruh operasi utamanya, sehingga alur pengolahan data menjadi lebih terstruktur, fleksibel, dan mudah dipelajari.



Output Program:

Link Youtube: 
