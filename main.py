import os  # Mengimpor modul os untuk interaksi dengan sistem operasi
import subprocess  # Mengimpor modul subprocess untuk menjalankan perintah shell
import platform  # Mengimpor modul platform untuk mendapatkan informasi sistem operasi
from colorama import *  # Mengimpor modul colorama untuk penataan warna output

# Membuat alias untuk warna-warna yang akan digunakan
m = Fore.LIGHTRED_EX # Merah terang
h = Fore.LIGHTGREEN_EX  # Hijau terang
r = Style.RESET_ALL  # Me-reset warna
b = Fore.LIGHTBLUE_EX  # Biru terang
k = Fore.LIGHTYELLOW_EX  # Kuning terang

# Mengecek apakah sistem operasi yang digunakan adalah Windows
if platform.system() != 'Windows':
    print(f"{m}Error{r}: Program ini hanya dapat dijalankan di sistem operasi Windows.")
    exit()

# Membersihkan layar
os.system("cls")

print(f"""
+------------------------------------------------------------------------------------+
|                                                                                    |
| {k}Peringatan{r}: Penggunaan program ini tanpa izin adalah ilegal dan melanggar privasi. |
| Pembuat program (Rofidoang03) tidak bertanggung jawab atas penggunaan yang salah.  |
| Pastikan Anda memiliki izin resmi sebelum menggunakan program ini.                 |
|                                                                                    |
+------------------------------------------------------------------------------------+
""")

input("Tekan [Enter] untuk melanjutkan...")

# Membersihkan layar dan menetapkan judul program
os.system("cls")
os.system("title TSKSW")

# Menjalankan perintah netsh untuk menampilkan semua profil WiFi
keluaran = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode("utf-8")

# Membuat daftar kosong untuk menyimpan profil WiFi
profil_wifi = []

# Memproses keluaran untuk mendapatkan nama semua profil WiFi
for baris in keluaran.splitlines():
    if "All User Profile" in baris:
        profil = {"nama": baris.split(":")[1].strip()}  # Ekstrak nama profil WiFi
        profil_wifi.append(profil)

# Membuat daftar kosong untuk menyimpan informasi WiFi beserta kata sandinya
data_wifi = []

# Mengambil kata sandi untuk setiap profil WiFi
for profil in profil_wifi:
    keluaran = subprocess.run(["netsh", "wlan", "show", "profiles", profil["nama"], "key=clear"], capture_output=True).stdout.decode("utf-8")
    if "Key Content" in keluaran:
        info_wifi = {"Jaringan WI-FI": profil["nama"], "Kata sandi": keluaran.split(":")[1].strip()}  # Ekstrak kata sandi WiFi
        data_wifi.append(info_wifi)

# Menampilkan hasil dalam format tabel
print(f"{r}-" * 57)
print(f"     {h}No.".ljust(8) + "     Jaringan WI-FI".ljust(29) + "Kata sandi")
print(f"{r}-" * 57)

for i, data in enumerate(data_wifi, 1):
    print(f"     {str(i)}".ljust(13) + data['Jaringan WI-FI'].ljust(24) + data['Kata sandi'])

print("-" * 57)

# Menampilkan informasi tambahan berupa link ke repository GitHub pembuat program
print(f"                     {b}https://github.com/rofidoang03/TSKSW{r}")
print(f"{r}-" * 57)
