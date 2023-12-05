# program   : tsksw
# deskripsi : tampilan semua kata sandi wifi 
# pembuat   : rofidoang03@gmail.com
# github    : https://github.com/rofidoang03/tsksw

import os
import subprocess

os.system("cls")

keluaran = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode("utf-8")

profil_wifi = []

for baris in keluaran.splitlines():
    if "All User Profile" in baris:
        profil = {}
        profil["nama"] = baris.split(":")[1].strip()
        profil_wifi.append(profil)

data_wifi = []

for profil in profil_wifi:
    keluaran = subprocess.run(["netsh", "wlan", "show", "profiles", profil["nama"], "key=clear"], capture_output=True).stdout.decode("utf-8")
    if "Key Content" in keluaran:
        info_wifi = {"Jaringan WI-FI": profil["nama"], "Kata sandi": ""}
        sandi = [baris.split(":")[1].strip() for baris in keluaran.splitlines() if "Key Content" in baris][0]
        info_wifi["Kata sandi"] = sandi
        data_wifi.append(info_wifi)

print("-" * 50)
print("Jaringan WI-FI".ljust(25) + "Kata sandi")
print("-" * 50)

for data in data_wifi:
    print(data["Jaringan WI-FI"].ljust(25) + data["Kata sandi"])

print("-" * 50)
