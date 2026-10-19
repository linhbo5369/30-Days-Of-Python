# pi = 3.14159265
# print("Pi: {:.2f}".format(pi))  # Pi: 3.14 (lấy 2 chữ số thập phân)

# # Độ rộng 10 ký tự, căn giữa, lấp đầy khoảng trống bằng '*'
# print("{:*^10}".format("TEST"))  # ***TEST***

# n = 42
# print("Bin: {0:b}, Hex: {0:x}, Oct: {0:o}".format(n))
# Bin: 101010, Hex: 2a, Oct: 52

# salary = 10000000
# print("Lương: {:,} VND".format(salary))  # Lương: 10,000,000 VND

# val = 230.2346
# print("Balance: {:9.3f}".format(val))

# 1. Nối chuỗi 'Thirty', 'Days', 'Of', 'Python' thành một chuỗi duy nhất
print("1.", " ".join(["Thirty", "Days", "Of", "Python"]))

# 2. Nối chuỗi 'Coding', 'For', 'All' thành một chuỗi duy nhất
print("2.", " ".join(["Coding", "For", "All"]))

# 3. Khai báo biến company và gán giá trị ban đầu là "Coding For All"
company = "Coding For All"

# 4. In biến company bằng print()
print("4.", company)

# 5. In độ dài của chuỗi company
print("5. Length:", len(company))

# 6. Đổi toàn bộ chuỗi sang chữ in hoa
print("6. Upper:", company.upper())

# 7. Đổi toàn bộ chuỗi sang chữ in thường
print("7. Lower:", company.lower())

# 8. Định dạng chuỗi bằng các phương thức capitalize(), title(), swapcase()
print("8. Capitalize:", company.capitalize())
print("   Title:", company.title())
print("   Swapcase:", company.swapcase())

# 9. Cắt bỏ (slice out) từ đầu tiên của chuỗi "Coding For All"
# Lấy từ vị trí sau khoảng trắng đầu tiên đến hết chuỗi
first_space_idx = company.find(" ")
print("9. Sliced first word:", company[first_space_idx + 1 :])

# 10. Kiểm tra xem chuỗi có chứa từ "Coding" hay không bằng index/find
print("10. Index of 'Coding':", company.find("Coding"))

# 11. Thay thế từ "Coding" thành "Python"
print("11. Replace 'Coding':", company.replace("Coding", "Python"))

# 12. Đổi 'Python for Everyone' thành 'Python for All' bằng replace
sentence_12 = "Python for Everyone"
print("12. Replace 'Everyone':", sentence_12.replace("Everyone", "All"))

# 13. Tách chuỗi 'Coding For All' thành danh sách bằng split()
print("13. Split by space:", company.split(" "))

# 14. Tách chuỗi các công ty công nghệ lớn bởi dấu phẩy
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("14. Tech companies list:", tech_companies.split(", "))

# 15. Ký tự tại vị trí index 0 trong 'Coding For All'
print("15. Character at index 0:", company[0])

# 16. Ký tự ở vị trí cuối cùng trong 'Coding For All' (dùng index -1)
print("16. Last character:", company[-1])

# 17. Ký tự tại vị trí index 10 trong chuỗi 'Coding For All'
print("17. Character at index 10:", f"'{company[10]}'")  # Ký tự khoảng trắng ' '

# 18. Tạo từ viết tắt (acronym) cho 'Python For Everyone'
pfe = "Python For Everyone"
acronym_pfe = "".join([w[0] for w in pfe.split()])
print("18. Acronym PFE:", acronym_pfe)

# 19. Tạo từ viết tắt cho 'Coding For All'
acronym_cfa = "".join([w[0] for w in company.split()])
print("19. Acronym CFA:", acronym_cfa)

# 20. Dùng index xác định vị trí đầu tiên của ký tự 'C' trong 'Coding For All'
print("20. First index of 'C':", company.index("C"))

# 21. Dùng index xác định vị trí đầu tiên của ký tự 'F' trong 'Coding For All'
print("21. First index of 'F':", company.index("F"))

# 22. Dùng rfind xác định vị trí xuất hiện cuối cùng của 'l' trong 'Coding For All People'
print("22. Last index of 'l':", "Coding For All People".rfind("l"))

# 23. Dùng index hoặc find tìm vị trí xuất hiện đầu tiên của 'because'
sentence_because = (
    "You cannot end a sentence with because because because is a conjunction"
)
print("23. First index of 'because':", sentence_because.find("because"))

# 24. Dùng rindex tìm vị trí xuất hiện cuối cùng của 'because'
print("24. Last index of 'because':", sentence_because.rindex("because"))

# 25. Cắt cụm từ 'because because because' ra khỏi câu
start_idx = sentence_because.find("because")
end_idx = sentence_because.rindex("because") + len("because")
print("25. Sliced phrase:", sentence_because[start_idx:end_idx])

# 26. Tìm vị trí xuất hiện đầu tiên của 'because' (tương tự câu 23)
print("26. Find 'because':", sentence_because.find("because"))

# 27. Cắt cụm 'because because because' (tương tự câu 25)
print("27. Sliced 'because' phrase:", sentence_because[start_idx:end_idx])

# 28. Kiểm tra xem 'Coding For All' có bắt đầu bằng chuỗi con 'Coding' không
print("28. Starts with 'Coding':", company.startswith("Coding"))

# 29. Kiểm tra xem 'Coding For All' có kết thúc bằng chuỗi con 'coding' không (chú ý chữ hoa/thường)
print("29. Ends with 'coding':", company.endswith("coding"))

# 30. Loại bỏ khoảng trắng thừa ở hai đầu chuỗi '   Coding For All      '
raw_company = "   Coding For All      "
print("30. Stripped string:", f"'{raw_company.strip()}'")

# 31. Kiểm tra biến hợp lệ bằng isidentifier()
print("31. '30DaysOfPython' is identifier?:", "30DaysOfPython".isidentifier())  # False (bắt đầu bằng số)
print("    'thirty_days_of_python' is identifier?:", "thirty_days_of_python".isidentifier())  # True

# 32. Nối danh sách các thư viện Python bằng chuỗi '# '
libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("32. Joined libraries:", "# ".join(libraries))

# 33. Dùng escape sequence để in chuỗi ngắt dòng
print("33. Newline escape sequence:\nI am enjoying this challenge.\nI just wonder what is next.")

# 34. Dùng escape sequence tab (\t) để in bảng
print("34. Tab escape sequence:")
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 35. Định dạng chuỗi hiển thị diện tích hình tròn bằng format hoặc f-string
radius = 10
area = 3.14 * radius**2
print("35. radius = 10")
print("    area = 3.14 * radius ** 2")
print(f"    The area of a circle with radius {radius} is {area:.0f} meters square.")

# 36. Định dạng chuỗi in ra các phép tính số học
a, b = 8, 6
print("36. Arithmetic operations:")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")