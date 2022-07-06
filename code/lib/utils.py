#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations

import random
import string
import hashlib


class Utils:
    @classmethod
    def calc_md5(cls, s: str) -> str:
        """
        生成md5
        """
        return hashlib.md5(s.encode(encoding='UTF-8')).hexdigest()

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
