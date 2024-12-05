import unittest
from interpreter import Interpreter
class TestInterpreter(unittest.TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def test_1(self):
        code = "BEGIN x := 5; y := 10; z := x + y; END."
        result = self.interpreter.eval(code)
        self.assertEqual(result["x"], 5)
        self.assertEqual(result["y"], 10)
        self.assertEqual(result["z"], 15)

    def test_2(self):
        code = "BEGIN a := 10; b := 2; c := a + b * 3; d := (a + b) * 3; END."
        result = self.interpreter.eval(code)
        self.assertEqual(result["c"], 16)
        self.assertEqual(result["d"], 36)

    def test_3(self):
        code = "BEGIN a := 5; b := -a; c := +a; END."
        result = self.interpreter.eval(code)
        self.assertEqual(result["b"], -5)
        self.assertEqual(result["c"], 5)

    def test_4(self):
        code = "BEGIN x := 5; y := x + 10; z := y - 3; END."
        result = self.interpreter.eval(code)
        self.assertEqual(result["x"], 5)
        self.assertEqual(result["y"], 15)
        self.assertEqual(result["z"], 12)

    def test_5(self):
        code = "BEGIN END."
        result = self.interpreter.eval(code)
        self.assertEqual(result, {})

    def test_6(self):
        code = """BEGIN x := 2 + 3 * (2 + 3); y := 2 / 2 - 2 + 3 * ((1 + 1) + (1 + 1)); END."""
        result = self.interpreter.eval(code)
        self.assertEqual(result["x"], 2 + 3 * (2 + 3))
        self.assertEqual(result["y"], 2 / 2 - 2 + 3 * ((1 + 1) + (1 + 1)))

    def test_7(self):
        code = """BEGIN y := 2; BEGIN a := 3; a := a; b := 10 + a + 10 * y / 4; c := a - b; END; x := 11; END."""
        result = self.interpreter.eval(code)
        self.assertEqual(result["y"], 2)
        self.assertEqual(result["a"], 3)
        self.assertEqual(result["b"], 18)
        self.assertEqual(result["c"], -15)
        self.assertEqual(result["x"], 11)

if __name__ == "__main__":
    unittest.main()
