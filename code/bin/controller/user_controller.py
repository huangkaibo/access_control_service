#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations

import os
import sys

current_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
code_dir = os.path.join(current_dir, '../..')
sys.path.append(os.path.join(code_dir, 'lib'))
sys.path.append(os.path.join(code_dir, 'bin/db'))
sys.path.append(os.path.join(code_dir, 'bin/dao'))
sys.path.append(os.path.join(code_dir, 'bin/entity'))

from user import User
from utils import Utils
from user_dao import UserDao
from exception import InvalidToken, UserNotExist, AuthFailed, UserExist


class UserController:
    """
    用户管理相关API
    (逻辑较浅, 所以controller和service合在一起写)
    """
    def add_user(self, user_name: str, password: str) -> None:
        """
        注册用户

        Args:
            user_name: 用户名
            password: 密码

        Returns:
            None
        """
        user_dao = UserDao()
        # 已存在
        if user_dao.get_user(user_name=user_name):
            raise UserExist(user_name)

        user = User(
            id=None,
            name=user_name,
            password=None,
            salt=None,
            enabled=None,
            create_time=None,
            modify_time=None
        )
        # 盐
        user.salt = Utils.generate_random_string(8)
        # 密码+盐加密
        user.password = Utils.calc_md5(password + user.salt)
        user_dao.add_user(user)

    def delete_user(self, user: 'User') -> None:
        """
        注销用户

        Args:
            user: 用户实体

        Returns:
            None
        """
        user_dao = UserDao()
        if not user_dao.get_user(user_id=user.id):
            raise UserNotExist(user.name)
        user_dao.delete_user(user.id)
