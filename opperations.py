
class TestsforType:

    def __init__(self):
        self.type_test_list = []

    def show(self):
        for i in self.type_test_list:
            print(i)

    def __iter__(self):
        self.index = 0
        return self

    def addition_int(self, N):
        a = 1
        b = 2
        c = 1
        d = 2
        for n in range(N):
            a = b + c; b = a + c; c = a + b; d = c + b; b = c + d

    def subtraction_int(self, N):
        a = 1
        b = 2
        c = 1
        d = 2
        for n in range(N):
            a = b - c; b = a - c; c = a - b; d = c - b; b = c - d

    def multiplication_int(self, N):
        a = 1
        b = 2
        c = 1
        d = 2
        for n in range(N):
            a = b * c; b = a * c; c = a * b; d = c * b; b = c * d

    def division_int(self, N):
        a = 1
        b = 2
        c = 1
        d = 2
        for n in range(N):
            a = b / c; b = a / c; c = a / b; d = c / b; b = c / d

    def addition_float(self, N):
        a = 1.1
        b = 2.2
        c = 1.1
        d = 2.2
        for n in range(N):
            a = b + c; b = a + c; c = a + b; d = c + b; b = c + d

    def subtraction_float(self, N):
        a = 2.2
        b = 1.1
        c = 2.2
        d = 1.1
        for n in range(N):
            a = b - c; b = a - c; c = a - b; d = c - b; b = c - d

    def multiplication_float(self, N):
        a = 1.1
        b = 2.2
        c = 1.1
        d = 2.2
        for n in range(N):
            a = b * c; b = a * c; c = a * b; d = c * b; b = c * d

    def division_float(self, N):
        a = 1.1
        b = 2.2
        c = 1.1
        d = 2.2

        for n in range(N):
            a = b / c; b = a / c; c = a / b; d = c / b; b = c / d

    def addition_comp(self, N):
        a = 1 + 1j
        b = 2 + 2j
        c = 3 + 3j
        d = 4 + 4j
        for n in range(N):
            a = b + c; b = a + c; c = a + b; d = c + b; b = c + d

    def subtraction_comp(self, N):
        a = 1 + 1j
        b = 2 + 2j
        c = 3 + 3j
        d = 4 + 4j
        for n in range(N):
            a = b - c; b = a - c; c = a - b; d = c - b; b = c - d

    def multiplication_comp(self, N):
        a = 1 + 1j
        b = 2 + 2j
        c = 3 + 3j
        d = 4 + 4j
        for n in range(N):
            a = b * c; b = a * c; c = a * b; d = c * b; b = c * d

    def division_comp(self, N, epsilon=1e-10):
        a = 10 + 1j
        b = 20 + 2j
        c = 30 + 3j
        d = 40 + 4j
        for n in range(N):
            if abs(c) > epsilon:
                a = b / c
            else:
                a = 1j

            if abs(a) > epsilon:
                b = a / c
            else:
                b = 1j

            if abs(b) > epsilon:
                c = a / b
            else:
                c = 1j

            if abs(c) > epsilon:
                d = c / b
            else:
                d = 1j

            if abs(d) > epsilon:
                b = c / d
            else:
                b = 1j

