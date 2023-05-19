from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column 


class Base(DeclarativeBase):
    pass

class TopMovies(Base):
    __tablename__ = "movies"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    year: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    review: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    rating: Mapped[int] = mapped_column(String, nullable=True, unique=False)
    description: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    image: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    
    
engine =create_engine('sqlite:///day_64_TopMovies/database.db')
Base.metadata.create_all(engine)


def add_movie(title, year, review, rating, description, image):
    with Session(engine) as session:
        new_movie = TopMovies(title=title, year=year, review=review, rating=rating, description=description, image=image)
        session.add(new_movie)
        session.commit()
        
def change_data(title, review, rating, year):
    with Session(engine) as session:
        movie = session.query(TopMovies).filter_by(title=title).filter_by(year=year).first()
        movie.review = review
        movie.rating = rating
        session.commit()
        
def delete_movie(title, year):
    with Session(engine) as session:
        movie = session.query(TopMovies).filter_by(title=title).filter_by(year=year).first()
        session.delete(movie)
        session.commit()
        
def get_movies():
    with Session(engine) as session:
        return session.query(TopMovies).order_by(TopMovies.rating)
    
def get_list_length():
    with Session(engine) as session:
        return len(session.query(TopMovies).all())
    
