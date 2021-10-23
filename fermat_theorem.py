
def theorm(a, b, c, n):
    if n > 2:
        a_b = a**n + b**n
        print(a_b, " = ", c**n)


def main():
    print("howdy")
    theorm(1, 2, 3, 3)
    theorm(80, 20, 3, 3)
    t = [1, 2, 3, 4]
    x = 5
    t = t.append(x)
    print(t)


if __name__ == '__main__':
    main()
