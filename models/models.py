from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

engine = create_engine('sqlite:///test.db', echo=True)
session = sessionmaker(bind=engine)()
Base = declarative_base()

class Config(Base):

    __tablename__ = 'config'

    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    offDelay = Column(Integer, nullable=False, default=0)
    onAdvance = Column(Integer, nullable=False, default=0)
    url = Column(String, nullable=False)
    apiKey = Column(String, nullable=False)

    def __init__(self, offDelay, onAdvance, url, apiKey):
        self.offDelay = offDelay
        self.onAdvance = onAdvance
        self.url = url
        self.apiKey = apiKey

    def __repr__(self):
        return f'Config(offDelay:{self.offDelay}, onAdvance:{self.onAdvance}, url:{self.url}, apiKey:{self.apiKey})'

class Timer(Base):
    __tablename__ = 'timer'
    
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    checkedTime = Column(DateTime, nullable=False)
    sunriseUnix = Column(Integer, nullable=False)
    sunsetUnix = Column(Integer, nullable=False)

    def __init__(self, checkTime, sunriseUnix, sunsetUnix):
        self.checkedTime = checkTime
        self.sunriseUnix = sunriseUnix
        self.sunsetUnix = sunsetUnix

    def __repr__(self):
        return {'checkedTimer':self.checkedTime, 'surnriseUnix':self.sunriseUnix, 'sunsetUnix':self.sunsetUnix}
        
Base.metadata.create_all(engine)