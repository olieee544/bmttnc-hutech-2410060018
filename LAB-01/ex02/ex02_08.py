# Nhập chuỗi số nhị phân, phân cách bằng dấu phẩy
data = input("Nhập các số nhị phân (4 chữ số), cách nhau bằng dấu phẩy: ")

# Tách chuỗi thành danh sách
binary_list = data.split(',')

# Danh sách để lưu kết quả
result = []

# Kiểm tra từng số nhị phân
for b in binary_list:
    b = b.strip()  # loại bỏ khoảng trắng
    if int(b, 2) % 5 == 0:   # chuyển nhị phân sang thập phân rồi kiểm tra chia hết 5
        result.append(b)

# In kết quả dưới dạng chuỗi phân cách bằng dấu phẩy
print(",".join(result))