#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations


class DB:
    """
    题目要求不用持久化, 数据全放内存, 故而弄了这个单例用于存储用户、角色数据
    """
    def __init__(self):
        self.user_table = []
        self.role_table = []
        self.user_role_table = []


db = DB()
