import os
import sys
from alembic import op
import sqlalchemy as sa
sys.path.append(os.getcwd)

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)

   
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))

    
    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')
    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant
    def upgrade():
     op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('star_rating', sa.Integer(), nullable=False),
        sa.Column('customer_id', sa.Integer(), sa.ForeignKey('customers.id'), nullable=False),
        sa.Column('restaurant_id', sa.Integer(), sa.ForeignKey('restaurants.id'), nullable=False),
    )



    def downgrade():
     op.drop_table('reviews')