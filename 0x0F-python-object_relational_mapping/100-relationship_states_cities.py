# 100-relationship_states_cities.py

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

def create_state_with_city(username, password, db_name):
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name='California')
    san_francisco = City(name='San Francisco', state=california)
    session.add(california)
    session.add(san_francisco)
    session.commit()
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 100-relationship_states_cities.py <username> <password> <db_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1:]
    create_state_with_city(username, password, db_name)
