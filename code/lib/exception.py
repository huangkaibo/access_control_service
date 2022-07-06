#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations


class InvalidToken(Exception):
    """
    token无效
    """

    def __init__(self, token: any) -> None:
        super().__init__(token)
        self.token = token

    def __str__(self) -> str:
        return f"异常: token无效({self.token})"


class UserExist(Exception):
    """
    用户已存在
    """

    def __init__(self, user_name: str) -> None:
        super().__init__(user_name)
        self.user_name = user_name

    def __str__(self) -> str:
        return f"异常: 用户已存在({self.user_name})"


class UserNotExist(Exception):
    """
    用户不存在
    """

    def __init__(self, user_name: str) -> None:
        super().__init__(user_name)
        self.user_name = user_name

    def __str__(self) -> str:
        return f"异常: 用户不存在({self.user_name})"


class RoleExist(Exception):
    """
    角色已存在
    """

    def __init__(self, role_name: str) -> None:
        super().__init__(role_name)
        self.role_name = role_name

    def __str__(self) -> str:
        return f"异常: 角色存在({self.role_name})"


class RoleNotExist(Exception):
    """
    角色不存在
    """

    def __init__(self, role_name: str) -> None:
        super().__init__(role_name)
        self.role_name = role_name

    def __str__(self) -> str:
        return f"异常: 角色不存在({self.role_name})"


class AuthFailed(Exception):
    """
    用户名密码校验失败
    """

    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return f"异常: 用户名密码校验失败"
