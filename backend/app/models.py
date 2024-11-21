from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class ProductCategories(Base):
    __tablename__='ProductCategories'

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(50), unique=True)

class Products(Base):
    __tablename__ = 'Products'

    product_id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer)
    product_name = Column(String(50))
    brand = Column(String(50))
    model = Column(String(50))

class Specifications_laptop(Base):
    __tablename__ = 'Specifications_laptop'

    spec_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    spec_name = Column(String(100))
    spec_value = Column(String(100))

class Specifications_smartphone(Base):
    __tablename__ = 'Specifications_smartphone'

    spec_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    spec_name = Column(String(100))
    spec_value = Column(String(100))

class Specifications_tabletpc(Base):
    __tablename__ = 'Specifications_tabletpc'

    spec_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    spec_name = Column(String(100))
    spec_value = Column(String(100))