# Program : Tampilkan semua kata sandi WI-FI
# Pembuat : Rofidoang03
# Github : https://github.com/rofidoang03/TSKSW

# Mengimpor modul os untuk interaksi dengan sistem operasi
import os

# Mengimpor modul subprocess untuk menjalankan perintah shell
import subprocess

# Mengimpor modul colorama untuk penataan warna output
from colorama import Fore

# Membuat alias untuk warna-warna yang akan digunakan
h = Fore.LIGHTGREEN_EX  # Hijau terang
r = Fore.RESET         # Me-reset warna
b = Fore.LIGHTBLUE_EX   # Biru terang

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
        profil = {}
        profil["nama"] = baris.split(":")[1].strip()
        profil_wifi.append(profil)

# Membuat daftar kosong untuk menyimpan informasi WiFi beserta kata sandinya
data_wifi = []

# Mengambil kata sandi untuk setiap profil WiFi
for profil in profil_wifi:
    keluaran = subprocess.run(["netsh", "wlan", "show", "profiles", profil["nama"], "key=clear"], capture_output=True).stdout.decode("utf-8")
    if "Key Content" in keluaran:
        info_wifi = {"Jaringan WI-FI": profil["nama"], "Kata sandi": ""}
        sandi = [baris.split(":")[1].strip() for baris in keluaran.splitlines() if "Key Content" in baris][0]
        info_wifi["Kata sandi"] = sandi
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
