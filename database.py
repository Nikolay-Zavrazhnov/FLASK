import atexit
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from config import PG_DSN

engine = create_engine(PG_DSN)
Base = declarative_base(bind=engine)


class OwnerModel(Base):

    __tablename__ = 'app_owner'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class AdvModel(Base):
    __tablename__ = 'app_adv'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    text = Column(Text)
    published_at = Column(DateTime,)
    user_id = Column(Integer, ForeignKey("app_owner.id", ondelete="CASCADE"))
    user = relationship('OwnerModel', lazy="joined")

Base.metadata.create_all()

Session = sessionmaker(bind=engine)

atexit.register(lambda: engine.dispose())
