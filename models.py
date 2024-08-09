from sqlalchemy import Column, Integer, String, Text, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TranslationTask(Base):
    __tablename__ = "translation_tasks"
    id = Column(Integer, primary_key=True, index= True)
    text = Column(String, nullable=False)
    languages=Column(JSON, nullable=False)
    status=Column(String, default="In Progress")

    translation =Column(JSON, default={})