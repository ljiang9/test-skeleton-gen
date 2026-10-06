import unittest

from test_skeleton_gen import generate_skeleton


class TestGen(unittest.TestCase):
    def test_creates_class(self):
        src = "def add(a, b):\n    return a + b\n"
        out = generate_skeleton(src)
        self.assertIn("class TestGenerated(unittest.TestCase):", out)
        self.assertIn("def test_add(self):", out)

    def test_multiple_funcs(self):
        src = "def foo():\n    pass\ndef bar(x):\n    return x\n"
        out = generate_skeleton(src)
        self.assertIn("test_foo", out)
        self.assertIn("test_bar", out)

    def test_imports_unittest(self):
        out = generate_skeleton("def a():\n    pass\n")
        self.assertIn("import unittest", out)
        self.assertIn("unittest.main()", out)

    def test_empty(self):
        out = generate_skeleton("")
        self.assertIn("class TestGenerated", out)

    def test_output_is_python(self):
        out = generate_skeleton("def a():\n    return 1\n")
        compile(out, "<gen>", "exec")


if __name__ == "__main__":
    unittest.main()
