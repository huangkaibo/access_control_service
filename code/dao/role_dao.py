#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations

import os
import sys
import datetime

current_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
code_dir = os.path.join(current_dir, '..')
sys.path.append(os.path.join(code_dir, 'db'))
sys.path.append(os.path.join(code_dir, 'lib'))
sys.path.append(os.path.join(code_dir, 'entity'))

from db import db
from role import Role
from exception import RoleExist, RoleNotExist


class RoleDao:
    def add_role(self, role: 'Role') -> None:
        """
        添加角色

        Args:
            role: 角色

        Returns:
            None
        """
        role.id = str(len(db.role_table))
        if self.get_role(role_name=role.name):
            raise RoleExist(role.name)
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.role_table.append({
            'id': role.id,
            'name': role.name,
            'enabled': True,
            'create_time': now,
            'modify_time': now
        })

    def delete_role(self, role_id: str) -> None:
        """
        删除角色

        Args:
            role_id: 角色id

        Returns:
            None
        """
        for role in db.role_table:
            if role['id'] == role_id:
                role['enabled'] = False
                role['modify_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                return
        raise RoleNotExist(role_id)

    def get_role(self, role_id: str = None, role_name: str = None) -> 'Role':
        """
        获取角色

        Args:
            role_id: 角色id
            role_name: 角色name

        Returns:
            角色
        """
        for role in db.role_table:
            if not role['enabled']:
                continue
            if role_id and role['id'] != role_id:
                continue
            if role_name and role['name'] != role_name:
                continue
            return Role(
                id=role['id'],
                name=role['name'],
                enabled=role['enabled'],
                create_time=datetime.datetime.strptime(role['create_time'], '%Y-%m-%d %H:%M:%S'),
                modify_time=datetime.datetime.strptime(role['modify_time'], '%Y-%m-%d %H:%M:%S'),
            )
