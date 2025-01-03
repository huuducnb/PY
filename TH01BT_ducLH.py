#Xin chào 
print("Hello word")

# hiển thị thông báo chào mừng 
print("Chào mừng bạn đến với ngôn ngữ Python ")

# Nhập tên vào biến name 
name = input("nhập họ và tên :")
# Hiển thị thông báo 
print ('Chúc bạn ' , name , 'sẽ công với ngôn ngữ python ')
# ví dụ tiếp theo 
# Nhập giá trị cho a và b
a = 9
b = 5

# Thực hiện các phép toán và in kết quả
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b

print("Tổng a + b =", tong)
print("Hiệu a - b =", hieu)
print("Tích a * b =", tich)
print("Thương a / b =", thuong)
# vd 38 
# Define variables
a = 52348252488
b = 523482034
c = 545354645577

# Calculate and print the sum of a and b
d = a + b
print(d)  # Output: 52871734442

# Calculate and print the sum of d and c
e = d + c
print(e)  # Output: 598226380019
# ví dụ 46 
# Define variables
a = 10
b = 8
tong = a + b
print("Tổng của hai số =", tong)  # Output: Tổng của hai số = 18

hieu = a - b
print("Hiệu của hai số =", hieu)  # Output: Hiệu của hai số = 2

tich = a * b
print("Tích của hai số =", tich)  # Output: Tích của hai số = 80

thuong = a / b
print("Thương của hai số =", thuong)  # Output: Thương của hai số = 1.25

thuong_nguyen = a // b
print("Phép chia lấy phần nguyên =", thuong_nguyen)  # Output: Phép chia lấy phần nguyên = 1

thuong_du = a % b
print("Phép chia lấy phần dư =", thuong_du)  # Output: Phép chia lấy phần dư = 2

mu = a ** b
print("Tính giá trị a lũy thừa b =", mu)  # Output: Tính giá trị a lũy thừa b = 100000000
# ví dụ 52 
st = 'HUMG là Trường đại học hàng đầu tại Việt Nam'
x = 'HUMG' in st
y = 'Python' in st

print('Kết quả kiểm tra HUMG:', x)
print('Kết quả kiểm tra Python:', y)

# ví dụ 62 
hoc_sinh = ['Lê Thùy Dung', 'Trần Đức Hùng', 'Nguyễn Lan Anh', 'Mai Phương Thúy']
print(hoc_sinh)
diem = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
print(diem)
list_so = [9, 5, 8, 13, 0, 4, 7, -9, 11]
print(list_so)
person_info = ['Mary', 1998, 'Tokyo, Japan', 1.70, 65]
print(person_info)
list_rong = []
print(list_rong) 
# ví dụ 63 
# Truy xuất dữ liệu trong danh sách:
# Hiển thị tên học sinh ở vị trí thứ 3
print('Học sinh vị trí thứ 3: ', hoc_sinh[2])

# Hiển thị tên người - chiều cao trong biến person_info
print('Họ tên:', person_info[0], '---Chiều cao:', person_info[3])

# Truy xuất nhiều phần tử trong danh sách
print(list_so[3:8])
# ví dụ 65 
# Define two lists
list_a = [8, 4, 8, 2]
list_b = [3, 0, 7, 6, 5]

# Concatenate the lists
list_ab = list_a + list_b

# Print the concatenated list
print('List mới:', list_ab)

# Get the length of the concatenated list
length_list_ab = len(list_ab)

# Print the length of the list
print(list_ab, 'Có số phần tử là:', length_list_ab)

# ví dụ 66
# Define the list
list_ab = [8, 4, 8, 2, 3, 0, 7, 6, 5]

# Check if 0 is in the list
bol_0 = 0 in list_ab
print('Phần tử 0 có thuộc list_ab?', bol_0)

# Check if 9 is in the list
bol_9 = 9 in list_ab
print('Phần tử 9 có thuộc list_ab?', bol_9)

# ví dụ 67
# Define the list
list_ab = [8, 4, 8, 2, 3, 0, 7, 6, 5]

# Print the original list
print('Danh sách ban đầu:\n', list_ab)

# Add an element to the end of the list
list_ab.append(10)
print('Danh sách thêm vào cuối:\n', list_ab)

# Add an element at a specific position
list_ab.insert(1, 100)
print('Danh sách thêm vào vị trí thứ 2:\n', list_ab)

# ví dụ 69
# Define the list
list_ab = [8, 100, 4, 8, 2, 3, 0, 7, 6, 5, 10]

print('Danh sách ban đầu:\n', list_ab)

list_ab.pop()
print('Danh sách xóa phần tử cuối:\n', list_ab)

del list_ab[1]
print('Danh sách xóa phần tử ở vị trí số 2:\n', list_ab)

list_ab.remove(0)
print('Xóa phần tử có giá trị 0 đầu tiên:\n', list_ab) 
# ví dụ 70
# Define the list
list_ab = [8, 4, 8, 2, 3, 7, 6, 5]

# Print the original list
print('Danh sách ban đầu:\n', list_ab)

# Count the occurrences of 8 in the list
count_8 = list_ab.count(8)
print('Số 8 xuất hiện:', count_8)

# Count the occurrences of 1 in the list
count_1 = list_ab.count(1)
print('Số 1 xuất hiện:', count_1)

# ví dụ 71 
# Declare variables
a = 10
b = a  # Assign the value of a to b

# Change the value of b
b = 5

# Print the values of a and b
print('Giá trị của biến a:', a)
print('Giá trị của biến b:', b)

# ví dụ 72 
# Create a copy of the list
ds_a = [4, 5, 8, 9] 
ds_b = ds_a.copy()  

# Modify an element in ds_b
ds_b[1] = 10

print('Biến ds_a:', ds_a)
print('Biến ds_b:', ds_b)
# ví dụ 73 
# Declare Boolean variables
x = True
y = False
z = 5 > 8
w = 12 == 12

# Print the data type and value of each variable
print('Kiểu dữ liệu của biến x:', type(x), ', Giá trị:', x)
print('Kiểu dữ liệu của biến y:', type(y), ', Giá trị:', y)
print('Kiểu dữ liệu của biến z:', type(z), ', Giá trị:', z)
print('Kiểu dữ liệu của biến w:', type(w), ', Giá trị:', w)