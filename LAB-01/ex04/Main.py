from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("*******************************")
    print("1. Thêm sinh viên")
    print("2. Cập nhật thông tin sinh viên theo ID")
    print("3. Xóa sinh viên theo ID")
    print("4. Tìm kiếm sinh viên theo tên")
    print("5. Sắp xếp sinh viên theo điểm trung bình")
    print("6. Sắp xếp sinh viên theo tên chuyên ngành")
    print("7. Hiển thị danh sách sinh viên")
    print("0. Thoát")
    print("*******************************")
    key = input("Nhập tùy chọn: ").strip()
    if key == "1":
        qlsv.nhapSinhVien()
        print("Thêm sinh viên thành công!")
    elif key == "2":
        if qlsv.soLuongSinhVien() > 0:
            id_update = int(input("Nhập ID sinh viên cần cập nhật: "))
            qlsv.updateSinhVien(id_update)
        else:
            print("Danh sách sinh viên trống!")
    elif key == "3":
        if qlsv.soLuongSinhVien() > 0:
            id_delete = int(input("Nhập ID sinh viên cần xóa: "))
            if qlsv.deleteById(id_delete):
                print(f"Sinh viên có ID {id_delete} đã bị xóa.")
            else:
                print(f"Sinh viên có ID {id_delete} không tồn tại.")
        else:
            print("Danh sách sinh viên trống!")
    elif key == "4":
        if qlsv.soLuongSinhVien() > 0:
            name_search = input("Nhập tên cần tìm: ")
            result = qlsv.findByName(name_search)
            qlsv.showSinhVien(result)
        else:
            print("Danh sách sinh viên trống!")
    elif key == "5":
        if qlsv.soLuongSinhVien() > 0:
            qlsv.sortByDiemTB()
            print("Danh sách sinh viên theo điểm trung bình:")
            qlsv.showSinhVien()
        else:
            print("Danh sách sinh viên trống!")
    elif key == "6":
        if qlsv.soLuongSinhVien() > 0:
            qlsv.sortByName()
            print("Danh sách sinh viên theo tên chuyên ngành:")
            qlsv.showSinhVien()
        else:
            print("Danh sách sinh viên trống!")
    elif key == "7":
        qlsv.showSinhVien()
    elif key == "0":
        print("Bạn đã chọn thoát chương trình!")
        break
    else:
        print("Không có chức năng này! Vui lòng chọn lại.")