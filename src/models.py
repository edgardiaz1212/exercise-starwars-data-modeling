import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__='user'
    id=Column(Integer, primary_key=True)
    name=Column(String(80), nullable=False)
    created=Column(String(50))

class Favorites(Base):
    __tablename__='favorites'
    id=Column(Integer, primary_key=True)


class Character(Base):
    __tablename__='character'
    id=Column(Integer, primary_key=True)
    name=Column(String(250),nullable=False)
    height=Column(Integer)
    mass=Column(Integer)
    hair_color=(String(30))
    skin_color=(String(30))
    eye_color=(String(30))
    birth_year=()
    gender=Column(String(40))
    homeworld=Column(String(50))
    films=Column(String(60))
    species=Column(String(60))
    vehicles=Column(String(60))
    starships=Column(String(60))
    created=Column(String(60))
    edited=Column(String(60))
    url=Column(String(60))

class Planets(Base):
    __tablename__='planets'
    id=Column(Integer, primary_key=True)
    name=Column(String(250),nullable=False)
    rotation_period=Column(Integer)
    orbital_period=Column(Integer)
    diameter=Column(Integer)
    climate=Column(String(60))
    gravity=Column(String(60))
    terrain=Column(String(100))
    surface_water=Column(Integer)
    population=Column(Integer)
    residents=Column(String(100))
    films=Column(String(100))
    created=Column(String(100))
    edited=Column(String(100))
    url=Column(String(100))





# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
