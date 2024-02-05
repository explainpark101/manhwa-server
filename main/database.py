# https://qratedev.tistory.com/32

import sqlite3
from .config import connectDB, init_db


def dictfetchall(cursor:sqlite3.Cursor) -> list[dict]:
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def init():
    
    
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name FROM sqlite_master WHERE type IN ('table', 'view') AND name NOT LIKE 'sqlite_%' 
        UNION ALL 
        SELECT name FROM sqlite_temp_master WHERE type IN ('table', 'view') ORDER BY 1;
    """)
    res = [_.get("name") for _ in dictfetchall(cursor)]
    # no database found
    if 'recents' not in res and 'bookmarks' not in res:
       init_db()
    return

class Insert:
    @staticmethod
    def intoRecents(body:dict) -> None:
        data = []
        for _ in [ "comicId", "title", "href", "author", "time", "episode", "genre",]:
            data.append(body.get(_))
            
            conn = connectDB()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO recents (comicId, title, href, author, time, episode, genre)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, data)
    
    @staticmethod
    def intoBookmarks(body:dict) -> None:
        data = []
        for _ in [ "href", "title", "author", "genre"]:
            data.append(body.get(_))
            conn = connectDB()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO bookmarks (href, title, author, genre)
            VALUES (?, ?, ?, ?)             
        """, data)


class Select:
    @staticmethod
    def fromRecents() -> list[dict]:
        conn = connectDB()
        cur = conn.cursor()
        cur.execute("SELECT * FROM recents ORDER BY time DESC")
        return dictfetchall(cur)
    
    @staticmethod
    def fromBookmarks() -> list[dict]:
        conn = connectDB()
        cur = conn.cursor()
        cur.execute("SELECT * FROM bookmarks")
        return dictfetchall(cur)
        
class Delete:
    @staticmethod
    def fromRecents(body:dict) -> None:
        conn = connectDB()
        cur = conn.cursor()
        cur.execute('''
            DELETE FROM recents
            WHERE comicId = ?
                AND href = ?
        ''', [body.get('comicId'), body.get('href')])

        
    @staticmethod
    def fromBookmarks(body:dict) -> None:
        conn = connectDB()
        cur = conn.cursor()
        cur.execute('''
            DELETE FROM bookmarks
            WHERE href = ?
        ''', [body.get('href'), ])
        