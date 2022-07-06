#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations

import os
import sys

current_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
code_dir = os.path.join(current_dir, '../..')
sys.path.append(os.path.join(code_dir, 'db'))
sys.path.append(os.path.join(code_dir, 'lib'))
sys.path.append(os.path.join(code_dir, 'entity'))

from user import User
from utils import Utils
from user_dao import UserDao
from exception import InvalidToken, UserNotExist, AuthFailed, UserExist


class RoleService:
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

    def all_roles(self, auth_token: str) -> List['UserRole']:
        """
        1. 返回这个角色的所有role
        2. 如果token无效, 返回error

        Args:
            auth_token (_type_): _description_
        """
        pass