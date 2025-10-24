from database import Base
from sqlalchemy import (String, Integer, Column, DateTime, ForeignKey)
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    birthday = Column(String)
    city = Column(String)
    reg_date = Column(DateTime, default=datetime.now())

    post_fk = relationship("UserPost",
                           back_populates="user_fk",
                           cascade="all, delete-orphan")
    comment_fk = relationship("Comment", back_populates="user_fk", cascade="all, delete-orphan")


class UserPost(Base):
    __tablename__ = "posts"

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String, nullable=False)
    main_text = Column(String, nullable=False)
    uid = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    reg_date = Column(DateTime, default=datetime.now())

    user_fk = relationship("User", back_populates="post_fk",
                           lazy="joined")
    photo_fk = relationship("PostPhoto", back_populates="post_fk", cascade="all, delete-orphan")
    comment_fk = relationship("Comment", back_populates="post_fk", cascade="all, delete-orphan")


class PostPhoto(Base):
    __tablename__ = "photos"

    id = Column(Integer, autoincrement=True, primary_key=True)
    photo_path = Column(String, nullable=False)
    pid = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"))
    reg_date = Column(DateTime, default=datetime.now())

    post_fk = relationship("UserPost", back_populates="photo_fk", lazy="joined")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, autoincrement=True, primary_key=True)
    uid = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    text = Column(String, nullable=False)
    pid = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"))
    reg_date = Column(DateTime, default=datetime.now())

    user_fk = relationship("User", back_populates="comment_fk",
                           lazy="joined")
    post_fk = relationship("UserPost", back_populates="comment_fk", lazy="joined")


