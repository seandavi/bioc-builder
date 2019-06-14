import sqlalchemy
from sqlalchemy import Column, String, Integer, JSONB

class BatchJob(Base):
    __tablename__ = 'batch_jobs'

    id = Column(String, primary_key=True)
    remote = Column(String)
    status = Column(String)
    config = Column(JSONB)

