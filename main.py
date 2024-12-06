import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import openpyxl

# Path ke file Excel dan kolom data
EXCEL_FILE = "dataCustomer.xlsx"  # Sesuaikan dengan nama file
COLUMN_NUMBER = "A"  # Kolom nomor HP
COLUMN_MESSAGE = "B"  # Kolom pesan

# Fungsi untuk membaca data dari Excel
def read_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Mulai dari baris kedua (header diabaikan)
        if row[0] and row[1]:  # Pastikan nomor dan pesan tidak kosong
            data.append((str(row[0]), row[1]))
    return data

# Fungsi untuk mengirim pesan
def send_whatsapp_message(driver, number, message):
    try:
        url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
        driver.get(url)

        time.sleep(10)  # Tunggu sampai QR Code dipindai atau halaman siap

        # Klik tombol kirim jika tombol tersedia
        send_button = driver.find_element(By.XPATH, "//span[@data-icon='send']")
        send_button.click()

        time.sleep(5)  # Beri waktu untuk mengirim pesan
    except Exception as e:
        print(f"Gagal mengirim pesan ke {number}: {e}")

# Main script
def main():
    # Baca data dari Excel
    data = read_excel(EXCEL_FILE)

    # Path ke WebDriver (sesuaikan dengan lokasi Anda)
    driver_path = r"E:\whatsapp-blaster\chromedriver.exe"  # Gunakan format mentah dengan r""
    service = Service(driver_path)

    # Inisialisasi WebDriver
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    print("Silakan scan QR Code di WhatsApp Web untuk login.")
    driver.get("https://web.whatsapp.com")
    time.sleep(20)  # Tunggu sampai login selesai

    # Kirim pesan ke semua nomor
    for number, message in data:
        print(f"Mengirim pesan ke {number}...")
        send_whatsapp_message(driver, number, message)

    print("Selesai mengirim pesan.")
    driver.quit()

if __name__ == "__main__":
    main()
