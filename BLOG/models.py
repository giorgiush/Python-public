from sqlalchemy import String, Integer, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from flask_login import UserMixin
from typing import List

class Base(DeclarativeBase):
    pass

class Posts(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["Users"] = relationship(back_populates="blog_posts")
    title: Mapped[str] = mapped_column(String(500), nullable=True, unique=True)
    subtitle: Mapped[str] = mapped_column(String(500), nullable=True)
    date: Mapped[str] = mapped_column(String(500), nullable=True)
    body: Mapped[Text] = mapped_column(Text, nullable=True)
    img_url: Mapped[str] = mapped_column(String(500), nullable=True)
    comments: Mapped["Comments"] = relationship(back_populates="post")
    
class Users(Base, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(500), nullable=True)
    email: Mapped[str] = mapped_column(String(500), nullable=True)
    password: Mapped[str] = mapped_column(String(500), nullable=True)
    blog_posts: Mapped[List["Posts"]] = relationship(back_populates="author")
    comments: Mapped["Comments"] = relationship(back_populates="comment_author")
    
class Comments(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[Text] = mapped_column(Text, nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    comment_author: Mapped["Users"] = relationship(back_populates="comments")
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    post: Mapped["Posts"] = relationship(back_populates="comments")