from fastapi import HTTPException
from fastapi import status



def user_username_exists() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="User with that username already exists",
    )