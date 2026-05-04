Deskripsi Singkat:

Program ini merupakan aplikasi sederhana berbasis Python yang dirancang untuk mengurutkan total nilai siswa SMA dari Semester 1 hingga Semester 5. Pengguna diminta memasukkan jumlah siswa, nama masing-masing siswa, serta nilai pada setiap semester. Data tersebut kemudian diolah untuk menghitung total nilai tiap siswa, yang selanjutnya disimpan dalam struktur data berupa list berisi dictionary (pasangan antara nama dan total nilai).
Setelah seluruh data terkumpul, program melakukan proses pengurutan menggunakan algoritma Bubble Sort. Algoritma ini bekerja dengan cara membandingkan elemen yang bersebelahan secara berulang, lalu menukarnya apabila urutan yang dihasilkan tidak sesuai. Proses tersebut berlangsung dalam beberapa iterasi hingga seluruh data tersusun dengan benar. Dalam implementasinya, pengurutan dilakukan secara descending, sehingga siswa dengan total nilai tertinggi akan menempati posisi teratas.
Hasil akhir ditampilkan dalam bentuk peringkat siswa berdasarkan total nilai yang diperoleh. Selain itu, program juga menerapkan pendekatan modular dengan memisahkan fungsi penukaran data (tukar), proses pengurutan (bubble_sort), dan fungsi utama (main). Pemisahan ini bertujuan untuk meningkatkan keterbacaan kode sekaligus mempermudah proses pengelolaan dan pengembangan program di masa mendatang.


Source Code:

<img width="813" height="1454" alt="image" src="https://github.com/user-attachments/assets/53df1071-42d4-4fd7-9ad6-0aa78b864ac9" />


Gambaran Umum

# Penjelasan Per Baris Kode Program Ranking Siswa

---

## 🔷 Fungsi `tukar()`

| Baris | Kode | Penjelasan |
|---|---|---|
| 1 | `def tukar(arr, i, j):` | Mendefinisikan fungsi bernama `tukar` yang menerima 3 parameter: `arr` (list data), `i` dan `j` (dua posisi indeks yang akan ditukar) |
| 2 | `temp = arr[i]` | Menyimpan sementara data di posisi `i` ke variabel `temp`, agar tidak hilang saat ditimpa |
| 3 | `arr[i] = arr[j]` | Mengisi posisi `i` dengan data yang ada di posisi `j` |
| 4 | `arr[j] = temp` | Mengisi posisi `j` dengan data lama dari posisi `i` yang tadi disimpan di `temp` |

---

## 🔷 Fungsi `bubble_sort()`

| Baris | Kode | Penjelasan |
|---|---|---|
| 5 | `def bubble_sort(arr, n):` | Mendefinisikan fungsi `bubble_sort` yang menerima `arr` (list siswa) dan `n` (jumlah siswa) |
| 6 | `for i in range(n - 1):` | Perulangan luar yang berjalan sebanyak `n-1` kali, mewakili jumlah putaran sorting |
| 7 | `for j in range(n - i - 1):` | Perulangan dalam yang membandingkan dua elemen berdampingan, batas kanannya berkurang tiap putaran karena elemen terbesar sudah berada di posisi yang benar |
| 8 | `if arr[j]["total"] < arr[j + 1]["total"]:` | Mengecek apakah total nilai di posisi `j` lebih kecil dari posisi `j+1`, jika iya berarti urutannya perlu dibalik (karena ingin descending) |
| 9 | `tukar(arr, j, j + 1)` | Memanggil fungsi `tukar()` untuk menukar posisi `j` dan `j+1` agar yang bernilai lebih besar naik ke posisi kiri |

---

## 🔷 Fungsi `main()`

| Baris | Kode | Penjelasan |
|---|---|---|
| 10 | `def main():` | Mendefinisikan fungsi utama `main` sebagai pusat jalannya program |
| 11 | `try:` | Memulai blok percobaan untuk menangkap kemungkinan error saat input |
| 12 | `n = int(input("Masukkan jumlah siswa: "))` | Meminta pengguna memasukkan jumlah siswa dan mengubahnya menjadi bilangan bulat |
| 13 | `except ValueError:` | Menangkap error jika pengguna memasukkan bukan angka (misal huruf atau simbol) |
| 14 | `print("Input tidak valid!")` | Mencetak pesan error jika input jumlah siswa tidak valid |
| 15 | `return` | Menghentikan fungsi `main()` jika terjadi error di atas |
| 16 | `siswa = []` | Membuat list kosong bernama `siswa` sebagai wadah untuk menyimpan semua data siswa |
| 17 | `print("\nMasukkan data siswa:")` | Mencetak judul bagian input data siswa ke layar |
| 18 | `for i in range(n):` | Memulai perulangan sebanyak `n` kali, satu kali untuk setiap siswa |
| 19 | `print(f"\nData siswa ke-{i+1}")` | Mencetak header yang menunjukkan siswa ke berapa yang sedang diinput (dimulai dari 1) |
| 20 | `nama = input("Nama: ")` | Meminta pengguna memasukkan nama siswa dan menyimpannya di variabel `nama` |
| 21 | `total = 0` | Menginisialisasi variabel `total` dengan nilai 0 sebagai akumulator penjumlahan nilai semester |
| 22 | `for semester in range(1, 6):` | Memulai perulangan sebanyak 5 kali untuk input nilai dari semester 1 sampai semester 5 |
| 23 | `while True:` | Memulai perulangan tak terbatas yang akan terus berulang sampai input nilai valid |
| 24 | `try:` | Memulai blok percobaan untuk menangkap error saat input nilai |
| 25 | `nilai = float(input(f"Nilai Semester {semester}: "))` | Meminta input nilai untuk semester tertentu dan mengubahnya menjadi bilangan desimal |
| 26 | `total += nilai` | Menambahkan nilai semester yang baru diinput ke variabel `total` (akumulasi) |
| 27 | `break` | Menghentikan perulangan `while True` karena input nilai sudah berhasil dan valid |
| 28 | `except ValueError:` | Menangkap error jika pengguna memasukkan bukan angka untuk nilai semester |
| 29 | `print("Input tidak valid, masukkan angka!")` | Mencetak pesan peringatan dan perulangan `while` akan mengulang input dari awal |
| 30 | `siswa.append({"nama": nama, "total": total})` | Menyimpan data siswa berupa dictionary berisi nama dan total nilai ke dalam list `siswa` |
| 31 | `print("\nData sebelum diurutkan:")` | Mencetak judul untuk menampilkan data siswa sebelum proses sorting |
| 32 | `for s in siswa:` | Memulai perulangan untuk menelusuri setiap data siswa dalam list `siswa` |
| 33 | `print(f"{s['nama']} - {s['total']}")` | Mencetak nama dan total nilai setiap siswa dalam urutan asli sebelum diurutkan |
| 34 | `bubble_sort(siswa, n)` | Memanggil fungsi `bubble_sort()` untuk mengurutkan list `siswa` berdasarkan total nilai secara descending |
| 35 | `print(f"\nHasil dari pengurutan {n} siswa:")` | Mencetak judul hasil ranking setelah proses sorting selesai |
| 36 | `for i in range(n):` | Memulai perulangan sebanyak `n` kali untuk menampilkan hasil ranking satu per satu |
| 37 | `print(f"Ranking {i+1}")` | Mencetak nomor ranking siswa (dimulai dari 1) |
| 38 | `print(f"Nama  : {siswa[i]['nama']}")` | Mencetak nama siswa pada ranking tersebut |
| 39 | `print(f"Total : {siswa[i]['total']}")` | Mencetak total nilai siswa pada ranking tersebut |
| 40 | `print("-" * 30)` | Mencetak garis pemisah sepanjang 30 karakter untuk memperindah tampilan antar siswa |

---

## 🔷 Blok Eksekusi Utama

| Baris | Kode | Penjelasan |
|---|---|---|
| 41 | `if __name__ == "__main__":` | Mengecek apakah file ini dijalankan langsung (bukan diimpor oleh file lain) |
| 42 | `main()` | Jika kondisi di atas terpenuhi, maka fungsi `main()` dipanggil untuk memulai program |

Link Youtube: Penjelasan kode dan contoh penggunaannya

