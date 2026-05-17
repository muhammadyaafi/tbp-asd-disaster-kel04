# tbp-asd-disaster-kel04
# Disaster Response Logistics System

Disaster Response Logistics System menggunakan beberapa struktur data dan algoritma dasar seperti:

* Binary Search Tree (BST)
* Graph Adjacency List
* Breadth First Search (BFS)
* Algoritma Dijkstra
* Stack
* Priority Queue Linked List

Program dapat dijalankan melalui Command Line Interface (CLI).

---

# Fitur Sistem

* Menambahkan bantuan ke antrian prioritas
* Memproses bantuan berdasarkan tingkat prioritas bencana
* Menentukan rute optimal menggunakan algoritma Dijkstra
* Menampilkan lokasi yang tidak terjangkau menggunakan BFS
* Memperbarui level bencana
* Menampilkan riwayat pengiriman bantuan
* Menampilkan laporan seluruh lokasi bencana

---

# Struktur Data dan Algoritma

| Komponen                    | Implementasi                 |
| --------------------------- | ---------------------------- |
| Penyimpanan lokasi          | Binary Search Tree           |
| Penyimpanan rute            | Graph Adjacency List         |
| Antrian bantuan             | Priority Queue (Linked List) |
| Riwayat pengiriman          | Stack                        |
| Pencarian lokasi terjangkau | BFS                          |
| Jalur terpendek             | Dijkstra                     |

---

# Kompleksitas Waktu (Big-O)

| Fitur / Operasi Utama                    | Struktur Data / Algoritma    | Kompleksitas                          |
| ---------------------------------------- | ---------------------------- | ------------------------------------- |
| Menambahkan lokasi                       | Binary Search Tree (BST)     | O(log n) rata-rata  - O(n) worst-case |
| Mencari lokasi                           | Binary Search Tree (BST)     | O(log n) rata-rata                    |
| Menambahkan bantuan ke antrian prioritas | Priority Queue (Linked List) | O(n)                                  |
| Memproses bantuan prioritas tertinggi    | Priority Queue               | O(1)                                  |
| Menyimpan riwayat pengiriman             | Stack                        | O(1)                                  |
| Menampilkan riwayat pengiriman           | Stack Traversal              | O(n)                                  |
| Menambahkan rute graph                   | Adjacency List               | O(1)                                  |
| Mencari lokasi tidak terjangkau          | BFS                          | O(V + E)                              |
| Mencari rute optimal                     | Dijkstra                     | O(V² + E)                             |
| Menampilkan laporan lokasi               | Inorder Traversal BST        | O(n)                                  |

## Keterangan

* `n` = jumlah data lokasi
* `V` = jumlah vertex/lokasi pada graph
* `E` = jumlah edge/rute pada graph

```
```

# Requirement

Pastikan Python sudah terinstall.

Cek versi python dengan:

```bash
python --version
```

Versi yang disarankan:

```bash
Python 3.10+
```

Library yang digunakan:

```bash
numpy
```

Install numpy dengan:

```bash
pip install numpy
```

---

# Cara Menjalankan Program

1. Clone repository

```bash
git clone https://github.com/muhammadyaafi/tbp-asd-disaster-kel04.git
```

2. Masuk ke folder project

```bash
cd tbp-asd-disaster-kel04
```

3. Jalankan program main

```bash
python main.py
```

---

# Cara Menggunakan Sistem

Setelah program berjalan, masukkan command pada terminal.

Program akan menampilkan:

```text
Disaster Response Logistics System | Ketik BANTUAN untuk daftar perintah
```

---

# Daftar Command

## 1. KIRIM

Menambahkan bantuan ke antrian prioritas.

Format:

```text
KIRIM <depot> <lokasi> <jenis> <jumlah>
```

Contoh:

```text
KIRIM DEPOT_0 L001 MAKANAN 650
```

---

## 2. PROSES_BANTUAN

Memproses bantuan dengan prioritas tertinggi.

Format:

```text
PROSES_BANTUAN
```

---

## 3. RUTE_OPTIMAL

Mencari jalur tercepat menggunakan algoritma Dijkstra.

Format:

```text
RUTE_OPTIMAL <depot> <tujuan>
```

Contoh:

```text
RUTE_OPTIMAL DEPOT_1 L015
```

---

## 4. UPDATE_LEVEL

Mengubah tingkat bencana suatu lokasi.

Level:

* 1 = KRITIS
* 2 = SEDANG
* 3 = RINGAN

Format:

```text
UPDATE_LEVEL <kode_lokasi> <level>
```

Contoh:

```text
UPDATE_LEVEL L010 1
```

---

## 5. TIDAK_TERJANGKAU

Menampilkan lokasi yang tidak dapat dijangkau dari depot tertentu menggunakan BFS.

Format:

```text
TIDAK_TERJANGKAU <depot>
```

Contoh:

```text
TIDAK_TERJANGKAU DEPOT_0
```

---

## 6. LOG_PENGIRIMAN

Menampilkan riwayat pengiriman bantuan.

Format:

```text
LOG_PENGIRIMAN
```

---

## 7. LAPORAN_BENCANA

Menampilkan seluruh data lokasi bencana.

Format:

```text
LAPORAN_BENCANA
```

---

## 8. BANTUAN

Menampilkan daftar command yang tersedia.

Format:

```text
BANTUAN
```

---

## 9. KELUAR

Keluar dari program.

Format:

```text
KELUAR
```

---

# Contoh Penggunaan

```text
>> KIRIM DEPOT_0 L001 MAKANAN 20

>> KIRIM DEPOT_1 L010 AIR 50

>> PROSES_BANTUAN

>> RUTE_OPTIMAL DEPOT_0 L010

>> LOG_PENGIRIMAN

>> KELUAR
```

---

# Author & Pembagian Modul

Raihan (25051030017) : stack log pengiriman

Ya'afi (25051030029) : graph & dijkstra, main loop CLI

Hafidh (25051030032) : priority queue bantuan

Nafif  (25051030036) : bst registry lokasi
