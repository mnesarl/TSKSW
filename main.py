# Program : Tampilkan semua kata sandi WI-FI
# Pembuat : Rofidoang03
# Github : https://github.com/rofidoang03/TSKSW

import os
import subprocess
from colorama import Fore

h = Fore.LIGHTGREEN_EX
r = Fore.RESET

os.system("cls")
os.system("title TSKSW")

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

print(f"{r}-" * 57)
print(f"     {h}No.".ljust(8) + "     Jaringan WI-FI".ljust(29) + "Kata sandi")
print(f"{r}-" * 57)

for i, data in enumerate(data_wifi, 1):
    print(f"     {str(i)}".ljust(13) + data['Jaringan WI-FI'].ljust(24) + data['Kata sandi'])

print("-" * 57)
