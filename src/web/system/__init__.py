#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'QHUANG'
from src import biz
from flask.ext.wtf import Form
from wtforms.fields.simple import TextAreaField, SubmitField
from wtforms.validators import Required
import hashlib


# 查询符合用户名和密码的用户ID:
sql_query_userID = '''
SELECT id FROM user_info WHERE username=:username AND password=:password
'''
# 注册(添加)用户信息:
sql_add_userInfo = '''
INSERT INTO user_info(username,password,email,phonenumber) VALUES (:username,:password,:email,:phonenum)
'''
sql_is_username_be_used = '''
SELECT id FROM user_info WHERE username=:username
'''
# 通过用户名查询其对应的密码:
sql_query_pwd_by_username = '''
SELECT password FROM user_info WHERE username=:username
'''
# 修改用户密码更新user_info表:
sql_modify_user_pwd = '''
UPDATE user_info SET password=:new_password WHERE username=:username
'''
# 查询所有的comments:
sql_query_all_comments = '''
SELECT * FROM comments
'''
# 添加评论到comments表中:
sql_add_comments = '''
INSERT INTO comments(body,author) VALUES (:body,:author)
'''
# 按照时间顺序降序排列comments表:
sql_comments_order_by_desc = '''
SELECT * FROM comments ORDER BY time DESC
'''
# 查询只符合某个用户的评论:
sql_query_comment_by_author = '''
SELECT * FROM comments WHERE author=:author
'''
# 根据commentID删除某条评论:
sql_del_comment_byID = '''
DELETE FROM comments WHERE id=:id
'''
# 通过commentID查找对应的评论者:
sql_query_author_by_commentID = '''
SELECT author FROM comments WHERE id=:id
'''

#用户信息User：
class User(biz.Biz):
    def __init__(self):
        return

    def login(self, username, password):
        userID = self.executeSql(sql_query_userID, username=username, password=password).one()
        print userID
        if userID:
            return userID
        else:
            return None

    def register(self, username, password, email, phonenum):
        result = self.executeSql(sql_add_userInfo, username=username, password=password, email=email, phonenum=phonenum)
        return

    def is_registered(self, username):
        idused = self.executeSql(sql_is_username_be_used, username=username).one()
        print idused
        return idused

    # 查询某个用户名对应的密码
    def check_pwd(self, username):
        old_pwd = self.executeSql(sql_query_pwd_by_username, username=username).one()
        return old_pwd

    def modify_pwd(self, new_password, username):
        result = self.executeSql(sql_modify_user_pwd, new_password=new_password, username=username)
        return

#定义评论表单Comment：
class Comment(biz.Biz):
    def __init__(self):
        return

    def all_comments(self):
        self.executeSql(sql_query_all_comments)
        cmlist = self.executeSql(sql_comments_order_by_desc).all()
        return cmlist

    def add_comment(self,body,author):
        self.executeSql(sql_add_comments, body=body,author=author)
        cmlist = self.executeSql(sql_comments_order_by_desc).all()
        # print cmlist
        return cmlist

    def del_comment(self,id):
        self.executeSql(sql_del_comment_byID, id=id)
        cmlist = self.executeSql(sql_comments_order_by_desc).all()
        return cmlist

    # 只显示我的评论
    def show_myCommnet(self,author):
        self.executeSql(sql_comments_order_by_desc)
        cmlist = self.executeSql(sql_query_comment_by_author, author=author).all()
        return cmlist

    # 通过commentID查找对应的评论人(author):
    def check_author(self,id):
        author = self.executeSql(sql_query_author_by_commentID, id=id).one()
        return author

    # 反序排列list修改成cmlist.reverse()写法不支持？？？？？？？
