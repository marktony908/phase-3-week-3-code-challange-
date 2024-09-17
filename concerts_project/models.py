from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hometown = Column(String)
    concerts = relationship('Concert', backref='band')

    def concerts(self):
        return self.concerts

    def venues(self):
        return [concert.venue for concert in self.concerts]

    @classmethod
    def most_performances(cls, session):
        return session.query(cls).order_by(cls.concerts.desc()).first()

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    city = Column(String)
    concerts = relationship('Concert', backref='venue')

    def concerts(self):
        return self.concerts

    def bands(self):
        return [concert.band for concert in self.concerts]

class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
