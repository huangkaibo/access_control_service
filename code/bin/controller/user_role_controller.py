#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations
from typing import List

import os
import sys

current_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
code_dir = os.path.join(current_dir, '../..')
sys.path.append(os.path.join(code_dir, 'db'))
sys.path.append(os.path.join(code_dir, 'lib'))
sys.path.append(os.path.join(code_dir, 'entity'))

from user import User
from role_dao import RoleDao
from user_role_dao import UserRoleDao
from token_controller import TokenController


class UserRoleController:
    def add_role_to_user(self, user: 'User', role: 'Role') -> None:
        """
        将用户关联到角色上

        Args:
            user: user实体
            role: role实体

        Returns:
            None
        """
        UserRoleDao().add_user_role(user, role)

    def all_roles(self, auth_token: str) -> List['Role']:
        """
        1. 返回这个角色的所有role
        2. 如果token无效, 返回error

        Args:
            auth_token (_type_): _description_
        """
        user = TokenController().parse_token(auth_token)
        user_role_list = UserRoleDao().list_user_role(user_id=user.id)
        role_dao = RoleDao()
        role_list = []
        for user_role in user_role_list:
            role = role_dao.get_role(user_role.role_id)
            role_list.append(role)
        return role_list