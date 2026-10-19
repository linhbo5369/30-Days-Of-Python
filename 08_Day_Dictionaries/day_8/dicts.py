# 1. Tạo một dictionary rỗng tên là dog
dog = {}
# hoặc: dog = dict()
print("1. Empty dog dict:", dog)

# 2. Thêm name, color, breed, legs, age vào dictionary dog
dog["name"] = "Lu"
dog["color"] = "Brown"
dog["breed"] = "Poodle"
dog["legs"] = 4
dog["age"] = 3
print("2. Dog dict after adding keys:", dog)

# 3. Tạo một student dictionary và thêm: first_name, last_name, gender, age, marital status,
# skills, country, city và address (address là một dictionary con gồm street và zip_code)
student = {
    "first_name": "Linh",
    "last_name": "Nguyen",
    "gender": "Female",
    "age": 20,
    "marital_status": "Single",
    "skills": ["Python", "C++", "SQL"],
    "country": "Vietnam",
    "city": "Hanoi",
    "address": {"street": "Nguyen Trai", "zip_code": "100000"},
}
print("3. Student dict:", student)

# 4. Lấy độ dài (số lượng cặp key-value) của student dictionary
student_length = len(student)
print("4. Length of student dict:", student_length)

# 5. Lấy giá trị của skills và kiểm tra kiểu dữ liệu (phải là list)
skills_val = student.get('skills') # hoặc: student["skills"]
print("5. Skills value:", skills_val)
print("   Skills data type:", type(skills_val))

# 6. Sửa đổi giá trị skills bằng cách thêm 1 hoặc 2 kỹ năng mới
student["skills"].append("Git")
student["skills"].append("Docker")
print("6. Skills after adding items:", student["skills"])

# 7. Lấy danh sách các keys của dictionary dưới dạng list
student_keys = list(student.keys())
print("7. Dictionary keys list:", student_keys)

# 8. Lấy danh sách các values của dictionary dưới dạng list
student_values = list(student.values())
print("8. Dictionary values list:", student_values)

# 9. Chuyển đổi dictionary thành danh sách các tuples bằng items() method
student_items_tuples = list(student.items())
print("9. List of (key, value) tuples:", student_items_tuples)

# 10. Xóa một mục trong dictionary (ví dụ: xóa 'marital_status')
# Dùng pop() để xóa theo key và lấy giá trị ra, hoặc dùng del student['marital_status']
student.pop("marital_status")
print("10. Student dict after deleting 'marital_status':", student)

# 11. Xóa hoàn toàn một trong các dictionaries (ví dụ xóa dog)
del dog
# print(dog)  # Dòng này sẽ ném lỗi NameError vì biến dog đã bị giải phóng hoàn toàn
print("11. Successfully deleted dog dictionary.")