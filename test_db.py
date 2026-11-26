
from sqlalchemy import text
from app import create_app
from app.config.database import db

app = create_app()

with app.app_context():
    try:
        result = db.session.execute(
            text("SELECT current_database()")
        ).scalar()

        print("Koneksi PostgreSQL berhasil!")
        print(f"Database aktif: {result}")

    except Exception as e:
        print("Koneksi PostgreSQL gagal!")
        print(e)

    finally:
        db.session.remove()
