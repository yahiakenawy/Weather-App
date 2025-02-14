# models.py
import datetime
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from Config import DATABASE_URI

Base = declarative_base()

class EnvironmentData(Base):
    __tablename__ = 'environment_data'
    id = Column(Integer, primary_key=True)
    temperature = Column(Float)
    humidity = Column(Integer)
    pressure = Column(Integer)
    weather_description = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

def init_db():
    engine = create_engine(DATABASE_URI)
    Base.metadata.create_all(engine)
    return engine

if __name__ == "__main__":
    engine = init_db()
    print("Database initialized.")
