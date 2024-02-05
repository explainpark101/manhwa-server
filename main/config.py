from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import pathlib
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BASE_DIR = pathlib.Path(__name__).resolve().parent
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
connectDB = lambda :sqlite3.connect(BASE_DIR/'database.sqlite3')



engine = create_engine(f"sqlite:///{BASE_DIR}/database.sqlite3", echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
