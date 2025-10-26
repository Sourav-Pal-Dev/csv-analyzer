from decouple import config, Csv

# === Django core settings ===
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# === Database ===
DATABASE_URL = config("DATABASE_URL")

# === Google Drive ===
GOOGLE_SERVICE_ACCOUNT = config("GOOGLE_SERVICE_ACCOUNT")
GOOGLE_FOLDER_ID = config("GOOGLE_FOLDER_ID", default=None)