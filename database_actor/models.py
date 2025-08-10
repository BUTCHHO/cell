from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, Table, String, ForeignKey


Base = declarative_base()


users_to_repos_association_table = Table('users_to_repos',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('repository_id', String, ForeignKey('repositories.id'))
)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, is_unique=True)
    role = Column(String)
    repositories = relationship('repositories', secondary='users_to_repos',
                                       back_populates='owners')

class Repository(Base):
    __tablename__ = 'repositories'
    id = Column(String, primary_key=True)
    name = Column(String, is_unique=True)
    owners = relationship('users', secondary='users_to_repos', back_populates='repositories')