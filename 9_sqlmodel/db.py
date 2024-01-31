from dotenv import load_dotenv, find_dotenv
from os import getenv
from typing import Optional
from sqlmodel import Field, SQLModel, create_engine,Session,select

_:bool = load_dotenv(find_dotenv())
postgress_url:str = getenv("POSTGRESS_URL")

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

engine = create_engine(postgress_url,echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
    hero_4 = Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32)
    hero_5 = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
    hero_6 = Hero(name="Dr. Weird", secret_name="Steve Weird", age=36)
    hero_7 = Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93)
    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.add(hero_4)
        session.add(hero_5)
        session.add(hero_6)
        session.add(hero_7)
        session.commit()

def select_heroes():
    with Session(engine) as session:
        statement = select(Hero)
        results = session.exec(statement)
        heroes = results.all()
        print(heroes)
        # for hero in results:
        #     print("=======",hero)

def select_filter_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Deadpond")
        results = session.exec(statement)
        for hero in results:
            print(hero)

def select_limited_heroes():
    with Session(engine) as session:
        statement = select(Hero).limit(3)
        results = session.exec(statement)
        heroes = results.all()
        print(heroes)

def select_offseted_heroes():
    with Session(engine) as session:
        statement = select(Hero).offset(3).limit(3)
        results = session.exec(statement)
        heroes = results.all()
        print(heroes)

def update_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        results = session.exec(statement)
        hero = results.one()
        hero.age = 16
        session.add(hero)
        session.commit()

def delete_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        results = session.exec(statement)
        hero = results.one()
        print("Hero: ", hero)
        session.delete(hero)
        session.commit()

if __name__ == "__main__":
    #  create_db_and_tables()
    #  create_heroes()
    # select_heroes()
    # select_filter_heroes()
    # select_limited_heroes()
    # select_offseted_heroes()
    # update_heroes()
    delete_heroes()