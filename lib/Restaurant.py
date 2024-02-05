import os
import sys
sys.path.append(os.getcwd())

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Relationships
    reviews = relationship('Review', back_populates='restaurant')

    def reviews(self):
        # Return a collection of all the reviews for the Restaurant
        return self.reviews

    def customers(self):
        # Return a collection of all the customers who reviewed the Restaurant
        return [review.customer for review in self.reviews]