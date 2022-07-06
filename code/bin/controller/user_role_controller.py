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
