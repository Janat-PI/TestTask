from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry

from DB.shemas import Base, Test


def get_session(bind):
    Session = sessionmaker(bind=bind)
    session = Session()
    return session

def get_engine(url: str):
    engine = create_engine(url=url,
    echo=True, 
    future=True
    )
    return engine

def main(get_session_: bool=False):
    URL = 'postgresql://zhanat:1@localhost/sheets'
    engine = get_engine(URL)
    session = get_session(engine)
    if get_session_:
        return session
    # Base.metadata.create_all(engine_)



if __name__ == "__main__":
    main()