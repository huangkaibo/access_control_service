#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations

import os
import sys
import unittest

current_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
code_dir = os.path.join(current_dir, '..')
sys.path.append(os.path.join(code_dir, 'lib'))
sys.path.append(os.path.join(code_dir, 'bin/db'))
sys.path.append(os.path.join(code_dir, 'bin/dao'))
sys.path.append(os.path.join(code_dir, 'bin/entity'))
sys.path.append(os.path.join(code_dir, 'bin/controller'))

from db import db
from role import Role
from user_dao import UserDao
from role_dao import RoleDao
from user_controller import UserController
from role_controller import RoleController
from user_role_controller import UserRoleController
from token_controller import TokenController
from access_control_controller import AccessControlController
from exception import InvalidToken, UserNotExist, AuthFailed, UserExist, RoleExist, RoleNotExist


class TestRole(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRole, self).__init__(*args, **kwargs)
        self.user_controller = UserController()
        self.user_dao = UserDao()
        self.role_controller = RoleController()
        self.role_dao = RoleDao()
        self.access_control_controller = AccessControlController()
        self.user_role_controller = UserRoleController()
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

    def test_add_role(self):
        """
        添加角色
        """
        self.role_controller.add_role('role_name1')
        role = self.role_dao.get_role(role_name='role_name1')
        self.assertIsInstance(role, Role)

    def test_delete_role(self):
        """
        删除角色
        """
        self.role_controller.add_role('role_name1')
        role = self.role_dao.get_role(role_name='role_name1')
        self.role_controller.delete_role(role)
        role = self.role_dao.get_role(role_name='role_name1')
        self.assertIsNone(role)

    def test_delete_not_exist_role(self):
        """
        删除不存在的角色
        """
        self.role_controller.add_role('role_name1')
        role = self.role_dao.get_role(role_name='role_name1')
        self.role_controller.delete_role(role)
        self.assertRaises(RoleNotExist, self.role_controller.delete_role, role)

    def test_duplicate_add_role(self):
        """
        重复添加角色
        """
        self.role_controller.add_role('role_name1')
        self.assertRaises(RoleExist, self.role_controller.add_role, 'role_name1')

    def test_check_role(self):
        """
        token是否关联到了角色
        """
        # 创建user
        self.user_controller.add_user('user_name1', 'password1')
        user = self.user_dao.get_user(user_name='user_name1')
        # 签发token
        token = self.access_control_controller.authenticate('user_name1', 'password1')
        # 创建role1
        self.role_controller.add_role('role_name1')
        role1 = self.role_dao.get_role(role_name='role_name1')
        # user绑定到role1
        self.user_role_controller.add_role_to_user(user, role1)
        # 创建role2, role2不绑定
        self.role_controller.add_role('role_name2')
        role2 = self.role_dao.get_role(role_name='role_name2')
        # 判断role1和role2是否绑定
        is_bind1 = self.role_controller.check_role(token, role1)
        is_bind2 = self.role_controller.check_role(token, role2)
        self.assertEqual(is_bind1, True)
        self.assertEqual(is_bind2, False)

    def test_all_roles(self):
        """
        获取token关联的所有角色
        """
        # 创建user
        self.user_controller.add_user('user_name1', 'password1')
        user = self.user_dao.get_user(user_name='user_name1')
        # 签发token
        token = self.access_control_controller.authenticate('user_name1', 'password1')
        # 创建role1
        self.role_controller.add_role('role_name1')
        role1 = self.role_dao.get_role(role_name='role_name1')
        # user绑定到role1
        self.user_role_controller.add_role_to_user(user, role1)
        # 创建role2
        self.role_controller.add_role('role_name2')
        role2 = self.role_dao.get_role(role_name='role_name2')
        # user绑定到role1
        self.user_role_controller.add_role_to_user(user, role2)
        # 创建role3, 不绑定
        self.role_controller.add_role('role_name3')
        role3 = self.role_dao.get_role(role_name='role_name3')
        # 获取关联的所有角色
        bind_role_list = self.role_controller.all_roles(token)
        bind_role_id_list = [br.id for br in bind_role_list]
        self.assertIn(role1.id, bind_role_id_list)
        self.assertIn(role2.id, bind_role_id_list)
        self.assertNotIn(role3.id, bind_role_id_list)


if __name__ == '__main__':
    unittest.main()
