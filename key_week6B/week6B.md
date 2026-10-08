# Praktikum Streamlit — Site Tugas

## Deskripsi

Buat sebuah aplikasi web sederhana menggunakan **Streamlit** dengan tema **Site Tugas**.

Aplikasi memiliki dua jenis pengguna:

1. **Murid**
2. **Dosen**

Pengguna harus melakukan login terlebih dahulu sebelum dapat menggunakan aplikasi.

---

## Hak Akses

### Murid

Murid hanya dapat:

* Melihat daftar tugas
* Mencari tugas
* Mengurutkan tugas secara ascending
* Mengurutkan tugas secara descending
* Logout

Murid **tidak dapat**:

* Menambah tugas
* Mengedit tugas

### Dosen

Dosen dapat:

* Melihat daftar tugas
* Mencari tugas
* Mengurutkan tugas secara ascending
* Mengurutkan tugas secara descending
* Menambah tugas
* Mengedit tugas
* Logout

---

# Login

Gunakan akun berikut untuk melakukan pengujian.

| Role  | Username | Password |
| ----- | -------- | -------- |
| Murid | `murid`  | `123`    |
| Dosen | `dosen`  | `123`    |

Jika username atau password salah, tampilkan pesan:

```text
Username atau password salah
```

---

# Data Tugas

Setiap tugas memiliki empat data:

```text
id
judul
mata_kuliah
deadline
```

Contoh:

```python
{
    "id": 1,
    "judul": "Tugas Python",
    "mata_kuliah": "Pemrograman",
    "deadline": "2026-10-10"
}
```

Data tugas disimpan dalam bentuk **list of dictionary**.

---

# Fitur yang Harus Dibuat

## 1. Login

Buat halaman login menggunakan Streamlit.

Login harus:

* menerima username
* menerima password
* mengecek data login
* menentukan role pengguna
* menyimpan status login menggunakan `st.session_state`

---

## 2. Daftar Tugas

Setelah berhasil login, pengguna dapat melihat daftar tugas.

Setiap tugas minimal menampilkan:

* Judul
* Mata kuliah
* Deadline

---

## 3. Search

Sediakan input:

```text
🔍 Cari tugas
```

Search dapat mencari berdasarkan:

* Judul tugas
* Mata kuliah

Search bersifat **case-insensitive**.

Contoh:

Jika pengguna mencari:

```text
python
```

maka:

```text
Tugas Python
```

dapat ditemukan.

---

## 4. Sorting

Sediakan pilihan:

```text
Default
Ascending
Descending
```

Sorting dilakukan berdasarkan **deadline**.

### Ascending

```text
2026-10-10
2026-10-12
2026-10-15
```

### Descending

```text
2026-10-15
2026-10-12
2026-10-10
```

Gunakan fungsi `sorted()`.

---

## 5. Tambah Tugas

Fitur ini hanya dapat digunakan oleh **dosen**.

Dosen dapat memasukkan:

* Judul tugas
* Mata kuliah
* Deadline

Ketika tombol `Tambah` ditekan, data baru harus dimasukkan ke daftar tugas.

---

## 6. Edit Tugas

Fitur ini hanya dapat digunakan oleh **dosen**.

Setiap tugas yang ditampilkan untuk dosen memiliki tombol:

```text
Edit
```

Ketika tombol tersebut ditekan:

1. Tampilkan form edit.
2. Tampilkan data lama sebagai nilai awal.
3. Dosen dapat mengubah judul.
4. Dosen dapat mengubah mata kuliah.
5. Dosen dapat mengubah deadline.
6. Sediakan tombol `Simpan Perubahan`.
7. Sediakan tombol `Batal`.

---

## 7. Logout

Sediakan tombol:

```text
Logout
```

Ketika logout dilakukan:

* status login menjadi `False`
* role di-reset
* pengguna kembali ke halaman login

---

# Struktur File

Gunakan struktur:

```text
site_tugas/
│
├── app.py
├── login.py
├── data.py
├── tugas.py
└── requirements.txt
```

### `app.py`

Berfungsi sebagai file utama aplikasi.

Mengatur:

* session state
* login
* menu
* logout
* role pengguna

### `login.py`

Berisi fungsi:

```python
login()
```

yang menangani proses login.

### `data.py`

Berisi data awal tugas melalui:

```python
get_data_tugas()
```

### `tugas.py`

Berisi:

```python
tampilkan_tugas()
tambah_tugas()
edit_tugas()
```

---

# Ketentuan Teknis

Gunakan:

* Python
* Streamlit
* `st.session_state`
* List
* Dictionary
* `if / elif / else`
* `for`
* List comprehension
* `sorted()`
* `st.text_input()`
* `st.button()`
* `st.selectbox()`
* `st.date_input()`

Tidak perlu menggunakan:

* Database
* Class
* Framework lain

---

# Petunjuk Pengerjaan

Starter code telah disediakan.

**Jangan menghapus seluruh kode yang telah diberikan.**

Lengkapi bagian yang diberi:

```python
# TODO
```

Ikuti petunjuk:

```python
# STEP 1
# STEP 2
# STEP 3
```

Kerjakan secara bertahap.

---

# Cara Menjalankan

Install Streamlit:

```bash
pip install -r requirements.txt
```

Kemudian jalankan:

```bash
streamlit run app.py
```

---

# Kriteria Program Berhasil

Program harus memenuhi:

* [ ] Login murid berhasil
* [ ] Login dosen berhasil
* [ ] Login salah menampilkan error
* [ ] Daftar tugas ditampilkan
* [ ] Search bekerja
* [ ] Search tidak case-sensitive
* [ ] Ascending bekerja
* [ ] Descending bekerja
* [ ] Murid tidak dapat menambah tugas
* [ ] Murid tidak dapat mengedit tugas
* [ ] Dosen dapat menambah tugas
* [ ] Dosen dapat mengedit tugas
* [ ] Tombol batal edit bekerja
* [ ] Logout bekerja
* [ ] Program tidak menghasilkan error saat digunakan

---

# Catatan

Data tugas disimpan menggunakan:

```python
st.session_state
```

sehingga data hanya digunakan selama aplikasi berjalan.

Tidak diperlukan database untuk praktikum ini.

Fokus praktikum adalah memahami:

* Streamlit
* Session State
* Role-based access
* Filtering
* Sorting
* Manipulasi list dan dictionary
