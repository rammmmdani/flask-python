
import uuid

from datetime import datetime, timezone

from app.config.database import db


class User(db.Model):
    __tablename__ = "users"

    uuid = db.Column(
        db.Uuid,
        primary_key=True,
        default=uuid.uuid4
    )

    email = db.Column(
        db.String(255),
        nullable=False,
        unique=True
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    created_by = db.Column(db.Uuid, nullable=True)

    updated_at = db.Column(
        db.DateTime(timezone=True),
        nullable=True
    )

    updated_by = db.Column(db.Uuid, nullable=True)

    deleted_at = db.Column(
        db.DateTime(timezone=True),
        nullable=True
    )

    deleted_by = db.Column(db.Uuid, nullable=True)
