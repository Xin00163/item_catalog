import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Ingredient(Base):
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name
        }


class RecipeItem(Base):
    __tablename__ = 'recipe_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    method = Column(String(250))
    tips = Column(String(8))
    ingredient_id = Column(Integer, ForeignKey('ingredient.id'))
    ingredient = relationship(Ingredient)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'method': self.method,
            'tips': self.tips
        }


engine = create_engine('sqlite:///ingredientrecipe.db')


Base.metadata.create_all(engine)
