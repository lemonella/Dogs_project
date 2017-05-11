from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///place.sqlite')
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Place(Base):
    __tablename__ = 'place'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    address = Column(String(300))
    latitude = Column(Float)
    longitude = Column(Float)
    description = Column(String(120))

    def __repr__(self):
        return '<Место: {} {}>'.format(self.name, self.address)

'''
------
Элины классы для юзеров и инфо о бронировании кафе
------

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(150), unique=True)
    image = Column(String(500))

    def __repr__(self):
        return '<Пользователь: {} {}>'.format(self.name, self.email)


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    booked_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    place_id = Column(Integer, ForeignKey('place.id'))

    users = relationship(User)
    places = relationship(Place)

    def __repr__(self):
        return '<Брони: {} {} {}>'.format(self.user, self.place, self.date)
'''

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
