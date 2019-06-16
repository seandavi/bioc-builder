import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB

metadata = MetaData()

batch_jobs = Table("batch_jobs", metadata,
                   Column("id", String, primary_key=True),
                   Column("remote", String, ForeignKey('remotes.remote')),
                   Column("status", String),
                   Column("config", JSONB)
)

remotes = Table("remotes", metadata,
                Column("remote", String, primary_key=True)
)


def create_all(engine):
    metadata.create_all(engine)

if __name__ == '__main__':
    from starlette.config import Config
    config = Config('.env')
    from sqlalchemy import create_engine
    engine = create_engine(config('DATABASE_URL'))
    create_all(engine)
    
