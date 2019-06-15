import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BatchJob(Base):
    __tablename__ = 'batch_jobs'

    id = Column(String, primary_key=True)
    remote = Column(String)
    status = Column(String)
    config = Column(JSONB)
