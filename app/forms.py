#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : forms.py
# @Author: shone
# @Date  : 2017/11/4
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


# class LoginForm(FlaskForm):
#     user_id = StringField(u'账号', validators=[DataRequired(message=u'账号不能为空')])
#     password = PasswordField(u'密码', validators=[DataRequired(message=u'密码不能为空')])
#     submit = SubmitField(u'登录')
#
class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message=u'用户名不能为空'), Length(min=4, max=15)])
    password = PasswordField('密码', validators=[DataRequired(message=u'密码不能为空'), Length(min=4, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(message=u'用户名不能为空'), Length(min=4, max=15)])
    password = PasswordField('password', validators=[DataRequired(message=u'密码不能为空'), Length(min=8, max=80)])


class EmailForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired(message=u'请写问题或意见'), Length(min=4,max=25)])
    content = TextAreaField('内容', validators=[DataRequired(message=u'请写内容'), Length(min=4,max=400)])


class Change_info(FlaskForm):
    phone = StringField('电话号码', validators=[DataRequired(message=u'手机号不能为空')])
    e_mail = StringField('邮箱', validators=[DataRequired(message=u'邮箱不能为空'), Email])


class Change_password(FlaskForm):
    password = PasswordField('密码', validators=[DataRequired(message=u'密码不能为空'), Length(min=8, max=80)])
    new_password = PasswordField('新密码', validators=[DataRequired(message=u'密码不能为空'), Length(min=8, max=80)])
    config_password = PasswordField('再输一次新密码', validators=[DataRequired(message=u'密码不能为空'), Length(min=8, max=80)])
