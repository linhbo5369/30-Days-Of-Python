# ==========================================
# EXERCISES: LEVEL 1
# ==========================================

# 1. Nhập tuổi người dùng, kiểm tra đủ điều kiện lái xe (18 tuổi trở lên)
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_needed = 18 - user_age
    print(f"You need {years_needed} more years to learn to drive.")

# 2. So sánh tuổi của người dùng với my_age (ví dụ my_age = 25)
my_age = 25
your_age = int(input("Enter your age: "))
if your_age > my_age:
    diff = your_age - my_age
    print(f"You are {diff} {'year' if diff == 1 else 'years'} older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    print(f"I am {diff} {'year' if diff == 1 else 'years'} older than you.")
else:
    print("We are the same age!")

# 3. Nhập hai số a và b, so sánh xem số nào lớn hơn
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


# ==========================================
# EXERCISES: LEVEL 2
# ==========================================

# 1. Xếp loại điểm số của học sinh (A: 80-100, B: 70-89..., theo thang điểm đề bài)
score = int(input("Enter your score (0 - 100): "))
if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score <= 79:
    grade = 'B'
elif 60 <= score <= 69:
    grade = 'C'
elif 50 <= score <= 59:
    grade = 'D'
elif 0 <= score <= 49:
    grade = 'F'
else:
    grade = "Invalid score"
print(f"Grade: {grade}")

# 2. Kiểm tra mùa dựa trên tháng người dùng nhập
# Thu: Autumn (September, October, November)
# Đông: Winter (December, January, February)
# Xuân: Spring (March, April, May)
# Hạ: Summer (June, July, August)
month = input("Enter a month: ").strip().capitalize()
if month in ['September', 'October', 'November']:
    print("The season is Autumn.")
elif month in ['December', 'January', 'February']:
    print("The season is Winter.")
elif month in ['March', 'April', 'May']:
    print("The season is Spring.")
elif month in ['June', 'July', 'August']:
    print("The season is Summer.")
else:
    print("Invalid month entered.")

# 3. Thêm hoa quả vào danh sách nếu chưa tồn tại
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").strip().lower()

if new_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(new_fruit)
    print("Updated fruit list:", fruits)


# ==========================================
# EXERCISES: LEVEL 3
# ==========================================

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Yêu cầu 1: Kiểm tra khóa 'skills' có tồn tại không. Nếu có, in ra kỹ năng ở chính giữa
if 'skills' in person:
    skills = person['skills']
    mid_idx = len(skills) // 2
    print("Middle skill:", skills[mid_idx])

# Yêu cầu 2: Kiểm tra người đó có kỹ năng 'Python' hay không
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("Has Python skill?:", has_python)

# Yêu cầu 3: Xác định chức danh dựa trên danh sách kỹ năng
# - Chỉ có JavaScript và React -> front-end developer
# - Có Node, Python, MongoDB -> fullstack developer
# - Có React, Node, MongoDB -> backend developer
if 'skills' in person:
    skills_set = set(person['skills'])
    if skills_set == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        print("He is a fullstack developer")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print("He is a backend developer")
    else:
        print("Unknown title")

# Yêu cầu 4: Kiểm tra tình trạng hôn nhân và nơi sống
# Nếu người đó đã kết hôn và sống ở Finland, in ra theo định dạng yêu cầu
if person.get('is_marred') and person.get('country') == 'Finland':
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name} lives in Finland. He is married.")