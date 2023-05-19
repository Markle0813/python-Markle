def print_line(char, times):
    print(char * times)


def print_lines(char, times):
    rows = 0
    while rows < 5:
        print_line(char, times)
        rows += 1

name = "Ray"