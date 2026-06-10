from sqlalchemy.orm import Session

from app.models.user import User

from app.schemas.user_schema import UserCreate

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def register_user(
        user: UserCreate,
        db: Session
):

    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:
        return None

    db_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def login_user(
        email: str,
        password: str,
        db: Session
):

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        return None

    if not verify_password(
            password,
            user.password
    ):
        return None

    token = create_access_token(
        {
            "sub": user.email,
            "role": user.role
        }
    )

    return token