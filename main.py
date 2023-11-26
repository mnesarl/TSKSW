import subprocess

def extract_wifi_passwords():
    try:
        # Get the list of saved Wi-Fi profiles
        command_output = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
        profile_names = [line.split(":")[1].strip() for line in command_output if "All User Profile" in line]

        # Extract the passwords for each profile
        for profile_name in profile_names:
            profile_info = subprocess.check_output(["netsh", "wlan", "show", "profile", profile_name, "key=clear"]).decode("utf-8").split("\n")
            password_line = [line.split(":")[1].strip() for line in profile_info if "Key Content" in line]
            
            if password_line:
                print(f"Wi-Fi Network: {profile_name}")
                print(f"Password: {password_line[0]}")
                print("")

    except Exception as e:
        print(f"Oops! Something went wrong: {str(e)}")

# Call the function to extract Wi-Fi passwords
extract_wifi_passwords()
