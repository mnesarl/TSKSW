import subprocess

def get_wifi_profiles():
  """
  Mendapatkan daftar profil WiFi yang pernah terhubung.

  Returns:
    List of dictionary, berisi informasi profil WiFi.
  """

  output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode("utf-8")
  profiles = []
  for line in output.splitlines():
    if "Profile" in line:
      profile = {}
      profile["name"] = line.split(":")[1].strip()
      profiles.append(profile)
  return profiles

def get_wifi_password(profile_name):
  """
  Mendapatkan password WiFi dari profil tertentu.

  Args:
    profile_name: Nama profil WiFi.

  Returns:
    Password WiFi, jika ada.
  """

  output = subprocess.run(["netsh", "wlan", "show", "profiles", profile_name, "key=clear"], capture_output=True).stdout.decode("utf-8")
  for line in output.splitlines():
    if "Key Content" in line:
      return line.split(":")[1].strip()
  return None

def main():
  """
  Menjalankan program.
  """

  profiles = get_wifi_profiles()
  for profile in profiles:
    password = get_wifi_password(profile["name"])
    if password:
      print(f"{profile['name']}: {password}")

if __name__ == "__main__":
  main()
