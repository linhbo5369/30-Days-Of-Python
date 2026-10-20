import random
import string

# ==========================================
# EXERCISES: LEVEL 1
# ==========================================

# 1. Hàm sinh mã user ID ngẫu nhiên gồm 6 ký tự (chữ và số)
def random_user_id():
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(6))


print("L1.1 Single User ID:", random_user_id())


# 2. Hàm user_id_gen_by_user(): nhận số lượng ký tự và số lượng ID cần tạo từ người dùng
def user_id_gen_by_user():
    # Nhập độ dài của mỗi ID và số lượng ID muốn tạo
    char_count = int(input("Enter number of characters for user_id: "))
    id_count = int(input("Enter number of IDs to generate: "))

    chars = string.ascii_letters + string.digits
    generated_ids = []

    for _ in range(id_count):
        uid = "".join(random.choice(chars) for _ in range(char_count))
        generated_ids.append(uid)

    return "\n".join(generated_ids)


# Chạy thử hàm 2 (mở comment khi chạy tương tác):
# print("L1.2 Generated IDs:\n" + user_id_gen_by_user())


# 3. Hàm rgb_color_gen(): sinh mã màu RGB ngẫu nhiên dạng rgb(r, g, b)
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"


print("L1.3 RGB color:", rgb_color_gen())


# ==========================================
# EXERCISES: LEVEL 2
# ==========================================


# 1. Hàm list_of_hexa_colors(num): trả về danh sách num mã màu Hex ngẫu nhiên
def list_of_hexa_colors(num):
    hex_digits = "0123456789abcdef"
    colors = []
    for _ in range(num):
        hex_code = "#" + "".join(random.choice(hex_digits) for _ in range(6))
        colors.append(hex_code)
    return colors


print("L2.1 Hex colors list:", list_of_hexa_colors(3))


# 2. Hàm list_of_rgb_colors(num): trả về danh sách num mã màu RGB ngẫu nhiên
def list_of_rgb_colors(num):
    return [rgb_color_gen() for _ in range(num)]


print("L2.2 RGB colors list:", list_of_rgb_colors(3))


# 3. Hàm generate_colors(color_type, num): sinh màu tùy biến theo định dạng
def generate_colors(color_type, num):
    if color_type == "hexa":
        return list_of_hexa_colors(num)
    elif color_type == "rgb":
        return list_of_rgb_colors(num)
    else:
        return "Invalid color type. Choose 'hexa' or 'rgb'."


print("L2.3 Custom generate_colors ('hexa', 3):", generate_colors("hexa", 3))
print("     Custom generate_colors ('rgb', 2):", generate_colors("rgb", 2))


# ==========================================
# EXERCISES: LEVEL 3
# ==========================================


# 1. Hàm shuffle_list(lst): xáo trộn ngẫu nhiên các phần tử trong danh sách
def shuffle_list(lst):
    copied_lst = lst.copy()
    random.shuffle(copied_lst)
    return copied_lst


test_list = [1, 2, 3, 4, 5, 6, 7]
print("L3.1 Shuffled list:", shuffle_list(test_list))


# 2. Hàm trả về mảng gồm 7 số ngẫu nhiên DUY NHẤT trong khoảng từ 0 đến 9
def seven_random_unique_numbers():
    # Dùng random.sample để chọn không hoàn lại (không trùng lặp)
    return random.sample(range(10), 7)


print("L3.2 Seven unique numbers (0-9):", seven_random_unique_numbers())