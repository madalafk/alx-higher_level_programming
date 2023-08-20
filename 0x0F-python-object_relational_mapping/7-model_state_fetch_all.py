#!/usr/bin/python3
""" Listing all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    mysql = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database_name)
    engine = create_engine(mysql)
    Session = sessionmaker(bind=engine)
    session = Session()

    for item in session.query(State).order_by(State.id):
        print("{:d}: {:s}".format(item.id, item.name))

    session.close()

if __name__ == "__main__":
    main()
