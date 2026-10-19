# ====== LEVEL 1 ======
# 1. Lặp từ 0 đến 10 bằng vòng lặp for và while
print("1. For loop 0 to 10:")
for i in range(11):
    print(i, end=' ')
print()

print("   While loop 0 to 10:")
i = 0
while i <= 10:
    print(i, end=' ')
    i += 1
print()

# 2. Lặp từ 10 về 0 bằng vòng lặp for và while
print("2. For loop 10 down to 0:")
for i in range(10, -1, -1):
    print(i, end=' ')
print()

print("   While loop 10 down to 0:")
i = 10
while i >= 0:
    print(i, end=' ')
    i -= 1
print()

# 3. In hình tam giác gồm 7 dòng ký tự '#'
print("3. Hash triangle:")
for i in range(1, 8):
    print('#' * i)

# 4. Dùng vòng lặp lồng nhau in hình vuông 8x8 dấu '#'
print("4. Hash 8x8 square:")
for row in range(8):
    for col in range(8):
        print('#', end=' ')
    print()

# 5. In bảng nhân lũy thừa dạng '0 x 0 = 0' đến '10 x 10 = 100'
print("5. Multiplication pattern:")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 6. Duyệt qua danh sách và in từng mục
tech_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
print("6. Items in list:")
for item in tech_list:
    print(item)

# 7. Dùng vòng lặp duyệt từ 0 đến 100 và chỉ in số chẵn
print("7. Even numbers from 0 to 100:")
for i in range(0, 101, 2):
    print(i, end=' ')
print()

# 8. Dùng vòng lặp duyệt từ 0 đến 100 và chỉ in số lẻ
print("8. Odd numbers from 0 to 100:")
for i in range(1, 101, 2):
    print(i, end=' ')
print()

# ====== LEVEL 2 ======
# 1. Tính tổng tất cả các số từ 0 đến 100
total_sum = 0
for i in range(101):
    total_sum += i
print(f"L2.1 The sum of all numbers is {total_sum}.")

# 2. Tính tổng các số chẵn và tổng các số lẻ từ 0 đến 100
sum_evens = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i
print(f"L2.2 The sum of all evens is {sum_evens}. And the sum of all odds is {sum_odds}.")

# ====== LEVEL 3 ======
# Dữ liệu danh sách quốc gia mẫu dùng cho Level 3
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

# 1. Trích xuất tất cả các quốc gia có chứa chuỗi 'land'
countries_with_land = []
for c in countries:
    if 'land' in c:
        countries_with_land.append(c)
print("L3.1 Countries containing 'land':", countries_with_land)

# 2. Đảo ngược danh sách hoa quả bằng vòng lặp (không dùng hàm .reverse())
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])
print("L3.2 Reversed fruits without .reverse():", reversed_fruits)