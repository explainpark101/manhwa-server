from .config import Base
from sqlalchemy import Column, Integer, String
import json


class Recent(Base):
    __tablename__ = "recents"
    id = Column(Integer, primary_key=True, autoincrement=True)

    comicId = Column(Integer, unique=True)
    title = Column(Integer)
    href = Column(String)
    author = Column(String)
    time = Column(Integer)
    episode = Column(String)
    __genre = Column(String, name="genre")
    
    @property
    def genre(self):
        return json.loads(self.__genre)

    @genre.setter
    def genre(self, value:list[str] | str) -> None:
        if not isinstance(value, str):
            value = json.dumps(value)
        self.__genre = value
        
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class Bookmark(Base):
    __tablename__ = 'bookmarks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    href = Column(String, unique=True)
    title = Column(String)
    author = Column(String)
    __genre = Column(String, name="genre")
    
    
    @property
    def genre(self):
        return json.loads(self.__genre)

    @genre.setter
    def genre(self, value:list[str] | str) -> None:
        if not isinstance(value, str):
            value = json.dumps(value)
        self.__genre = value

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
