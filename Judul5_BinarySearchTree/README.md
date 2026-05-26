Judul Program: Program informasi barang

Deskripsi Singkat:

Program ini merupakan sistem inventaris gudang sederhana yang dibangun menggunakan struktur data Binary Search Tree (BST) dengan bahasa pemrograman Python. Sistem dirancang untuk membantu pengelolaan data barang berdasarkan nama dan harga barang sehingga proses penyimpanan maupun pencarian data dapat dilakukan dengan lebih teratur.

Melalui program ini, pengguna dapat melakukan beberapa operasi utama, seperti menambahkan data barang, mencari barang tertentu, menampilkan seluruh daftar barang secara terurut, hingga menghapus data barang dari inventaris. Seluruh data disimpan dalam bentuk struktur pohon biner yang terorganisasi berdasarkan urutan alfabetis nama barang.

Selain menyediakan operasi dasar BST seperti insert, search, delete, dan traversal inorder, program ini juga dilengkapi fitur find successor dan find predecessor. Kedua fitur tersebut digunakan untuk mencari barang dengan harga yang paling mendekati nilai acuan, baik harga yang lebih besar maupun lebih kecil.

Penerapan BST pada program ini membuat proses pengelolaan data menjadi lebih efisien dibandingkan penyimpanan linear biasa. Setiap proses pencarian, penambahan, dan penghapusan data dapat dilakukan secara lebih cepat karena sistem hanya menelusuri cabang tertentu yang relevan, bukan memeriksa seluruh data satu per satu. Dengan demikian, program tidak hanya berfungsi sebagai media penyimpanan inventaris, tetapi juga sebagai implementasi nyata konsep struktur data BST dalam pengelolaan informasi barang secara terstruktur dan sistematis.

Source Code:

<img width="1402" height="8728" alt="image" src="https://github.com/user-attachments/assets/5ca86cdd-0d54-4dcf-9935-781a30f7fc30" />

 
Gambaran Umum:

Program ini merupakan sistem inventaris barang sederhana yang dibangun menggunakan struktur data Binary Search Tree (BST). Setiap data barang disimpan dalam bentuk node dan diurutkan berdasarkan nama barang secara alfabetis. Dengan pendekatan ini, proses pencarian, penambahan, maupun penghapusan data dapat dilakukan lebih cepat dan terstruktur dibandingkan penyimpanan linear biasa. Program juga menyediakan fitur tambahan untuk mencari barang dengan harga yang lebih besar atau lebih kecil dari nilai tertentu sehingga pengelolaan inventaris menjadi lebih fleksibel.

Class Node

Class Node berfungsi sebagai representasi dari setiap simpul (node) pada struktur BST. Setiap node menyimpan dua informasi utama, yaitu nama_barang dan harga. Selain itu, node juga memiliki dua pointer bernama left dan right yang digunakan untuk menunjuk child kiri dan child kanan pada pohon. Ketika node baru dibuat, kedua pointer tersebut otomatis bernilai None, yang berarti node belum memiliki cabang. Struktur ini memungkinkan setiap data barang saling terhubung membentuk pohon biner yang terorganisasi.

Class BinarySearchTree

Class BinarySearchTree bertugas mengelola seluruh struktur BST beserta operasi-operasi yang dilakukan di dalamnya. Seluruh proses seperti pencarian, penambahan, traversal, dan penghapusan node dikendalikan melalui class ini. Root pada BST menjadi titik awal seluruh operasi karena semua traversal selalu dimulai dari node tersebut.

Method insert()

Method insert() digunakan untuk menambahkan barang baru ke dalam BST. Mekanisme kerjanya mengikuti aturan dasar BST, yaitu membandingkan nama barang secara alfabetis dengan node saat ini. Jika nama barang lebih kecil, proses dilanjutkan ke cabang kiri. Sebaliknya, jika lebih besar, proses bergerak ke cabang kanan. Ketika ditemukan posisi kosong (None), node baru langsung dibuat pada posisi tersebut.

Perbandingan nama menggunakan fungsi .lower() agar program tidak membedakan huruf besar dan kecil. Dengan demikian, nama seperti “Laptop” dan “laptop” tetap dianggap sama. Jika barang sudah tersedia di dalam pohon, sistem akan menampilkan pesan bahwa data sudah ada tanpa menambahkan node baru. Pendekatan ini menjaga struktur BST tetap terurut sehingga operasi pencarian dapat berjalan lebih efisien.

Method search()

Method search() berfungsi untuk mencari barang berdasarkan nama. Pencarian dimulai dari root lalu membandingkan nama yang dicari dengan nama pada node saat ini. Jika data cocok, node tersebut langsung dikembalikan sebagai hasil pencarian. Jika nama yang dicari lebih kecil secara alfabetis, traversal bergerak ke subtree kiri. Sebaliknya, jika lebih besar, pencarian dilanjutkan ke subtree kanan.

Apabila traversal mencapai node bernilai None, artinya barang tidak ditemukan di dalam BST dan method akan mengembalikan nilai None. Pola pencarian seperti ini membuat BST lebih cepat dibandingkan pencarian linear karena setiap langkah hanya menelusuri cabang yang relevan.

Method inorder()

Method inorder() digunakan untuk menampilkan seluruh data barang secara terurut alfabetis menggunakan teknik in-order traversal. Traversal dilakukan dengan urutan mengunjungi subtree kiri terlebih dahulu, kemudian node saat ini, lalu subtree kanan.

Karena BST secara alami menyimpan data dengan aturan bahwa node kiri selalu lebih kecil dan node kanan lebih besar dibanding node induknya, hasil traversal inorder otomatis menghasilkan daftar barang yang tersusun rapi dari A hingga Z. Metode ini sangat berguna untuk menampilkan inventaris secara terstruktur dan mudah dibaca.

Method delete()

Method delete() digunakan untuk menghapus node berdasarkan nama barang. Proses penghapusan dilakukan dengan beberapa kondisi berbeda tergantung struktur node yang ditemukan.

Jika node tidak memiliki child, node dapat langsung dihapus. Jika node hanya memiliki satu child, posisi node tersebut akan digantikan oleh child yang dimilikinya. Namun, jika node memiliki dua child, sistem perlu mencari node pengganti menggunakan method min_value_node(), yaitu node dengan nilai terkecil pada subtree kanan (in-order successor). Data dari node pengganti kemudian disalin ke node yang dihapus, lalu node pengganti dihapus dari posisi awalnya. Teknik ini menjaga struktur BST tetap valid setelah proses penghapusan dilakukan.

Method find_successor() dan find_predecessor()

Kedua method ini digunakan untuk mencari barang berdasarkan rentang harga. Method find_successor() bertugas mencari barang dengan harga yang lebih besar dari harga acuan namun memiliki selisih paling kecil. Sebaliknya, find_predecessor() digunakan untuk mencari barang dengan harga yang lebih kecil dari harga acuan tetapi paling mendekati nilai tersebut.

Prosesnya dilakukan dengan mengumpulkan seluruh data barang melalui traversal inorder menggunakan helper get_all_items(). Setelah semua data terkumpul, program melakukan penyaringan berdasarkan kondisi harga lalu memilih nilai yang paling dekat dengan harga acuan. Dengan fitur ini, pengguna dapat memperoleh rekomendasi barang berdasarkan kisaran harga tertentu secara lebih praktis.

Fungsi main()

Fungsi main() menjadi pusat interaksi antara pengguna dan program melalui antarmuka berbasis teks (Command Line Interface / CLI). Program berjalan dalam perulangan while hingga pengguna memilih opsi keluar.

Menu utama menyediakan enam fitur utama, yaitu:

1. Menambahkan barang
2. Mencari harga lebih besar terdekat
3. Mencari harga lebih kecil terdekat
4. Mencari barang berdasarkan nama
5. Menampilkan seluruh data barang
6. Menghapus barang

Selain itu, tersedia opsi ketujuh untuk mengakhiri program. Setiap input dibungkus menggunakan try-except untuk menangani kesalahan input, misalnya ketika pengguna memasukkan huruf saat sistem meminta angka. Dengan mekanisme ini, program menjadi lebih aman dan tidak mudah berhenti akibat kesalahan pengguna.

Kesimpulan

Secara keseluruhan, program ini merupakan implementasi Binary Search Tree dalam sistem inventaris barang berbasis Python. BST digunakan untuk menyimpan data secara terurut sehingga proses pencarian, penambahan, dan penghapusan dapat dilakukan lebih efisien. Program juga memperlihatkan penerapan traversal, rekursi, serta pengelolaan node pada struktur pohon biner secara sistematis. Dengan fitur tambahan seperti pencarian successor dan predecessor, sistem inventaris menjadi lebih fleksibel dan fungsional untuk digunakan dalam pengelolaan data barang sederhana.

Output Program:

<img width="337" height="985" alt="Screenshot 2026-05-25 222014" src="https://github.com/user-attachments/assets/dcdd4222-26fd-4992-b610-09d7c353427c" />

<img width="468" height="707" alt="Screenshot 2026-05-25 222027" src="https://github.com/user-attachments/assets/59143737-0e4e-4816-9485-b54657494887" />

<img width="523" height="763" alt="Screenshot 2026-05-25 222039" src="https://github.com/user-attachments/assets/56c9a1e1-4983-493d-ab1f-b1e838ac780f" />

<img width="552" height="912" alt="Screenshot 2026-05-25 222050" src="https://github.com/user-attachments/assets/48de9e1b-186d-4a36-8e31-b101439fec3d" />

<img width="350" height="809" alt="Screenshot 2026-05-25 222100" src="https://github.com/user-attachments/assets/b6a206ad-d082-4cea-ad3a-3d2e005aed1e" />


Link Youtube: 
