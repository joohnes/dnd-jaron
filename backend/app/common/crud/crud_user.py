from models.user import User
from sqlalchemy.orm import Session


from common.helpers import check_if_username_is_taken
from common.auth import get_password_hash



class CRUDUser:
    def get_by_id(self, db: Session, user_id: int) -> User:
        return db.query(User).filter(User.id == user_id).first()
    
    def create(self, db: Session, user_in: UserCreate):
        check_if_username_is_taken(db, user_in.username)

        # Creating admin user
        data = user_in.dict()
        data.pop("password")
        db_user = User(**data)
        db_user.hashed_password = get_password_hash(user_in.password)
        db_user.is_admin = True

        db.add(db_user)
        db.flush()
        # Adding user id to parent_user id
        db_user.parent_user = db_user.id
        db.add(db_user)
        db.commit()

        return 