from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

from app.config.database import db
from app.models.user import User

user_bp = Blueprint("users", __name__)


@user_bp.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({"message": "Request body harus berupa JSON"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email dan password wajib diisi"}), 400

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({"message": "Email sudah terdaftar"}), 409

    new_user = User(
        email=email,
        password=generate_password_hash(password)
    )

    try:
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "message": "User berhasil dibuat",
            "data": {
                "uuid": str(new_user.uuid),
                "email": new_user.email,
                "created_at": new_user.created_at.isoformat()
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Gagal membuat user", "error": str(e)}), 500