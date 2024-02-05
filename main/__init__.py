
from typing import Union, Annotated, Dict, Any
from .database import init, Insert, Select
from .config import BASE_DIR, app, connectDB, db_session
from .models import Recent, Bookmark
from fastapi import Body
from pydantic import BaseModel

class Recents(BaseModel):
    comicId:int
    title:str
    href:str
    author:str
    time:int
    episode:str
    genre:str
    
class Bookmarks(BaseModel):
    href:str
    title:str
    author:str
    genre:str
    
@app.get("/")
def readAll():
    return {"recents": Select.fromRecents(), "bookmarks": Select.fromBookmarks()}

@app.post("/recents")
def add_recents(body: Dict[Any, Any]):
    recent_comic = Recent.query.filter_by(comicId=body.get('comicId')).all()
    if len(recent_comic):
        recent_comic = recent_comic[0]
        recent_comic.time = body.get('time')
        db_session.commit()
    else:
        db_session.add(Recent(**body))
        db_session.commit()
    return {"success": True}

@app.post("/bookmarks")
def add_bookmarks(body: Dict[Any, Any]):
    db_session.add(Bookmark(**body))
    db_session.commit()
    return {"success": True}

@app.delete("/recents")
def delete_recents(body: Dict[Any, Any]):
    objs = Recent.query.filter_by(**body)
    for obj in objs:
        db_session.delete(obj)
    db_session.commit()
    return {"success": True}

@app.delete("/bookmarks")
def delete_bookmarks(body: Dict[Any, Any]):
    objs = Bookmark.query.filter_by(**body)
    for obj in objs:
        db_session.delete(obj)
    db_session.commit()
    return {"success": True}

@app.put("/recents")
def update_recents(body: Recents):
    return {"success": True}

@app.put("/bookmarks")
def update_bookmarks(body: Bookmarks):
    return {"success": True}


init()