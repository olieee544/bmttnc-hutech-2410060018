print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):\n")
lines = []
while True:
    line = input()
    if line.lower()=='done':
        break
    lines.append(line)
print("\nCac dòng đa nhap sau khi chuyển thanh chữ in hoa:")
for line in lines:
    print(line.upper())