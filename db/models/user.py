import enum

from db.db_setup import Base
from db.models.mixins import Timestamp
from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class Role(enum.Enum):
    teacher: 1
    student: 2


class User(Timestamp, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String, nullable=False, unique=True)
    role = Column(Enum(Role))

    profile = relationship("Profile", back_populates="owner", uselist=False)


class Profile(Timestamp, Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text)
    is_active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="profile")
