import os

print("APP_ENV =", os.getenv("APP_ENV"))
print("APP_MESSAGE =", os.getenv("APP_MESSAGE"))
print("Secret is set:", bool(os.getenv("API_KEY")))