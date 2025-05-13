# https://projecteuler.net/problem=48


def problem_48_answer(n: int = 1_000, n_digits: int = 10):
    m = 10**n_digits
    s = 0
    for i in range(1, n + 1):
        s += pow(i, i, m)
        s %= m

    return s


if __name__ == "__main__":
    print(problem_48_answer())
