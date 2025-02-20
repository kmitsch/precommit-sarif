import hashlib

# Hardcoded secret (Insecure: Should be stored securely)
SECRET_KEY = "hardcoded_secret_12345678"


# Use of MD5 for hashing (Insecure: Use SHA-256 or stronger instead)
def insecure_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == "__main__":
    print("Insecure Hash:", insecure_hash("password123"))
