# -*- coding: utf-8 -*-

from peewee import *
from datetime import datetime
from hashlib import sha256

from peewee import ForeignKeyField

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
        order_by = ('login',)


class Task(BaseModel):
    taskId = IntegerField(primary_key = True, column_name = "id", index = True)
    name = CharField(null = False)
    description = CharField()
    create_date = DateTimeField(default = datetime.now)
    time_to_do = IntegerField(null = False) #Time in minutes, every 480 minuts are 1 day
    value = IntegerField(null = False)
    done = BooleanField(default = False)
    user_id = ForeignKeyField(User, field = User.userId, related_name = "Zadanie")

    class Meta:
        order_by = ('value',)


def hexToStr(passwd):
    return str(sha256(passwd.encode('utf-8')).hexdigest())


def connect():
    dbbase.connect()
    dbbase.create_tables([User, Task])
    loadTestData()
    return True


def tolog(login, password):
    try:
        user, created = User.get_or_create(login = login, password = hexToStr(password))
        print('user ID in motdconnect.py line 56:', user.userId)
        return user.userId
    except IntegrityError:
        return None


def loadTestData():
    """
    Preparation of initial data
    """
    if User.select().count() > 0:
        return

    users = [
    ['Adam', '123'],
    ['Zawadiaka', '123']
    ]
    tasks = [
    ['Napisać 200 linijek kodu', 'Napisać 200 linijek kodu w rozpoczetych projektach', 480, 2,False, 1],
    ['Zrobic porządek z mailami', 'Uporządkowac skrzynkę odbiorczą', 100, 1 ,False, 2]
    ]

    for user in users:
        u = User(login = user[0], password = hexToStr(user[1]))
        u.save()

    for task in tasks:
        t = Task(
            name = task[0],
            description = task[1],
            time_to_do = task[2],
            value = task[3],
            done = task[4],
            user_id = task[5]
            )
        t.save()

    dbbase.commit()
    dbbase.close()

def readData(owner):
    """
    :param osoba: id from User
    :return: list of tasks
    """

    tasks = []
    posts = (Task.select().where(Task.user_id == owner))
    for p in posts:
        tasks.append([
            p.taskId, # identificator of task
            p.name,
            p.description,
            '{0:%Y-%m-%d %H:%M:%S}'.format(p.create_date),
            p.time_to_do,
            p.value,
            p.done,
            False]) # delete task?
    return tasks


