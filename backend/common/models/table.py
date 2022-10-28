from dataclasses import dataclass
from datetime import date
from enum import Enum as EnumClass

from sqlalchemy import Table, Column, Integer, String, Enum, ForeignKey, BigInteger, Date, \
    ForeignKeyConstraint, UniqueConstraint, PrimaryKeyConstraint

from common.models.bases import metadata, mapper_registry


@dataclass
class First_tabl:
    reg_nomer: int
    date_postup: date
    name_doc: str
    story_doc: str
    foiv: str
    cur_aprf: str
    napr: str
    fed_num: str
    type_of_doc: str
    resh_doc: str
    status: str
    fin_oc: int
    exp_oc: int
    req_otv: int
    date_otv: date


@dataclass
class Second_tabl:
    reg_nomer: str
    date_postup: date
    name_doc: str
    story_doc: str
    foiv: str
    cur_aprf: str
    napr: str
    fed_num: str
    type_of_doc: str
    resh_doc: str
    status: str
    fin_oc: int
    exp_oc: int
    req_otv: int
    date_otv: date


first_tabl = Table('first_tabl', metadata,
                   Column('reg_nomer', Integer(), nullable=False, primary_key=True),
                   Column('date_postup', Date(), nullable=False),
                   Column('name_doc', String(), nullable=False),
                   Column('story_doc', String(), nullable=False),
                   Column('foiv', String(), nullable=False),
                   Column('cur_aprf', String(), nullable=False),
                   Column('napr', String(), nullable=False),
                   Column('fed_num', String(), nullable=False),
                   Column('type_of_doc', String(), nullable=False),
                   Column('resh_doc', String(), nullable=False),
                   Column('status', String(), nullable=False),
                   Column('fin_oc', Integer(), nullable=False),
                   Column('exp_oc', Integer(), nullable=False),
                   Column('req_otv', Integer(), nullable=False),
                   Column('date_otv', Date(), nullable=False),
                   )

second_tabl = Table('second_tabl', metadata,
                    Column('id', Integer(), nullable=False, primary_key=True),
                    Column('reg_nomer', String()),
                    Column('date_postup', Date()),
                    Column('name_doc', String()),
                    Column('story_doc', String()),
                    Column('foiv', String()),
                    Column('cur_aprf', String()),
                    Column('napr', String()),
                    Column('fed_num', String()),
                    Column('type_of_doc', String()),
                    Column('resh_doc', String()),
                    Column('status', String()),
                    Column('fin_oc', String()),
                    Column('exp_oc', String()),
                    Column('req_otv', String()),
                    Column('date_otv', Date()),
                    )

mapper_registry.map_imperatively(First_tabl, first_tabl)
mapper_registry.map_imperatively(Second_tabl, second_tabl)
