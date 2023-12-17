def generate_and_print_points(a, b, c):
    input_numbers = (a, b, c)
    points_list = ['.' * num for num in input_numbers]
    for points in points_list:
        print(points)
    return points_list

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

output_points = generate_and_print_points(a, b, c)
