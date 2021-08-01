class Vector:
    def __init__(self,*args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]

    def __sub__(self, other):
        if isinstance(other, int):
            if other >= len(self.values):
                self.values = []
                return self.values
            for i in range(other):
                self.values.pop()
            return self.values

    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        elif key > len(self.values):
            diff = key - len(self.values)
            self.values.extend([0]* diff)
            self.values.append(value)
