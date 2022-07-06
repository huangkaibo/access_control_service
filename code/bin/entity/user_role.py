#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations
from datetime import datetime


class UserRole:
    """
    用户-角色实体类
    """

    def __init__(
        self,
        id: str,
        user_id: str,
        role_id: str,
        enabled: bool,
        create_time: datetime,
        modify_time: datetime
    ) -> None:
        self.__id = id
        self.__user_id = user_id
        self.__role_id = role_id
        self.__enabled = enabled
        self.__create_time = create_time
        self.__modify_time = modify_time

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        if isinstance(id, str):
            self.__id = id
        else:
            raise TypeError('id不是字符串类型')

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id: str):
        if isinstance(user_id, str):
            self.__user_id = user_id
        else:
            raise TypeError('user_id不是字符串类型')

    @property
    def role_id(self):
        return self.__role_id

    @role_id.setter
    def role_id(self, role_id: str):
        if isinstance(role_id, str):
            self.__role_id = role_id
        else:
            raise TypeError('role_id不是字符串类型')

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        if isinstance(enabled, bool):
            self.__enabled = enabled
        else:
            raise TypeError('enabled不是bool类型')

    @property
    def create_time(self):
        return self.__create_time

    @create_time.setter
    def create_time(self, create_time: datetime):
        if isinstance(create_time, datetime):
            self.__create_time = create_time
        else:
            raise TypeError('create_time不是datetime类型')

    @property
    def modify_time(self):
        return self.__modify_time

    @modify_time.setter
    def modify_time(self, modify_time: datetime):
        if isinstance(modify_time, datetime):
            self.__create_time = modify_time
        else:
            raise TypeError('modify_time不是datetime类型')
