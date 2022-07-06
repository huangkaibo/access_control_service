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
from role import Role
from user_role import UserRole


class UserRoleDao:
    """
    用户-角色关系的curd
    """
    def add_user_role(self, user: 'User', role: 'Role') -> None:
        """
        添加用户-角色

        Args:
            user: 用户
            role: 角色

        Returns:
            None
        """
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.user_role_table.append({
            'id': str(len(db.user_role_table)),
            'user_id': user.id,
            'role_id': role.id,
            'enabled': True,
            'create_time': now,
            'modify_time': now
        })

    def get_user_role(self, user_id: str = None, role_id: str = None) -> 'UserRole':
        """
        获取用户-角色

        Args:
            user_id: 用户id
            role_id: 角色id

        Returns:
            用户-角色
        """
        for user_role in db.user_role_table:
            if not user_role['enabled']:
                continue
            if user_id and user_role['id'] != user_id:
                continue
            if role_id and user_role['id'] != role_id:
                continue
            return UserRole(
                id=user_role['id'],
                user_id=user_role['user_id'],
                role_id=user_role['role_id'],
                enabled=user_role['enabled'],
                create_time=datetime.datetime.strptime(user_role['create_time'], '%Y-%m-%d %H:%M:%S'),
                modify_time=datetime.datetime.strptime(user_role['modify_time'], '%Y-%m-%d %H:%M:%S'),
            )

    def list_user_role(self, user_id: str = None) -> 'UserRole':
        """
        获取指定用户的所有用户-角色

        Args:
            user_id: 用户id

        Returns:
            用户-角色
        """
        user_role_list = []
        for user_role in db.user_role_table:
            if not user_role['enabled']:
                continue
            if user_id and user_role['user_id'] != user_id:
                continue
            user_role_list.append(UserRole(
                id=user_role['id'],
                user_id=user_role['user_id'],
                role_id=user_role['role_id'],
                enabled=user_role['enabled'],
                create_time=datetime.datetime.strptime(user_role['create_time'], '%Y-%m-%d %H:%M:%S'),
                modify_time=datetime.datetime.strptime(user_role['modify_time'], '%Y-%m-%d %H:%M:%S'),
            ))
        return user_role_list
