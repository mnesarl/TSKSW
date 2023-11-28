import os
import subprocess

os.system("cls")
output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode("utf-8")
profiles = []

for line in output.splitlines():
    if "All User Profile" in line:
        profile = {}
        profile["name"] = line.split(":")[1].strip()
        profiles.append(profile)

wifi_data = []

for profile in profiles:
    output = subprocess.run(["netsh", "wlan", "show", "profiles", profile["name"], "key=clear"], capture_output=True).stdout.decode("utf-8")
    if "Key Content" in output:
        wifi_info = {"Jaringan WI-FI": profile["name"], "Kata sandi": ""}
        password = [line.split(":")[1].strip() for line in output.splitlines() if "Key Content" in line][0]
        wifi_info["Kata sandi"] = password
        wifi_data.append(wifi_info)

print("-" * 50)
print("Jaringan WI-FI".ljust(25) + "Kata sandi")
print("-" * 50)
for data in wifi_data:
    print(data["Jaringan WI-FI"].ljust(25) + data["Kata sandi"])
print("-" * 50)
