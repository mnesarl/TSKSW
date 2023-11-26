import subprocess

output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode("utf-8")

profiles = []

for line in output.splitlines():
    if "Profile" in line:
        profile = {}
        profile["name"] = line.split(":")[1].strip()
        profiles.append(profile)

for profile in profiles:
    output = subprocess.run(["netsh", "wlan", "show", "profiles", profile["name"], "key=clear"], capture_output=True).stdout.decode("utf-8")
    for line in output.splitlines():
        if "Key Content" in line:
            password = line.split(":")[1].strip()
            if password:
                print(f"Jaringan WI-FI : {profile['name']}")
                print(f"Kata sandi : {password}")
