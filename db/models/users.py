# import bcrypt
# import jwt
# from sqlalchemy import Integer, Column, String, Boolean, LargeBinary, UniqueConstraint, PrimaryKeyConstraint
#
# from db.config import Base, SECRET_KEY
#
#
# class NewUser(Base):
#     """Models a user table"""
#     __tablename__ = "new_user"
#     email = Column(String(225), nullable=False, unique=True)
#     id = Column(Integer, nullable=False, primary_key=True)
#     hashed_password = Column(LargeBinary, nullable=False)
#     full_name = Column(String(225), nullable=False)
#     is_active = Column(Boolean, default=False)
#
#     UniqueConstraint("email", name="uq_user_email")
#     PrimaryKeyConstraint("id", name="pk_user_id")
#
#     def __repr__(self):
#         """Returns string representation of model instance"""
#         return "<User {full_name!r}>".format(full_name=self.full_name)
#
#     @staticmethod
#     def hash_password(password) -> bytes:
#         return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
#
#     def validate_password(self, password) -> bool:
#         """Confirms password validity"""
#         return bcrypt.checkpw(password.encode(), self.hashed_password)
#
#     def generate_token(self) -> dict:
#         """Generate access token for user"""
#         return {
#             "access_token": jwt.encode(
#                 {"full_name": self.full_name, "email": self.email},
#                 SECRET_KEY
#             )
#         }
