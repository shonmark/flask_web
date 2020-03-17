#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : views.py
# @Author: shone
# @Date  : 2017/11/5
from flask import render_template, redirect, url_for, jsonify, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from threading import Thread
login_manager = LoginManager()


def init_views(app):
    mail = Mail(app)
    from app.models import Teacher, Class, Total, Department, Email
    from app.forms import LoginForm, RegisterForm, EmailForm, Change_info, Change_password
    from app.models import db
    # def send_async_email(app, msg):
    #     with app.app_context():
    #         mail.send(msg)

    @login_manager.user_loader
    def load_user(user_id):
        return Teacher.query.get(int(user_id))

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = Teacher.query.filter_by(teacher_id=form.username.data).first()
            if user:
                if check_password_hash(user.password, form.password.data):
                    login_user(user, remember=form.remember.data)
                    return redirect(url_for('dashboard'))

            return '<h1>Invalid username or password</h1>'
        return render_template('login.html', form=form)

    @app.route('/change_password', methods=['GET', 'POST'])
    def change_password():
        form = Change_password()
        user = Teacher.query.filter_by(teacher_id=current_user.teacher_id).first()
        if form.validate_on_submit():
            password_first = form.new_password.data
            password_second = form.config_password.data
            if check_password_hash(user.password, form.password.data):
                if password_first == password_second:
                    hashed_password = generate_password_hash(password_first, method='sha256')
                    user.password = hashed_password
                    db.session.commit()
                    return redirect(url_for('login'))
                else:
                    return '<h1>两次密码不一致<h1>'
            else:
                return '<h1>旧密码错误<h1>'
        return render_template('change_password.html', form=form)

    @app.route('/dashboard')
    @login_required
    def dashboard():
        
        department_list = Department.query.all()
        return render_template('dashboard.html', department_list=department_list, name=current_user.teacher_id)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))

    @app.route('/email', methods=['GET', 'POST'])
    @login_required
    def email():
        email_form = EmailForm()
        if email_form.validate_on_submit():
            msg = Email(title=email_form.title.data, content=email_form.content.data)
            # 邮件内容会以文本和html两种格式呈现，而你能看到哪种格式取决于你的邮件客户端。
            db.session.add(msg)
            db.session.commit()
            return '<h1>邮件发送成功</h1><a href="http://127.0.0.1:5000/dashboard">点此回主页</a>'
        return render_template('email.html', form=email_form)

    @app.route('/school')
    @login_required
    def school():
        return render_template('school_info.html')

    @app.route('/setting')
    @login_required
    def setting():
        user_info = Teacher.query.filter_by(teacher_id=current_user.teacher_id).first()
        return render_template('setting.html', user_info=user_info)

    @app.route('/change_info', methods=['GET', 'POST'])
    @login_required
    def change_info():
        teacher_id = current_user.teacher_id
        form = Change_info()
        if form.is_submitted():
            user_info = Teacher.query.filter_by(teacher_id=teacher_id).first()
            if user_info:
                user_info.phone = form.phone.data
                user_info.email = form.e_mail.data
                db.session.commit()
            else:
                return redirect(login)
            return render_template('setting.html', user_info=user_info)
        return render_template('change_info.html', form=form)

