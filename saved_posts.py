import instaloader
import os

instance = instaloader.Instaloader()

session_file = "login_credentials.txt"

username = "your_username"
password = "your_password"

instance.compress_json = False

# If you don't already have a session file to upload, it logs in using your credentials
try:
    instance.load_session_from_file(username, session_file)

except FileNotFoundError:
    try:
        instance.login(username, password)

    except:
        # If login fails, it logs in using your session ID and CSRF Token (not recommended to use with VPN!!!)
        instance.load_session(username, {"sessionid": "your_sessionid", "csrftoken": "your_csrftoken"})

# Saves your credentials in a file if you want to use them later
if not session_file and instance.context.is_logged_in:
    instance.save_session_to_file(session_file)
    print(f"Logged as {username}")

else:
    print("Login failed.")

profile = instaloader.Profile.from_username(instance.context, username)

instance.download_saved_posts()