#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations

import os
import sys
import unittest
from time import sleep

current_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
code_dir = os.path.join(current_dir, '..')
sys.path.append(os.path.join(code_dir, 'lib'))
sys.path.append(os.path.join(code_dir, 'bin/db'))
sys.path.append(os.path.join(code_dir, 'bin/dao'))
sys.path.append(os.path.join(code_dir, 'bin/entity'))
sys.path.append(os.path.join(code_dir, 'bin/controller'))

from db import db
from utils import Utils
from user import User
from role import Role
from user_role import UserRole
from user_dao import UserDao
from role_dao import RoleDao
from user_role_dao import UserRoleDao
from user_controller import UserController
from role_controller import RoleController
from user_role_controller import UserRoleController
from token_controller import TokenController
from access_control_controller import AccessControlController
from exception import InvalidToken, UserNotExist, AuthFailed, UserExist, RoleExist, RoleNotExist


class TestUser(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestUser, self).__init__(*args, **kwargs)
        self.user_controller = UserController()
        self.user_dao = UserDao()

    def setUp(self) -> None:
        db.user_table = []
        db.role_table = []
        db.user_role_table = []
        db.token_black_list = []

    def tearDown(self) -> None:
        db.user_table = []
        db.role_table = []
        db.user_role_table = []
        db.token_black_list = []

    def test_add_user(self):
        """
        添加用户
        """
        self.user_controller.add_user('user_name1', 'password1')
        user = self.user_dao.get_user(user_name='user_name1')
        self.assertIsInstance(user, User)

    def test_delete_user(self):
        """
        删除用户
        """
        self.user_controller.add_user('user_name1', 'password1')
        user = self.user_dao.get_user(user_name='user_name1')
        self.user_controller.delete_user(user)
        user = self.user_dao.get_user(user_name='user_name1')
        self.assertIsNone(user)

    def test_delete_not_exist_user(self):
        """
        删除不存在的用户
        """
        self.user_controller.add_user('user_name1', 'password1')
        user = self.user_dao.get_user(user_name='user_name1')
        self.user_controller.delete_user(user)
        self.assertRaises(UserNotExist, self.user_controller.delete_user, user)

    def test_duplicate_add_user(self):
        """
        重复添加用户
        """
        self.user_controller.add_user('user_name1', 'password1')
        self.assertRaises(UserExist, self.user_controller.add_user, 'user_name1', 'password1')


if __name__ == '__main__':
    unittest.main()
