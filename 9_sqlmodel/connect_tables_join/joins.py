from dotenv import load_dotenv, find_dotenv
from os import getenv
from typing import Optional
from sqlmodel import Field, SQLModel, create_engine,Session,select

_:bool = load_dotenv(find_dotenv())
postgress_url:str = getenv("POSTGRESS_URL")


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")


def create_heroes_team():
    with Session(engine) as session:
        team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret's Bar")
        session.add(team_preventers)
        session.add(team_z_force)
        session.commit()
        hero_deadpond = Hero(
            name="Deadpond", secret_name="Dive Wilson", team_id=team_z_force.id
        )
        hero_rusty_man = Hero(
            name="Rusty-Man",
            secret_name="Tommy Sharp",
            age=48,
            team_id=team_preventers.id,
        )
        hero_spider_boy = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        session.commit()

def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.team_id == 3)
        results = session.exec(statement)
        hero = results.all()
        print("Hero: ", hero)

# Code above omitted 👆

def update_heroes_add_relation():
    with Session(engine) as session:
        team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret's Bar")
        # session.add(team_preventers)
        # session.add(team_z_force)
        # session.commit()
        hero_deadpond = Hero(
            name="Deadpond", secret_name="Dive Wilson", team_id=team_z_force.id
        )
        hero_rusty_man = Hero(
            name="Rusty-Man",
            secret_name="Tommy Sharp",
            age=48,
            team_id=team_preventers.id,
        )
        hero_spider_boy = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
        # session.add(hero_deadpond)
        # session.add(hero_rusty_man)
        # session.add(hero_spider_boy)
        # session.commit()
        # hero_spider_boy.team_id = 3
        hero_spider_boy.team_id = None
        session.add(hero_spider_boy)
        session.commit()


engine = create_engine(postgress_url,echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)   

if __name__ == "__main__":
    # create_db_and_tables()
    # create_heroes_team()
    # select_heroes()
    update_heroes_add_relation()