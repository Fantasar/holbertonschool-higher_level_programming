#!/usr/bin/python3
"""
Modules pour créer une classe en utilisant SQL Alchimie
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class city(Base):
    """
    Création de la classe city
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)