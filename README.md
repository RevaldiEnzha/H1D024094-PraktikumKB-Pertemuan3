# Fuzzy Logic System – Studi Kasus

## Deskripsi
Repositori ini berisi implementasi **sistem logika fuzzy menggunakan Python** untuk menyelesaikan dua studi kasus berbeda.
Program dibuat menggunakan library **scikit-fuzzy** untuk membangun sistem inferensi fuzzy yang memproses beberapa variabel input dan menghasilkan keputusan sebagai output.

Terdapat dua file program utama:
1. **studiKasus1 - Toko Hewan.py**
   Sistem fuzzy untuk menentukan jumlah **stok makanan hewan** berdasarkan kondisi penjualan.
2. **studiKasus2 - Pelayanan Masyarakat.py**
   Sistem fuzzy untuk menentukan tingkat **kepuasan pelayanan masyarakat** berdasarkan beberapa indikator pelayanan.

---

# Library yang Digunakan

Program menggunakan beberapa library Python berikut:
* numpy
* scikit-fuzzy (skfuzzy)
* matplotlib (digunakan oleh skfuzzy untuk menampilkan grafik)

Install library dengan perintah:

```
pip install numpy scikit-fuzzy matplotlib
```

---

# Studi Kasus 1 – Toko Hewan

File: `studiKasus1 - Toko Hewan.py`

Program ini menggunakan sistem fuzzy untuk menentukan jumlah **stok makanan hewan** berdasarkan kondisi penjualan dan keuntungan.

### Variabel Input

* barangTerjual
* permintaan
* hargaPerItem
* profit

### Variabel Output

* stokMakanan

### Struktur Program

#### 1. Import Library

Bagian ini mengimpor library yang diperlukan untuk menjalankan sistem fuzzy.

#### 2. Definisi Variabel Fuzzy

Pada bagian ini dibuat variabel **antecedent (input)** dan **consequent (output)** beserta rentang nilainya.

#### 3. Fungsi Keanggotaan

Setiap variabel dibagi ke dalam beberapa kategori menggunakan **membership function** seperti:

* rendah
* sedang
* tinggi
* murah
* mahal

#### 4. Aturan Fuzzy

Bagian ini mendefinisikan beberapa aturan yang menghubungkan kondisi input dengan keputusan jumlah stok makanan.

#### 5. Pembuatan Sistem Fuzzy

Semua aturan kemudian digabungkan menggunakan **ControlSystem** untuk membentuk mesin inferensi fuzzy.

#### 6. Simulasi Sistem

Nilai input dimasukkan ke sistem, kemudian diproses menggunakan `compute()` untuk menghasilkan jumlah stok makanan yang disarankan.

#### 7. Menampilkan Hasil

Hasil ditampilkan di console dan divisualisasikan dalam grafik membership function.

---

# Studi Kasus 2 – Pelayanan Masyarakat

File: `studiKasus2 - Pelayanan Masyarakat.py`


Program ini menggunakan sistem fuzzy untuk menentukan tingkat **kepuasan pelayanan masyarakat** berdasarkan beberapa indikator pelayanan.

### Variabel Input

* kejelasanInformasi
* kejelasanPersyaratan
* kemampuanPetugas
* ketersediaanSarpras

### Variabel Output

* kepuasanPelayanan

### Struktur Program

#### 1. Import Library

Bagian ini mengimpor library yang digunakan untuk membangun sistem fuzzy.

#### 2. Definisi Variabel Fuzzy

Variabel input dan output didefinisikan beserta rentang nilainya.

#### 3. Fungsi Keanggotaan

Setiap variabel input dibagi menjadi beberapa kategori seperti:

* tidak memuaskan
* cukup memuaskan
* memuaskan

Sedangkan variabel output memiliki lima kategori kepuasan.

#### 4. Aturan Fuzzy

Program mendefinisikan **81 aturan fuzzy** yang merepresentasikan berbagai kombinasi kondisi pelayanan untuk menentukan tingkat kepuasan masyarakat.

#### 5. Pembuatan Sistem Fuzzy

Semua aturan digabungkan menjadi satu sistem inferensi menggunakan **ControlSystem**.

#### 6. Simulasi Sistem

Nilai input dimasukkan ke dalam sistem, kemudian diproses menggunakan `compute()` untuk menghasilkan nilai kepuasan pelayanan.

#### 7. Menampilkan Hasil

Output sistem ditampilkan di console serta divisualisasikan dalam grafik membership function.

---

# Cara Menjalankan Program

1. Pastikan Python sudah terinstall
2. Install library yang diperlukan
3. Jalankan salah satu file Python

Contoh:

```
python "studiKasus1 - Toko Hewan.py"
```

atau

```
python "studiKasus2 - Pelayanan Masyarakat.py"
```

Program akan menampilkan hasil perhitungan fuzzy berdasarkan nilai input yang digunakan.

---

# Tujuan Program

Program ini dibuat sebagai implementasi konsep logika fuzzy dalam pengambilan keputusan, khususnya untuk:
* membantu menentukan jumlah stok produk
* mengevaluasi tingkat kepuasan pelayanan
