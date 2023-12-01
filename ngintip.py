import os  # Mengimpor modul os untuk mengakses fungsi-fungsi sistem operasi
import subprocess  # Mengimpor modul subprocess untuk menjalankan perintah subshell

os.system("cls")  # Membersihkan layar konsol menggunakan perintah sistem "cls" pada Windows

# Menjalankan perintah "netsh wlan show profiles" untuk menampilkan daftar profil Wi-Fi dan menyimpan keluarannya ke dalam variabel keluaran
keluaran = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode("utf-8")

profil_wifi = []  # Membuat list kosong untuk menyimpan informasi profil Wi-Fi

# Memproses setiap baris dari keluaran perintah sebelumnya untuk mengidentifikasi nama-nama profil Wi-Fi
for baris in keluaran.splitlines():
    if "All User Profile" in baris:
        profil = {}  # Membuat dictionary kosong untuk setiap profil Wi-Fi yang ditemukan
        profil["nama"] = baris.split(":")[1].strip()  # Menyimpan nama profil Wi-Fi
        profil_wifi.append(profil)  # Menambahkan informasi profil ke dalam list profil_wifi

data_wifi = []  # Membuat list kosong untuk menyimpan informasi jaringan Wi-Fi beserta kata sandinya

# Untuk setiap profil yang ditemukan, menjalankan perintah untuk mendapatkan informasi lebih lanjut tentang jaringan Wi-Fi
for profil in profil_wifi:
    keluaran = subprocess.run(["netsh", "wlan", "show", "profiles", profil["nama"], "key=clear"], capture_output=True).stdout.decode("utf-8")
    if "Key Content" in keluaran:  # Memeriksa apakah informasi kata sandi Wi-Fi tersedia
        info_wifi = {"Jaringan WI-FI": profil["nama"], "Kata sandi": ""}  # Membuat dictionary untuk menyimpan informasi jaringan Wi-Fi
        sandi = [baris.split(":")[1].strip() for baris in keluaran.splitlines() if "Key Content" in baris][0]  # Mendapatkan kata sandi Wi-Fi
        info_wifi["Kata sandi"] = sandi  # Menyimpan kata sandi Wi-Fi dalam dictionary info_wifi
        data_wifi.append(info_wifi)  # Menambahkan informasi jaringan Wi-Fi ke dalam list data_wifi

# Mencetak header tabel untuk informasi jaringan Wi-Fi dan kata sandi
print("-" * 50)
print("Jaringan WI-FI".ljust(25) + "Kata sandi")
print("-" * 50)

# Mencetak informasi jaringan Wi-Fi dan kata sandi ke layar dengan format tabel yang rapi
for data in data_wifi:
    print(data["Jaringan WI-FI"].ljust(25) + data["Kata sandi"])

# Mencetak garis putus-putus sebagai pemisah setelah selesai menampilkan informasi
print("-" * 50)
