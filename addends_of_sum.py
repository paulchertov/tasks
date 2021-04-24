from typing import List, Optional
from enum import Enum
from datetime import datetime


def AAA(i: int, n: int) -> List[List[int]]:
    """
    Function that returns all possible combinations of i integer addends
    that will have sum = n
    :param i: number of addends in combination
    :param n: row to process (added for compatibility), may be omitted
    :return: list where each element is a list of i integers, sum of each element is n
    """
    if i < 0:
        raise ValueError("i should be greater than 0")
    elif i == 1:
        return [n]
    if n < 1:
        raise ValueError("n should be greater than 0")

    ite = 0  # debug iterations counter
    res = []
    leftmost = n - i + 1
    while leftmost:
        dt = datetime.now()
        print(f"leftmost={leftmost} datetime={dt}, ite={ite}")
        col_no = 0
        prev = None
        current = leftmost
        row_sum = 0
        prev_cols = []
        revert = False
        brk = False
        while True:
            """
            Finite state machine with 4 states:
                 break - exit
                 revert - go back over stack to decrement value
                 write row - add value to the result, and go to revert
                 proceed - write value into the next column 
            """
            ite += 1

            if brk:
                break
            elif revert:
                col_no -= 1
                row_sum -= prev
                current = prev_cols.pop()
                if not prev_cols:
                    brk = True
                    break
                prev = prev_cols[-1]
                revert = current > prev or current < 2
                if not revert:
                    current -= 1
            elif col_no == (i - 1):  # write row
                if (row_sum + current) == n:
                    row = prev_cols + [current]
                    res.append(row)
                revert = True
            else:  # proceed
                col_no += 1
                row_sum += current
                prev = current
                nxt = min(current, (n + 1 - row_sum - i + col_no))

                prev_cols.append(current)
                current = nxt
                """
                if it is impossible to fit to n with all remaining elements 
                with max value (value of next element) we switch state
                """
                if (n - row_sum) > nxt * (i - col_no):
                    if prev_cols:
                        revert = True
                    else:
                        brk = True

        leftmost -= 1
    print(f"iterations: {ite}")
    return res


rs = AAA(5, 300)
print(len(rs))