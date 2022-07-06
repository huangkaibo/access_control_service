#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations
from typing import List

import os
import sys

current_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
code_dir = os.path.join(current_dir, '../..')
sys.path.append(os.path.join(code_dir, 'bin/db'))
sys.path.append(os.path.join(code_dir, 'lib'))
sys.path.append(os.path.join(code_dir, 'bin/entity'))
sys.path.append(os.path.join(code_dir, 'bin/dao'))

from user import User
from user_dao import UserDao
from role_dao import RoleDao
from user_role_dao import UserRoleDao
from exception import UserNotExist, RoleNotExist


class UserRoleController:
    """
    用户、角色关联关系相关api
    (逻辑较浅, 所以controller和service合在一起写)
    """
    def add_role_to_user(self, user: 'User', role: 'Role') -> None:
        """
        将用户关联到角色上

        Args:
            user: user实体
            role: role实体

        Returns:
            None
        """

        user_role_dao = UserRoleDao()
        # 已关联
        if user_role_dao.get_user_role(user_id=user.id, role_id=role.id):
            return
        # 用户不存在
        if not UserDao().get_user(user.id):
            raise UserNotExist()
        # 角色不存在
        if not RoleDao().get_role(role.id):
            raise RoleNotExist()
        user_role_dao.add_user_role(user, role)
