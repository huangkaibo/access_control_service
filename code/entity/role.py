#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations


class Role:
    """
    角色实体类
    """

    def __init__(self, id: str, name: str) -> None:
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        if isinstance(id, str):
            self.__id = id
        else:
            raise TypeError('role_id不是字符串类型')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError('role_name不是字符串类型')
