import base64
import json
import os

DATA_FILE = "vault.json"

def encode_password(password):
    return base64.b64encode(password.encode()).decode()

def decode_password(encoded):
    return base64.b64decode(encoded.encode()).decode()

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_credential():
    site = input("Enter site name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    encoded_pass = encode_password(password)
    data = load_data()
    data[site] = {"username": username, "password": encoded_pass}
    save_data(data)
    print("✅ Credential saved successfully.")

def view_credentials():
    data = load_data()
    if not data:
        print("📭 No credentials stored yet.")
        return
    print("\n🔐 Saved Credentials:")
    for site, info in data.items():
        print(f"Site: {site}")
        print(f"Username: {info['username']}")
        print(f"Password: {decode_password(info['password'])}")
        print("-" * 30)

def menu():
    while True:
        print("\n🔐 Password Vault")
        print("1. Add new credential")
        print("2. View all credentials")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_credential()
        elif choice == '2':
            view_credentials()
        elif choice == '3':
            print("👋 Exiting Password Vault. Stay secure!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    menu()
