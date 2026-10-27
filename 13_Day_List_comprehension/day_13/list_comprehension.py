# ==========================================
# EXERCISES: DAY 13 (LIST COMPREHENSION & LAMBDA)
# ==========================================

# 1. Lọc ra các số âm và số 0 từ danh sách bằng List Comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [i for i in numbers if i <= 0]
print("1. Negative and zero numbers:", negative_and_zero)

# 2. Làm phẳng (flatten) danh sách danh sách thành danh sách một chiều
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [
    num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2
]
print("2. Flattened list:", flattened_list)

# 3. Tạo danh sách các tuples theo mẫu yêu cầu bằng List Comprehension
# Mẫu: (i, 1, i, i**2, i**3, i**4, i**5) với i từ 0 đến 10
tuples_pattern = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("3. Tuples pattern (in 3 phần tử đầu):", tuples_pattern[:3])

# 4. Làm phẳng danh sách các quốc gia và tạo định dạng (Tên in hoa, Tên in hoa viết tắt 3 chữ, Tên in hoa 3 chữ)
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
formatted_countries = [
    [country.upper(), country[:3].upper(), city.upper()]
    for sublist in countries
    for country, city in sublist
]
print("4. Formatted countries:", formatted_countries)

# 5. Chuyển đổi danh sách các quốc gia thành danh sách các dictionaries[cite: 17]
countries_dict_list = [
    {"country": country.upper(), "city": city.upper()}
    for sublist in countries
    for country, city in sublist
]
print("5. Countries list of dicts:", countries_dict_list)

# 6. Chuyển đổi danh sách chuỗi thành danh sách các chuỗi đã nối (concatenate)[cite: 17]
names = [
    ["Asabeneh", "Yetayeh"],
    ["David", "Gundermand"],
    ["John", "Doe"],
    ["Eyob", "Yetter"],
]
full_names = [f"{first} {last}" for first, last in names]
print("6. Full names:", full_names)

# 7. Viết hàm lambda tính hệ số góc (slope) hoặc tung độ gốc (y-intercept) của phương trình đường thẳng[cite: 17]
# Phương trình y = mx + c => slope = m = (y2 - y1) / (x2 - x1)
linear_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print("7. Lambda slope between (2, 2) and (6, 10):", linear_slope(2, 2, 6, 10))