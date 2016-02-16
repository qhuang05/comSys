#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'QHUANG'

from flask import request, Blueprint, render_template, redirect, session, url_for
from . import User, Comment
from src.tools import JSON
from src.tools import HTTP

bp = Blueprint("system", __name__)
bp.secret_key = '\xb0Q_\xe4\x02\x95\xc4\x88\x1aG\xff\x1d\x95\xff\xff43Q\xe6p\xce\xea-\x05'

@bp.route("/")
def index():
    return render_template('login.html')

@bp.route("/login", methods=['POST'])
def login():
    log_name = request.form.get('username')
    session['username'] = log_name
    log_pwd = request.form.get('password')
    # print log_name,log_pwd
    LoginUser = User()
    comment = Comment()
    comments = comment.all_comments()
    # print comments
    if LoginUser.login(log_name,log_pwd):
        return render_template('index.html', comments=comments, name=session['username'])
        # return "<h1>Welcome,{{log_name}}</h1>"
    else:
        return render_template('login.html', erroMsg='错误的用户名或密码')

@bp.route("/regPage")
def regPage():
    return render_template('register.html')


@bp.route("/register", methods=['POST'])
def register():
    reg_name = request.form.get('username')
    reg_password = request.form.get('password')
    reg_email = request.form.get('email')
    reg_phonenum = request.form.get('phonenum')
    RegUser = User()
    # return "<span>恭喜你注册成功！</span>"
    if RegUser.is_registered(reg_name):
        return render_template('register.html', errMsg='用户名已被注册')
    else:
        RegUser.register(reg_name, reg_password, reg_email, reg_phonenum)
        return redirect('/')


@bp.route('/addComment', methods=['GET', 'POST'])
def add_comment():
    # ctxt = request.form.get('txt')
    ctxt = request.values.get('txt')
    cauthor = session['username']
    comment = Comment()                                 # 实例化Comment()类
    comments = comment.add_comment(ctxt, cauthor)        # 返回所有comments表中的所有评论,一个list,list元素为dict类型
    # return render_template('index.html',comments=comments,name=session['username'])

    # print comments[0]
    json_str = JSON.dumps(comments[0])              # 把python中的dict类型转化为js中可用的json类型
    # print type(json_str), json_str
    return json_str

# 显示我的评论:
@bp.route('/myComment')
def show_myComment():
    comment = Comment()
    comments = comment.show_myCommnet(session['username'])
    return render_template('index.html', comments=comments, name=session['username'])


@bp.route('/delComment')
def del_comment():
    # del_id = request.form.get('id')
    del_id = request.values.get('delID')
    print '已获取delID...'+del_id
    comment = Comment()
    if comment.check_author(del_id) == session['username']:
        comments = comment.del_comment(del_id)
        res = '1'
    else:
        comments = comment.del_comment(-1)
        res = '0'
    # return render_template('index.html',comments=comments,name=session['username'])
    # json_str = JSON.dumps(res)
    return res

@bp.route('/renew_pwd_page')
def to_Renew_page():
    return render_template('modify_pwd.html')


@bp.route("/renewPassword", methods=['GET', 'POST'])
def modify_pwd():
    LoginUser = User()
    old_pwd = request.form.get('old_pwd')
    new_pwd = request.form.get('new_pwd')
    correct_pwd = LoginUser.check_pwd(session['username'])
    print old_pwd, new_pwd, correct_pwd
    print session['username'], correct_pwd
    if old_pwd == correct_pwd:
        LoginUser.modify_pwd(new_pwd, session['username'])
        print 'Change password success.'
        return redirect('/')
    else:
        # LoginUser.modify_pwd(old_pwd, session['username'])
        return render_template('modify_pwd.html', errMsg='密码错误')

