#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : models.py
# @Author: shone
# @Date  : 2017/11/5
# @Desc
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Teacher(UserMixin, db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, unique=True)
    email = db.Column(db.VARCHAR(50))
    password = db.Column(db.VARCHAR(50))
    phone = db.Column(db.VARCHAR(20))


class Card(db.Model):
    __tablename__ = 'card_info'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    kinds = db.Column(db.VARCHAR(20))
    location = db.Column(db.VARCHAR(20))
    pay_type = db.Column(db.VARCHAR(20))
    pay_time = db.Column(db.DATETIME)
    money = db.Column(db.VARCHAR(20))
    left_money = db.Column(db.VARCHAR(20))


class Total(db.Model):
    __tablename__='count_info'
    id = db.Column(db.Integer, primary_key=True)
    class_num = db.Column(db.VARCHAR(20))
    student_id = db.Column(db.Integer)
    eat_money = db.Column(db.VARCHAR(20))
    eat_times = db.Column(db.VARCHAR(20))
    score = db.Column(db.VARCHAR(20))
    amount = db.Column(db.VARCHAR(20))


class Class(db.Model):
    __tablename__ = 'class_info'
    id = db.Column(db.Integer, primary_key=True)
    class_number = db.Column(db.Integer)
    class_name = db.Column(db.VARCHAR(10))
    department_num = db.Column(db.VARCHAR(10))


class Department(db.Model):
    __tablename__ = 'department_info'
    id = db.Column(db.Integer, primary_key=True)
    departmet_id = db.Column(db.Integer)
    department_name = db.Column(db.VARCHAR(10))

class Email(db.Model):
    __tablename__ = 'email'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer)
    content = db.Column(db.VARCHAR(10))


