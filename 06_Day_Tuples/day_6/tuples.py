# ==========================================
# EXERCISES: LEVEL 1
# ==========================================

# 1. Tạo một tuple rỗng
empty_tuple = ()
# hoặc: empty_tuple = tuple()
print("1. Empty tuple:", empty_tuple)

# 2. Tạo một tuple chứa tên các chị em gái và một tuple chứa tên các anh em trai
sisters = ("Hoa", "Lan", "Mai")
brothers = ("Nam", "Minh", "Tuan")
print("2. Sisters:", sisters)
print("   Brothers:", brothers)

# 3. Gộp (nối) hai tuple anh em trai và chị em gái lại thành siblings
siblings = sisters + brothers
print("3. Siblings:", siblings)

# 4. Đếm số lượng anh chị em trong tuple siblings
num_siblings = len(siblings)
print("4. Number of siblings:", num_siblings)

# 5. Sửa đổi tuple siblings và thêm tên bố mẹ để tạo thành family_members
# Vì tuple là bất biến (immutable), ta cần chuyển sang list hoặc nối tuple mới
parents = ("Father", "Mother")
family_members = parents + siblings
print("5. Family members:", family_members)


# ==========================================
# EXERCISES: LEVEL 2
# ==========================================

# 1. Giải nén (unpack) siblings và parents từ family_members
# 2 phần tử đầu là parents, toàn bộ phần còn lại là siblings
father, mother, *unpacked_siblings = family_members
parents_unpacked = (father, mother)
siblings_unpacked = tuple(unpacked_siblings)
print("L2.1 Parents:", parents_unpacked)
print("     Siblings:", siblings_unpacked)

# 2. Tạo các tuple fruits, vegetables, animal_products. Sau đó gộp lại thành food_stuff_tp
fruits = ("banana", "apple", "mango", "orange")
vegetables = ("tomato", "potato", "cabbage", "onion", "carrot")
animal_products = ("beef", "milk", "cheese", "egg")

food_stuff_tp = fruits + vegetables + animal_products
print("L2.2 Food stuff tuple:", food_stuff_tp)

# 3. Chuyển đổi food_stuff_tp thành một danh sách (list): food_stuff_lt
food_stuff_lt = list(food_stuff_tp)
print("L2.3 Food stuff list:", food_stuff_lt)

# 4. Cắt ra phần tử (hoặc các phần tử) ở chính giữa từ food_stuff_tp hoặc food_stuff_lt
n = len(food_stuff_tp)
mid_idx = n // 2
if n % 2 == 1:
    middle_items = food_stuff_tp[mid_idx : mid_idx + 1]
else:
    middle_items = food_stuff_tp[mid_idx - 1 : mid_idx + 1]
print("L2.4 Middle item(s):", middle_items)

# 5. Cắt ra 3 phần tử đầu tiên và 3 phần tử cuối cùng từ danh sách food_stuff_lt
first_3_items = food_stuff_lt[:3]
last_3_items = food_stuff_lt[-3:]
print("L2.5 First 3 items:", first_3_items)
print("     Last 3 items:", last_3_items)

# 6. Xóa hoàn toàn tuple food_stuff_tp
del food_stuff_tp
# print(food_stuff_tp)  # Sẽ gây lỗi NameError vì tuple đã bị xóa khỏi bộ nhớ

# 7. Kiểm tra xem một phần tử có tồn tại trong tuple không
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

# 7.a. Kiểm tra 'Estonia' có phải là quốc gia Bắc Âu không
print("L2.7a. Is 'Estonia' a nordic country?:", "Estonia" in nordic_countries)

# 7.b. Kiểm tra 'Iceland' có phải là quốc gia Bắc Âu không
print("L2.7b. Is 'Iceland' a nordic country?:", "Iceland" in nordic_countries)