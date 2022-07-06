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
from user_dao import UserDao
from role_dao import RoleDao
from user_role_dao import UserRoleDao
from user_controller import UserController
from role_controller import RoleController
from user_role_controller import UserRoleController
from token_controller import TokenController
from access_control_controller import AccessControlController
from exception import InvalidToken, UserNotExist, AuthFailed, UserExist, RoleExist, RoleNotExist


class TestAccessControl(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAccessControl, self).__init__(*args, **kwargs)
        self.user_controller = UserController()
        self.user_dao = UserDao()
        self.role_controller = RoleController()
        self.role_dao = RoleDao()
        self.user_role_controller = UserRoleController()
        self.user_role_dao = UserRoleDao()
        self.access_control_controller = AccessControlController()
        self.token_controller = TokenController()

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

    def test_authenticate(self):
        """
        成功鉴权
        """
        self.user_controller.add_user('user_name1', 'password1')
        token = self.access_control_controller.authenticate('user_name1', 'password1')
        self.assertIsInstance(token, str)

    def test_authenticate_not_exist_user(self):
        """
        鉴权不存在的用户
        """
        self.assertRaises(UserNotExist, self.access_control_controller.authenticate, 'user_name1', 'password1')

    def test_authenticate_wrong_password(self):
        """
        鉴权密码错误
        """
        self.user_controller.add_user('user_name1', 'password1')
        self.assertRaises(AuthFailed, self.access_control_controller.authenticate, 'user_name1', 'password_wrong')

    def test_expire_token(self):
        """
        token过期
        """
        self.user_controller.add_user('user_name1', 'password1')
        token = self.access_control_controller.authenticate('user_name1', 'password1')
        self.assertIsInstance(token, str)
        sleep(5)
        self.assertRaises(InvalidToken, self.token_controller.parse_token, token)

    def test_invalidate(self):
        """
        失活token
        """
        self.user_controller.add_user('user_name1', 'password1')
        token = self.access_control_controller.authenticate('user_name1', 'password1')
        self.assertIsInstance(token, str)
        self.access_control_controller.invalidate(token)
        self.assertRaises(InvalidToken, self.token_controller.parse_token, token)


if __name__ == '__main__':
    unittest.main()
