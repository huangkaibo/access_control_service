#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations

import random
import string
import base64
import hashlib


class Utils:
    """
    工具类
    """
    @classmethod
    def calc_md5(cls, s: str) -> str:
        """
        生成md5
        """
        return hashlib.md5(s.encode(encoding='UTF-8')).hexdigest()

    @classmethod
    def calc_base64(cls, s: str) -> str:
        """
        生成base64
        """
        return base64.b64encode(s.encode('utf-8')).decode("utf-8")

    @classmethod
    def parse_base64(cls, s: str) -> str:
        """
        解析base64
        """
        return base64.b64decode(s).decode("utf-8")

    @classmethod
    def generate_random_string(cls, length: int) -> str:
        """
        生成指定长度的随机字符串

        Args:
            length: 字符串长度

        Returns:
            随机字符串
        """
        return ''.join(random.sample(string.ascii_letters + string.digits, length))
