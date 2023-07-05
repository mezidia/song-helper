from schemas import User
from sqlmodel import Session, SQLModel, create_engine, select

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    with Session(engine) as session:
        yield session


def get_user(name: str) -> User | None:
    with Session(engine) as session:
        user = session.exec(select(User).where(User.name == name)).first()
        return user
