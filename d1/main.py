
def get_password(lines):
    is_zero = 0
    n_zeros = 0
    dial = 50
    for line in lines:
        direction, steps = line[0], int(line[1:])
        sign = -1 if direction == "L" else 1
        start = dial
        result = dial + steps*sign
        dial = result % 100

        for i in range(1, steps + 1):
            if (start +sign*i) % 100 == 0:
                n_zeros += 1

        if result%100 == 0:
            is_zero += 1

    return is_zero, n_zeros

with open("./d1/input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

is_zero, n_zeros = get_password(lines)
print(is_zero, n_zeros)
