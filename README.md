# test-skeleton-gen

解析 Python 函数定义，自动生成 **unittest 测试骨架**。用标准库 `ast`，零依赖。

## 功能简介

- `generate_skeleton(source)`：为每个顶层函数生成 `def test_<name>(self):`；
- 自动带上 `import unittest` 与 `unittest.main()`；
- 生成结果可直接 `python3` 运行。

## 快速开始

```bash
python3 test_skeleton_gen.py --file your_module.py
```

作为库：

```python
from test_skeleton_gen import generate_skeleton
print(generate_skeleton("def add(a, b):\n    return a + b\n"))
```

## 无 API key 如何运行

纯 ast 解析，**不需要任何 API key**。

## 目录结构

```
test-skeleton-gen/
├── test_skeleton_gen.py
├── tests/test_test_skeleton_gen.py
├── README.md / LICENSE / .gitignore
```

## 运行测试

```bash
python3 -m unittest discover -s tests -v
```

## 许可证

[MIT](./LICENSE) © 2026 ljiang9
