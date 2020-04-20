# -*- coding: utf-8 -*-

from peewee import *
from datetime import datetime

dbbase = SqliteDatabase('myowntodo.db')

class BaseModel(Model): 
    """
    class base
    """

    class Meta:
       database = dbbase

class User(BaseModel):
    userId = IntegerField(primary_key = True, column_name = "id", index = True)
    login = CharField(null = False, unique = True)
    password = CharField()

    class Meta:
        order_by('login')

class Task(BaseModel):
    taskId = IntegerField(primary_key = True, column_name = "id", index = True)
    name = CharField(null = False)
    description = CharField()
    create_date = DateTimeField(default = datetime.now)
    time_to_do = IntegerField(null = False) #Time in minutes, every 8 hours are 1 day
    value = IntegerField(null = False)
    done = BooleanField(default = False)

    class Meta:
        order_by = ('value')

def connect():
    dbbase.connect()
    dbbase.create_tables([User, Task], True)
    testDataLoad()
    return True

def tolog(login, password):
    try:
        User, created = User.get_or_create(login = login, password = password)
        return User
    except IntegrityError:
        return None

def loadData():
    """
    Preparation of initial data
    """
    if User.select().count > 0:
        return
    users = [
    ['Adam', '123'],
    ['Ewa', '123']
    ]
    tasks = [
    ['Napisać 200 linijek kodu', 'Napisać 200 linijek kodu w rozpoczetych projektach', 480, 2,False]
    ['Zrobic porządek z mailami', 'Uporządkowac skrzynkę odbiorczą', 100, 1,False]
    ]

    for user in users:
        u = User(login = user[0], password = user[1])
        u.save()

    for task in tasks:
        t = Task(
            name = task[0],
            description = task[1],
            time_to_do = task[2],
            value = task[3],
            done = task[4]
            )
        t.save()

    dbbase.commit()
    dbbase.close()



