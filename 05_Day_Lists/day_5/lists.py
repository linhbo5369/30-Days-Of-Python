# ==================== LEVEL 1 ====================
# 1
lst = []
# 2
lst = [0, 1, 2, 3, 4, 5]
# 3
print("3. length of lst: ", len(lst))
# 4
print("4. first item of lst: ", lst[0])
print("   middle item of lst: ", lst[len(lst) // 2])
print("   last item of lst: ", lst[-1])
# 5
mixed_data_types = ['Linh', 19, 1.62, {'marital_status': False, 'adress': 'HCMC'}]
# 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# 7
print("7. it_companies: ", it_companies)
# 8
print("8. numbers of companies in the list: ", len(it_companies))
# 9
print("9. first item of lst: ", it_companies[0])
print("   middle item of lst: ", it_companies[len(it_companies) // 2])
print("   last item of lst: ", it_companies[-1])
# 10
it_companies[0] = 'Instagram'
print("10. it_companies after modified: ", it_companies)
# 11
it_companies.append('Telegram')
print("11. it_companies after appending 'Telegram': ", it_companies)
# 12
middle = len(it_companies) // 2
it_companies.insert(middle, 'Spotify');
print("12. it_companies after insert at the middle: ", it_companies)
# 13
it_companies[-2] = it_companies[-2].upper()
print("13. it_companies after uppercase 1 company: ", it_companies)
# 14
joined_companies = '#; '.join(it_companies)
print("14. it_companies_joined: ", joined_companies)
# 15
print("15. 'Google' exists in it_companies? ", 'Google' in it_companies)
# 16
it_companies.sort()
print("16. it_companies after sort(): ", it_companies)
# 17
it_companies.reverse()
print("17. it_companies in descending order: ", it_companies)
# 18
first_3_companies = it_companies[:3]
print("18. the first 3 companies from the list: ", first_3_companies)
# 19
last_3_companies = it_companies[-3:]
print("19. the last 3 companies from the list: ", last_3_companies)
# 20. Slice out the middle IT company or companies from the list
mid_idx = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[mid_idx - 1 : mid_idx + 1]
else:
    middle_companies = it_companies[mid_idx : mid_idx + 1]
print("20. Middle company/companies sliced:", middle_companies)

# 21. Remove the first IT company from the list
del it_companies[0]  # hoặc: it_companies.pop(0)
print("21. it_companies after removing first item:", it_companies)

# 22. Remove the middle IT company or companies from the list
mid_idx = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    del it_companies[mid_idx - 1 : mid_idx + 1]
else:
    del it_companies[mid_idx]
print("22. it_companies after removing middle item:", it_companies)

# 23. Remove the last IT company from the list
it_companies.pop()  # hoặc: del it_companies[-1]
print("23. it_companies after removing last item:", it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print("24. it_companies after clear():", it_companies)

# 25. Destroy the IT companies list
del it_companies
# print(it_companies)  # Dòng này sẽ ném lỗi NameError vì danh sách đã bị hủy hoàn toàn

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print("26. Joined full_stack list:", full_stack)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack.
# Then insert Python and SQL after Redux.
full_stack = full_stack.copy()
redux_idx = full_stack.index('Redux')
full_stack.insert(redux_idx + 1, 'Python')
full_stack.insert(redux_idx + 2, 'SQL')
print("27. full_stack after inserting Python & SQL:", full_stack)


# ==================== LEVEL 2 ====================

# Bài 1: Thao tác với ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1.1 Sắp xếp danh sách và tìm min, max
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"L2.1 Sorted ages: {ages}")
print(f"      Min age: {min_age}, Max age: {max_age}")

# 1.2 Thêm min và max vào lại danh sách
ages.append(min_age)
ages.append(max_age)
print(f"      Ages after adding min & max again: {ages}")

# Sắp xếp lại để tiện tính trung vị (median)
ages.sort()

# 1.3 Tìm tuổi trung vị (median age)
n = len(ages)
if n % 2 == 1:
    median_age = ages[n // 2]
else:
    median_age = (ages[n // 2 - 1] + ages[n // 2]) / 2
print(f"      Median age: {median_age}")

# 1.4 Tìm tuổi trung bình (average age)
average_age = sum(ages) / len(ages)
print(f"      Average age: {average_age:.2f}")

# 1.5 Tìm khoảng biến thiên (range = max - min)
age_range = max_age - min_age
print(f"      Age range: {age_range}")

# 1.6 So sánh giá trị của (min - average) và (max - average) bằng hàm abs()
diff_min = abs(min_age - average_age)
diff_max = abs(max_age - average_age)
print(f"      abs(min - avg): {diff_min:.2f}, abs(max - avg): {diff_max:.2f}")
print(f"      Are the differences equal? {diff_min == diff_max}")

# Bài 2: Countries list
countries = [
    'China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'
]

# 2.1 Tìm quốc gia ở vị trí chính giữa danh sách countries
mid_c = len(countries) // 2
if len(countries) % 2 == 1:
    middle_country = [countries[mid_c]]
else:
    middle_country = countries[mid_c - 1 : mid_c + 1]
print(f"L2.2 Middle country: {middle_country}")

# 2.2 Chia danh sách các quốc gia thành 2 phần bằng nhau (nếu lẻ thì nửa đầu nhiều hơn 1 nước)
half = (len(countries) + 1) // 2
first_half = countries[:half]
second_half = countries[half:]
print(f"      First half countries: {first_half}")
print(f"      Second half countries: {second_half}")

# 2.3 Unpack các nước đầu tiên và phần còn lại làm các nước scandic
first_c, second_c, third_c, *scandic_countries = countries
print(f"      First country: {first_c}, Second: {second_c}, Third: {third_c}")
print(f"      Scandic countries: {scandic_countries}")
