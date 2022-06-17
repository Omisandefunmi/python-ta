import sys
import os


def prime(s):
    count = 0
    for i in range(1, s):
        if s % i == 0:
            count += 1
    if count <= 1:
        return True
    return False


def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
