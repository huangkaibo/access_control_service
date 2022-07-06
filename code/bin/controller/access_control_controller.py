#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations

import os
import sys

current_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
code_dir = os.path.join(current_dir, '../..')
sys.path.append(os.path.join(code_dir, 'bin/db'))
sys.path.append(os.path.join(code_dir, 'lib'))
sys.path.append(os.path.join(code_dir, 'bin/entity'))
sys.path.append(os.path.join(code_dir, 'bin/dao'))

from utils import Utils
from user_dao import UserDao
from token_controller import TokenController
from exception import InvalidToken, UserNotExist, AuthFailed


class AccessControlController:
    """
    鉴权相关api
    (逻辑较浅, 所以controller和service合在一起写)
    """
    def authenticate(self, user_name: str, password: str) -> str:
        """
        校验用户名密码, 返回token

        Args:
            user_name: 用户名
            password: 密码

        Returns:
            token
        """
        user = UserDao().get_user(user_name=user_name)
        # 用户名不存在
        if not user:
            raise UserNotExist(user_name)
        # 密码错误
        if Utils.calc_md5(password + user.salt) != user.password:
            raise AuthFailed()
        # 签发token
        token = TokenController().sign_token(user)
        return token

    def invalidate(self, auth_token: str) -> None:
        """
        失活token

        Args:
            auth_token: token

        Returns:
            None
        """
        TokenController().invalid_token(auth_token)
