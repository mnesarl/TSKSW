import os

def extract_wifi_passwords():
    try:
        # Get the list of saved Wi-Fi profiles
        profiles = os.popen('netsh wlan show profiles').read()
        profile_names = [i.split(":")[1].strip() for i in profiles if "All User Profile" in i]

        # Extract the passwords for each profile
        for profile_name in profile_names:
            password_info = os.popen(f'netsh wlan show profile "{profile_name}" key=clear').read()
            password = [line.split(":")[1].strip() for line in password_info.split('\n') if "Key Content" in line]
            
            if password:
                print(f"Wi-Fi Network: {profile_name}")
                print(f"Password: {password[0]}")
                print("")

    except Exception as e:
        print(f"Oops! Something went wrong: {str(e)}")

# Call the function to extract Wi-Fi passwords
extract_wifi_passwords()
