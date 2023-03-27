from models.user import User
from typing import Union

from exceptions import user_username_exists


def check_if_username_is_taken(
    db, user_username, user_id=None
) -> Union[bool, Exception]:
    if not user_id:
        user = db.query(User).filter(User.username == user_username).first()
    else:
        user = (
            db.query(User)
            .filter(User.username == user_username, User.id != user_id)
            .first()
        )
    if user:
        raise user_username_exists()
    return True