class KeyAnalyzer:
    def analyze(self, key: str):
        signs, numbers, current_number = [], [], ""
        i = 0
        while i < len(key):
            if key[i] in ">=<":
                if key[i:i + 2] in {">=", "<=", "<>"}:
                    signs.append(key[i:i + 2])
                    i += 2
                else:
                    signs.append(key[i])
                    i += 1
            elif key[i].isdigit() or key[i] == ".":
                current_number += key[i]
                i += 1
            elif key[i].isspace():
                i += 1
            else:
                if current_number:
                    self._validate_number_format(current_number, key)
                    numbers.append(float(current_number))
                    current_number = ""
                i += 1

        if current_number:
            self._validate_number_format(current_number, key)
            numbers.append(float(current_number))
        if len(signs) != len(numbers):
            raise KeyError("Conditions and numbers count mismatch")
        return signs, numbers
    def _validate_number_format(self, current_number, key):
        if ".." in current_number or current_number.count(".") > 1:
            raise KeyError(f"Bad number format in key: {key}")

class ConditionChecker:
    def check(self, signs, numbers, key, key_numbers):
        for i in range(len(signs)):
            if not key_numbers[i].isdigit():
                return False
            if not self._check_condition(signs[i], key_numbers[i], numbers[i]):
                return False
        return True
    def _check_condition(self, sign, key_number, number):
        if sign == '>':
            return int(key_number) > number
        elif sign == '<':
            return int(key_number) < number
        elif sign == '>=':
            return int(key_number) >= number
        elif sign == '<=':
            return int(key_number) <= number
        elif sign == '=':
            return int(key_number) == number
        elif sign == '<>':
            return int(key_number) != number
        return False

class KeySearcher:
    def search(self, signs, numbers, keys, values):
        result = {}
        for j, key in enumerate(keys):
            key_numbers = key.replace("(", '').replace(")", '').split(', ')
            if len(key_numbers) == len(signs):
                checker = ConditionChecker()
                if checker.check(signs, numbers, key, key_numbers):
                    result[key] = values[j]
        return result
class Dict(dict):
    def __init__(self):
        super().__init__()
        self.keys = []
        self.values = []
        self.iloc = Iloc(self.keys, self.values)
        self.ploc = Ploc(self.keys, self.values)
    def bubble_sort(self):
        n = len(self.keys)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.keys[j] > self.keys[j + 1]:
                    self.keys[j], self.keys[j + 1] = self.keys[j + 1], self.keys[j]
                    self.values[j], self.values[j + 1] = self.values[j + 1], self.values[j]
    def __setitem__(self, key, value):
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
            self.bubble_sort()
        else:
            index = self.keys.index(key)
            self.values[index] = value
        super().__setitem__(key, value)
class Iloc:
    def __init__(self, keys, values):
        self.keys = keys
        self.values = values
    def __getitem__(self, key):
        if isinstance(key, int):
            return self.values[key]
        else:
            raise KeyError("Key must be an integer")
class Ploc:
    def __init__(self, keys, values):
        self.keys = keys
        self.values = values
        self.analyzer = KeyAnalyzer()
        self.searcher = KeySearcher()
    def __getitem__(self, key):
        if isinstance(key, str):
            if len(key) < 2:
                raise KeyError("Key too short")
            signs, numbers = self.analyzer.analyze(key)
            return self.searcher.search(signs, numbers, self.keys, self.values)
        else:
            raise KeyError("Key must be a string")
