import subprocess
import re

keluaran_perintah = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()
nama_profil = (re.findall("All User Profile     : (.*)\r", keluaran_perintah))

daftar_wifi = []

if len(nama_profil) != 0:
    for nama in nama_profil:
        profil_wifi = {}
        info_profil = subprocess.run(["netsh", "wlan", "show", "profile", nama], capture_output=True).stdout.decode()

        if re.search("Security key           : Absent", info_profil):
            continue
        else:
            profil_wifi["ssid"] = nama
            info_profil_kunci = subprocess.run(["netsh", "wlan", "show", "profile", nama, "key=clear"], capture_output=True).stdout.decode()
            kata_sandi = re.search("Key Content            : (.*)\r", info_profil_kunci)

            if kata_sandi is None:
                profil_wifi["password"] = None
            else:
                profil_wifi["password"] = kata_sandi[1]

            daftar_wifi.append(profil_wifi)

with open('wifi_passwords.txt', 'w') as file:
    for wifi in daftar_wifi:
        file.write(f"[+] SSID: {wifi['ssid']}, Password: {wifi['password']}\n")
