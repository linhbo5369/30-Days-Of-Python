import math

my_age = 19
my_height = 1.62
solution = 1 + 3j

base = int(input('Enter base: '))
height = int(input('Enter height: '))
area_of_triangle = 0.5 * base * height
print('The area of the triangle is {:.0f}'.format(area_of_triangle))

a, b, c = [int(input(f'Enter side {side}: ')) for side in ('a', 'b', 'c')]
perimeter_of_triangle = a + b + c
print(f'The permeter of the triangle is {perimeter_of_triangle}')

l, w = [int(input(f'Enter {attr} of rectangle')) for attr in ('length', 'width')]
area_of_rectangle = l * w
perimeter_of_rectangle = (l + w) * 2
for key, value in zip(('area', 'perimeter'), (area_of_rectangle, perimeter_of_rectangle)):
    print(f'The {key} of the rectangle is {value}')

# circle (done day_2) -> skip

def f(x):
    return 2 * x - 2

x_a, x_b = 0, 1
slope_8 = (f(x_b) - f(x_a)) / (x_b - x_a)
y_intercept = f(0)
x_intercept = -y_intercept / slope_8
print(f"8. Slope: {slope_8}")
print(f"y-intercept: {y_intercept}")
print(f"x-intercept: {x_intercept}")

x1, y1 = 2, 2
x2, y2 = 6, 10
slope_9 = (y2 - y1) / (x2 - x1)
euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"\n9. Slope: {slope_9}\n Distance: {euclidean_distance}")

print("10. Slopes are equal:", slope_8 == slope_9)

for x in [-5, -4, -3, -2, -1, 0]:
    y = x**2 + 6*x + 9
    print(f"x = {x}, y = {y}")

len_python = len('python')
len_dragon = len('dragon')
print("12. Falsy statement:", len_python != len_dragon)

# Bài 13: Dùng toán tử 'and' kiểm tra 'on'
print("13. 'on' in both:", ('on' in 'python') and ('on' in 'dragon'))

# Bài 14: Kiểm tra 'jargon' trong câu
sentence = "I hope this course is not full of jargon."
print("14. 'jargon' in sentence:", 'jargon' in sentence)

# Bài 15: Kiểm tra 'không có on trong cả hai'
print("15. No 'on' in both:", ('on' not in 'python') and ('on' not in 'dragon'))

# Bài 16: len -> float -> str
length_val = len('python')     # 6
float_val = float(length_val)  # 6.0
str_val = str(float_val)       # '6.0'
print(f"16. Result: {str_val}, Type: {type(str_val)}")

# Bài 17: Kiểm tra số chẵn
num = 14
is_even = (num % 2 == 0)
print(f"17. Is {num} even?:", is_even)

# Bài 18: Floor division 7 by 3 và int(2.7)
floor_div = 7 // 3  # 2
int_val = int(2.7)  # 2
print("18. Equal:", floor_div == int_val)

# Bài 19: So sánh type('10') và type(10)
print("19. Type equal:", type('10') == type(10))  # str vs int => False

# Bài 20: int('9.8') == 10
# Chú ý: int('9.8') sẽ gây lỗi ValueError vì không thể ép chuỗi float trực tiếp về int!
try:
    print("20.", int('9.8') == 10)
except ValueError as e:
    print("20. Error:", e)  # Cần sửa thành: int(float('9.8')) == 10

# Bài 21: Tính lương hàng tuần
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
print(f"Your weekly earning is {int(hours * rate)}")

# Bài 22: Tính số giây sống (1 năm quy chuẩn = 365 ngày = 31,536,000 giây)
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print(f"You have lived for {seconds} seconds.")

# Bài 23: In bảng lũy thừa (x, 1, x^1, x^2, x^3)
for i in range(1, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")