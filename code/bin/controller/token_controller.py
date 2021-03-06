#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations

import os
import sys
import json
import datetime

current_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
code_dir = os.path.join(current_dir, '../..')
sys.path.append(os.path.join(code_dir, 'bin/db'))
sys.path.append(os.path.join(code_dir, 'lib'))
sys.path.append(os.path.join(code_dir, 'bin/entity'))

from db import db
from utils import Utils
from user_dao import UserDao
from exception import InvalidToken, UserNotExist


class TokenController:
    """
    token相关API
    (逻辑较浅, 所以controller和service合在一起写)
    """
    def __init__(self):
        # 过期时间, 单位秒
        self.EXPIRE = 2

    def sign_token(self, user: 'User') -> str:
        """
        签发token

        Args:
            user: 用户

        Returns:
            token
        """
        # 过期时间
        expire_datetime = datetime.datetime.now() + datetime.timedelta(seconds=self.EXPIRE)
        expire_datetime = expire_datetime.strftime('%Y-%m-%d %H:%M:%S')
        token = {
            'user_id': user.id,
            'expire_datetime': expire_datetime
        }
        token = json.dumps(token)
        token = Utils.calc_base64(token)
        return token

    def parse_token(self, token: str) -> 'User':
        """
        解析token

        Args:
            token: token

        Returns:
            用户实体
        """
        # 已失活
        if token in db.token_black_list:
            raise InvalidToken(token)

        # 解析
        try:
            token = Utils.parse_base64(token)
            token = json.loads(token)
            user_id = token['user_id']
            expire_datetime = token['expire_datetime']
        except:
            raise InvalidToken()

        # 过期
        if datetime.datetime.strptime(expire_datetime, '%Y-%m-%d %H:%M:%S') < datetime.datetime.now():
            raise InvalidToken(token)

        # 获取对应的用户
        user = UserDao().get_user(user_id)
        if not user:
            raise UserNotExist()
        else:
            return user

    def invalid_token(self, token: str) -> None:
        """
        失活token

        Args:
            token: token

        Returns:
            None
        """
        # 本就无效
        if not self.parse_token(token):
            return

        db.token_black_list.append(token)
