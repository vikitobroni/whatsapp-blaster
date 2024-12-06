# WhatsApp Message Blaster

Proyek ini mengotomatisasi proses pengiriman pesan ke banyak penerima di WhatsApp menggunakan Selenium dan data dari file Excel. Ini memberikan cara yang efisien untuk menangani pengiriman pesan WhatsApp tanpa mengetik setiap pesan secara manual.

---

## Fitur

- Membaca nomor telepon dan pesan dari file Excel.
- Mengirim pesan yang dipersonalisasi ke setiap penerima melalui WhatsApp Web.
- Secara otomatis berinteraksi dengan antarmuka WhatsApp Web menggunakan Selenium.

---

## Prasyarat

### 1. **Dependensi**

Pastikan perangkat lunak dan pustaka berikut telah terinstal:

- **Python 3.7+**
- **Google Chrome Browser**
- **ChromeDriver** (sesuaikan dengan versi Chrome Anda)
- Pustaka Python:
  - `selenium`
  - `openpyxl`

### 2. **Setup ChromeDriver**

- Unduh ChromeDriver: [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/).
- Tempatkan file `chromedriver.exe` di direktori proyek atau lokasi yang telah ditentukan di PATH sistem Anda.

---

## Instalasi

1. Clone repositori ini atau unduh kode.

   ```bash
   git clone https://github.com/vikitobroni/whatsapp-blaster.git
   ```

2. Instal pustaka Python yang diperlukan menggunakan `requirements.txt` yang disediakan:
   ```bash
   pip install -r requirements.txt
   ```

---

## Penggunaan

### 1. **Persiapkan File Excel**

- Pastikan file Excel (misalnya, `dataCustomer.xlsx`) berada di direktori proyek.
- File Excel harus memiliki struktur berikut:

| **Nomor Telepon** | **Pesan**                |
| ----------------- | ------------------------ |
| 6281234567890     | Halo, apa kabar?         |
| 6289876543210     | Pesanan Anda sudah siap! |

- Simpan file dengan nama `dataCustomer.xlsx` atau perbarui nama file di kode pada variabel `EXCEL_FILE`.

### 2. **Jalankan Script**

- Eksekusi script Python:
  ```bash
  python main.py
  ```
- Browser Chrome akan terbuka, dan Anda akan diminta untuk memindai kode QR WhatsApp Web.
- Script akan secara otomatis mengirim pesan ke nomor yang tercantum.

---

## Penjelasan Kode

### Komponen Utama

1. **Membaca Data Excel**:

   - Fungsi `read_excel()` membaca nomor telepon dan pesan dari file Excel yang ditentukan.

2. **Mengirim Pesan WhatsApp**:

   - Fungsi `send_whatsapp_message()` menavigasi ke WhatsApp Web, memasukkan nomor telepon, mengisi pesan secara otomatis, dan mengirimnya.

3. **Eksekusi Script**:
   - Fungsi `main()` menangani alur eksekusi, termasuk inisialisasi ChromeDriver dan pengiriman pesan secara berurutan.

### Variabel Utama

- `EXCEL_FILE`: Path ke file Excel.
- `driver_path`: Path ke `chromedriver.exe`.

---

## Catatan

- Pastikan semua nomor telepon menggunakan format internasional yang benar (misalnya, `6281234567890` untuk Indonesia).
- Hindari menggunakan script ini untuk tujuan spam agar mematuhi ketentuan layanan WhatsApp.

---

## Pemecahan Masalah

### Masalah Umum

1. **`FileNotFoundError`: File Excel tidak ditemukan**:

   - Pastikan file Excel berada di path yang ditentukan.
   - Verifikasi nama file sesuai dengan nilai variabel `EXCEL_FILE` dalam script.

2. **Timeout Pemindaian QR Code**:

   - Tingkatkan waktu tunggu pada baris `time.sleep(20)` di fungsi `main()`.

3. **Versi ChromeDriver Tidak Cocok**:
   - Pastikan versi ChromeDriver sesuai dengan versi browser Chrome Anda.
   - Perbarui ChromeDriver jika diperlukan.

---

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Gunakan dengan bijak dan patuhi semua peraturan serta ketentuan layanan yang berlaku.

---

## Penulis

Dikembangkan oleh vikitobroni.
