import os

class Config:
    """
    Konfigurasi aplikasi Flask
    """

    # Mengambil konfigurasi dari Vercel, jika tidak ada akan memakai "localhost" (untuk tes di komputer)
    HOST = os.getenv("DB_HOST", "localhost")
    PORT = int(os.getenv("DB_PORT", 3306))
    USER = os.getenv("DB_USER", "root")
    PASSWORD = os.getenv("DB_PASSWORD", "root")
    DATABASE = os.getenv("DB_NAME", "db_akademik")

    # Secret Key Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "praktikum-flask-2026")

    # Konfigurasi Flask
    DEBUG = os.getenv("FLASK_DEBUG", "True") == "True"
