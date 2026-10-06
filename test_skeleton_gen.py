#!/usr/bin/env python3
"""test_skeleton_gen —— 从 Python 函数定义生成 unittest 测试骨架。

用 ast 解析源码中的顶层函数，为每个函数生成
`def test_<name>(self):` 占位方法。零第三方依赖。

用法：
    from test_skeleton_gen import generate_skeleton
    print(generate_skeleton(source_code))
"""
from __future__ import annotations

import argparse
import ast
import sys


def generate_skeleton(source: str) -> str:
    tree = ast.parse(source)
    funcs = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    imports = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.ImportFrom) and n.module:
            imports.add(n.module)
    lines = ["import unittest", ""]
    for mod in sorted(imports):
        lines.append(f"from {mod} import *  # noqa")
    lines.append("")
    lines.append("class TestGenerated(unittest.TestCase):")
    for f in funcs:
        lines.append(f"    def test_{f}(self):")
        lines.append(f"        # TODO: 为 {f} 补充断言")
        lines.append(f"        pass")
    if not funcs:
        lines.append("    pass")
    lines.append("")
    lines.append('if __name__ == "__main__":')
    lines.append("    unittest.main()")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="函数 -> unittest 骨架")
    p.add_argument("--file", required=True, help="待解析的 Python 文件")
    args = p.parse_args(argv)
    with open(args.file, encoding="utf-8") as f:
        src = f.read()
    print(generate_skeleton(src))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
