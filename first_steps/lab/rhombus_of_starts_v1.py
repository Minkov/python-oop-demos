def print_line(spaces_count, stars_count):
    line_spaces = ''.join([' '] * spaces_count)
    line_stars = ' '.join(['*'] * stars_count)
    print(line_spaces + line_stars)


def print_rhombus(n):
    for i in range(n):
        spaces = n - i - 1
        stars = i + 1
        print_line(spaces, stars)

    for i in range(n - 2, -1, -1):
        spaces = n - i - 1
        stars = i + 1
        print_line(spaces, stars)


def print_triangle(n):
    for i in range(n):
        print_line(0, i + 1)


print_rhombus(int(input()))
