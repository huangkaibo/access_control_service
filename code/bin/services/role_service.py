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

from role import Role
from role_dao import RoleDao
from user_role_dao import UserRoleDao
from token_manater import TokenService
from exception import InvalidToken, UserNotExist, AuthFailed, UserExist, RoleExist, RoleNotExist


class RoleService:
    def add_role(self, role_name: str) -> None:
        """
        添加角色

        Args:
            role_name: 角色名

        Returns:
            None
        """
        role_dao = RoleDao()
        # 已存在
        if role_dao.get_role(role_name=role_name):
            raise RoleExist(role_name)

        role = Role(
            id=None,
            name=role_name,
            enabled=None,
            create_time=None,
            modify_time=None
        )
        role_dao.add_role(role)

    def delete_role(self, role_id: str) -> None:
        """
        删除角色

        Args:
            role_id: 角色id

        Returns:
            None
        """
        role_dao = RoleDao()
        role = role_dao.get_role(role_id=role_id)
        if not role:
            raise RoleNotExist(role_id)
        else:
            role_dao.delete(role_id)

    def check_role(self, auth_token: str, role: 'Role') -> bool:
        """
        校验token所代表的用户是否关联到了指定角色上

        Args:
            auth_token: token
            role: 角色实体

        Returns:
            true代表已关联, false代表未关联
        """
        user = TokenService().parse_token(auth_token)
        user_role = UserRoleDao().get_user_role(user_id=user.id, role_id=role.id)
        return user_role is not None
