# 简介

鉴权服务, 作者: 黄凯博

需求调研文档、设计文档详见document文件夹

# 依赖

* 环境依赖: python3.10
* 包依赖: 无

# 测试方法

```bash
cd access_control_service/code/tests
python3 -m unittest
```

或单独运行每个测试文件

# 目录

```
access_control_service
│  .gitignore
│  README.md
│  
├─code: 源代码
│  ├─bin
│  │  ├─controller: api
│  │  │      access_control_controller.py: 鉴权相关api
│  │  │      role_controller.py: 角色控制相关API
│  │  │      token_controller.py: token相关API
│  │  │      user_controller.py: 用户相关API
│  │  │      user_role_controller.py: 用户-角色关系相关API
│  │  │
│  │  ├─dao: 各数据的curd
│  │  │      role_dao.py
│  │  │      user_dao.py
│  │  │      user_role_dao.py
│  │  │
│  │  ├─db: 存在内存的数据
│  │  │      db.py
│  │  │
│  │  └─entity: 实体
│  │          role.py
│  │          user.py
│  │          user_role.py
│  │
│  ├─lib
│  │      exception.py
│  │      utils.py
│  │
│  └─tests: 测试用例
│          test_access_control.py
│          test_role.py
│          test_user.py
│          test_user_role.py
│
└─document
        设计文档.docx
        需求调研文档.docx
```