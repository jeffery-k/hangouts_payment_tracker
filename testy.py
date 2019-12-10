
def ting(*args):
    for arg in args:
        yield from funcOne(arg)
        yield from funcTwo(arg)


def funcOne(arg):
    for i in range(10):
        yield "funcOne says: " + arg


def funcTwo(arg):
    for i in range(10):
        yield "funcTwo says: " + arg


def main():
    for blink in ting("tong", "tim", "tinny"):
        print(blink)
    flem = 0


if __name__ == '__main__':
    main()