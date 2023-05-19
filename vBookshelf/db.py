from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass

class Bookshelf(Base):   
    __tablename__ = "books"  
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(50), nullable=False)
    rating: Mapped[str] = mapped_column(nullable=False)


engine = create_engine('sqlite:///day_63_vBookshelf/bookshelf.db')
Base.metadata.create_all(engine)


def insert_row(title, author, rating):
    with Session(engine) as session:
        new_book = Bookshelf(title=title, author=author, rating=rating)
        session.add(new_book)
        session.commit()
        
        
def change_rating(title, rating):
    with Session(engine) as session:
        book = session.query(Bookshelf).filter_by(title=title).first()
        book.rating = rating
        session.commit()
        
        
def delete_row(title):
    with Session(engine) as session:
        book = session.query(Bookshelf).filter_by(title=title).first()
        session.delete(book)
        session.commit()


def titles():
    with Session(engine) as session:
        return [i.title for i in session.scalars(select(Bookshelf))]
    
def authors():
    with Session(engine) as session:
        return [i.author for i in session.scalars(select(Bookshelf))]
    
def ratings():
    with Session(engine) as session:
        return [i.rating for i in session.scalars(select(Bookshelf))]