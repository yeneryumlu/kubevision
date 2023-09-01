from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import utils.constants as c

engine = create_engine(
    f'postgresql://{c.POSTGRESQL_USERNAME}:{c.POSTGRESQL_PASSWORD}@{c.POSTGRESQL_HOSTNAME}:{c.POSTGRESQL_PORT}/{c.POSTGRESQL_DB}')
# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory():
    if(c.DB_DROP_ALL == 'True'):
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return _SessionFactory()
