# sets ban đầu
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# ====== LEVEL 1 ======
# 1. Find the length of the set it_companies
print("1. length of the set it_companies: ", len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("2. it_companies after adding 'Twitter': ", it_companies)

# 3. Insert multiple IT companies at once (SỬA: truyền vào một list để không bị băm thành ký tự)
it_companies.update(['Nvidia', 'Broadcom', 'TSMC'])
print("3. it_companies after inserting multiple IT companies: ", it_companies)

# 4. Remove one of the companies from the set it_companies
removed_item = it_companies.pop()
print(f"4. it_companies after remove randomly '{removed_item}': ", it_companies)

# 5. What is the difference between remove and discard
print("5. Difference: 'remove()' raises KeyError if the item is not found, whereas 'discard()' does nothing.")


# ====== LEVEL 2 ======
# 1. Join A and B (A hợp B)
join_AB = A.union(B)  # hoặc: A | B
print("1. A joins B = ", join_AB)

# 2. Find A intersection B (A giao B)
intersection_AB = A.intersection(B)  # hoặc: A & B
print("2. A intersects B = ", intersection_AB)

# 3. Is A subset of B (SỬA: Bổ sung câu hỏi bị thiếu)
print("3. Is A subset of B? ", A.issubset(B))

# 4. Are A and B disjoint sets
print("4. Are A and B disjoint sets? ", A.isdisjoint(B))

# 5. What is the symmetric difference between A and B
# (SỬA: Phải tính trước khi làm thay đổi giá trị A, B ở câu sau)
symmetric_diff = A.symmetric_difference(B)  # hoặc: A ^ B
print("5. Symmetric difference between A and B = ", symmetric_diff)

# 6. Join A with B and B with A (làm biến đổi tập hợp gốc)
A_mutated = A.copy()
B_mutated = B.copy()
A_mutated.update(B)
B_mutated.update(A)
print("6. A joins B (mutated) = ", A_mutated)
print("   B joins A (mutated) = ", B_mutated)

# 7. Delete the sets completely
del it_companies, A_mutated, B_mutated


# ====== LEVEL 3 ======
# 1. Convert ages to a set and compare length (SỬA: ép kiểu sang set để lọc trùng)
age_set = set(age)
print(f"1. Length of age list: {len(age)}, Length of age set: {len(age_set)}")
if len(age) > len(age_set):
    print("   => The list is bigger because it contains duplicate elements.")
else:
    print("   => Both have equal length.")

# 2. Giải thích sự khác biệt
# - String: Bất biến (immutable), có thứ tự theo index, chứa văn bản.
# - List: Khả biến (mutable), có thứ tự, cho phép trùng lặp.
# - Tuple: Bất biến (immutable), có thứ tự, cho phép trùng lặp.
# - Set: Khả biến (mutable container), KHÔNG có thứ tự, phần tử là DUY NHẤT và phải hashable.
print("2. Explained data types successfully.")

# 3. Unique words in the sentence (loại bỏ dấu câu nếu có để đếm chuẩn từ)
sentence = "I am a teacher and I love to inspire and teach people."
# Làm sạch dấu chấm ở cuối câu trước khi tách từ
clean_sentence = sentence.replace('.', '')
words_set = set(clean_sentence.split())
print("3. Words set: ", words_set)
print("   Number of unique words: ", len(words_set))