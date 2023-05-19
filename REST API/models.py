from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column 

class Base(DeclarativeBase):
    pass

class Cafe(Base):
    __tablename__ = "cafe"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=True)
    map_url: Mapped[str] = mapped_column(String(500), nullable=True)
    img_url: Mapped[str] = mapped_column(String(500), nullable=True)
    location: Mapped[str] = mapped_column(String(250), nullable=True)
    seats: Mapped[str] = mapped_column(String(250), nullable=True)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=True)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=True)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=True)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=True)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    
    def __repr__(self):
        return   f"name: {self.name}\nmap_ur: {self.map_url}\nimg_url: {self.img_url}\nlocation: {self.location}\nseats: {self.seats}\nhas_toilet: {self.has_toilet}\nhas_wifi: {self.has_wifi}\nhas_sockets: {self.has_sockets}\ncan_take_calls: {self.can_take_calls}\ncoffee_price: {self.coffee_price}"
