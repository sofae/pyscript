#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, BIGINT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlalchemy_db = 'sqlite://'

Base = declarative_base()


class Demo(Base):
    __tablename__ = 'demo'
    id = Column(BIGINT, primary_key=True)
    task = Column(BIGINT)


uline_engine = create_engine(sqlalchemy_db, pool_recycle=3600, echo=False)

Base.metadata.bind = uline_engine
Base.metadata.create_all(checkfirst=True)
db_Session = sessionmaker()
db_Session.configure(bind=uline_engine)

session = db_Session()


def insert_data(id, task):
    if session.query(Demo).filter(Demo.id == id, Demo.task == task).first():
        return
    session.add(Demo(id=id, task=task))
    session.commit()


def test_insert_data(trade_session):
    insert_data(20, 2)
    insert_data(21, 2)


test_insert_data(session)

a = session.query(Demo).first()
print({c.name: getattr(a, c.name, None) for c in a.__table__.columns})

b = session.query(Demo.id, Demo.task).first()
print(b._asdict())
print(dict(zip(b.keys(), b)))

b = session.execute('select * from demo')
for i in b:
    print(dict(i.items()))

for i in session.query(Demo.id).all():
    print(dict(zip(i.keys(), i)))
