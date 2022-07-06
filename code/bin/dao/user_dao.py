#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations

import os
import sys
import datetime

current_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
code_dir = os.path.join(current_dir, '../..')
sys.path.append(os.path.join(code_dir, 'bin/db'))
sys.path.append(os.path.join(code_dir, 'lib'))
sys.path.append(os.path.join(code_dir, 'bin/entity'))

from db import db
from user import User


class UserDao:
    """
    用户的curd
    """
    def add_user(self, user: 'User') -> None:
        """
        添加用户

        Args:
            user: 用户

        Returns:
            None
        """
        user.id = str(len(db.user_table))
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.user_table.append({
            'id': user.id,
            'name': user.name,
            'password': user.password,
            'salt': user.salt,
            'enabled': True,
            'create_time': now,
            'modify_time': now
        })

    def delete_user(self, user_id: str) -> None:
        """
        删除用户

        Args:
            user_id: 用户id

        Returns:
            None
        """
        for user in db.user_table:
            if user['id'] == user_id:
                user['enabled'] = False
                user['modify_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                return

    def get_user(self, user_id: str = None, user_name: str = None) -> 'User':
        """
        获取用户

        Args:
            user_id: 用户id
            user_name: 用户名

        Returns:
            用户
        """
        for user in db.user_table:
            if not user['enabled']:
                continue
            if user_id and user['id'] != user_id:
                continue
            if user_name and user['name'] != user_name:
                continue
            return User(
                id=user['id'],
                name=user['name'],
                password=user['password'],
                salt=user['salt'],
                enabled=user['enabled'],
                create_time=datetime.datetime.strptime(user['create_time'], '%Y-%m-%d %H:%M:%S'),
                modify_time=datetime.datetime.strptime(user['modify_time'], '%Y-%m-%d %H:%M:%S'),
            )
