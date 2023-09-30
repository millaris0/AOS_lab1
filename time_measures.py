import timeit
from opperations import TestsforType


def table(lst_time):
    types = ['int', 'float', 'complex']
    oppers = ['+', '-', '*', '/']
    results = []

    max_op_len = max(len(op) for op in oppers)
    max_type_len = max(len(t) for t in types)

    for t in types:
        max_time = max(lst_time[types.index(t) * len(oppers):(types.index(t) + 1) * len(oppers)])

        for op in oppers:
            index = oppers.index(op) + types.index(t) * len(oppers)
            op_time = lst_time[index]

            percentage = (op_time / max_time) * 100 if max_time > 0 else 0

            formatted_time = "{:.6e}".format(op_time)
            result_str = f"{op.ljust(max_op_len)}\t{t.ljust(max_type_len)}\t{formatted_time}\t{percentage:.2f}%"
            results.append(result_str)

    return results


def main():
    N = 50000

    execution_time1 = timeit.timeit(lambda: TestsforType().addition_int(N), number=10)

    execution_time2 = timeit.timeit(lambda: TestsforType().subtraction_int(N), number=10)

    execution_time3 = timeit.timeit(lambda: TestsforType().multiplication_int(10), number=10)

    execution_time4 = timeit.timeit(lambda: TestsforType().division_int(10), number=10)

    execution_time5 = timeit.timeit(lambda: TestsforType().addition_float(N), number=10)

    execution_time6 = timeit.timeit(lambda: TestsforType().subtraction_float(N), number=10)

    execution_time7 = timeit.timeit(lambda: TestsforType().multiplication_float(10), number=10)

    execution_time8 = timeit.timeit(lambda: TestsforType().division_float(10), number=10)

    execution_time9 = timeit.timeit(lambda: TestsforType().addition_comp(N), number=10)

    execution_time10 = timeit.timeit(lambda: TestsforType().subtraction_comp(N), number=10)

    execution_time11 = timeit.timeit(lambda: TestsforType().multiplication_comp(10), number=10)

    execution_time12 = timeit.timeit(lambda: TestsforType().division_comp(10), number=10)

    lst_time = [(N*10)/execution_time1, (N*10)/execution_time2, 10/execution_time3, 10/execution_time4,
                (N*10)/execution_time5, (N*10)/execution_time6, 10/execution_time7, 10/execution_time8,
                (N*10)/execution_time9, (N*10)/execution_time10, 10/execution_time11, 10/execution_time12]

    results = table(lst_time)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()