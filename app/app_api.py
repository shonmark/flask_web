#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : flask_api.py
# @Author: shone
# @Date : 2018/1/15

from views import login_required, jsonify
from flask import render_template, redirect, url_for


def init_api(app):
    from app.models import Class, Total
    from app.models import db

    @app.route('/department/<string:department>', methods=['GET'])
    def department(department):
        classes = Class.query.filter_by(department_num=department).all()
        if classes:
            message = []
            for one_class in classes:
                message.append({
                    'class_number':str(one_class.class_number),
                    'class_name':str(one_class.class_name)
                })
            # print(message)
            return jsonify(message)
        else:
            return jsonify({'message': 'failed'})


    @app.route('/students/<string:class_num>', methods=['GET'])
    def students(class_num):
        students = Total.query.filter_by(class_num=class_num).all()
        if students:
            message = []
            for student in students:
                message.append({
                    'student_id':str(student.student_id),
                    'eat_money':str(student.eat_money),
                    'eat_times': str(student.eat_times),
                    'score': str(student.score),
                    'amount': str(student.amount)
                })
            # print(message)
            return jsonify(message)
        else:
            return jsonify({'message': 'failed'})

    # @app.route('/find/<int:book_id>', methods=['GET'])
    # @login_required
    # def del_user(book_id):
    #     book = Book.query.filter_by(book_id=book_id).first()
    #     if book:
    #
    #         return jsonify({
    #             'message': 'success',
    #             'book_name': book.book_name,
    #             'author': book.author,
    #             'kinds': book.kinds,
    #             'left_amount': book.left_amount,
    #             'press': book.press,
    #
    #         })
    #     else:
    #         return jsonify({'message': 'failed'})