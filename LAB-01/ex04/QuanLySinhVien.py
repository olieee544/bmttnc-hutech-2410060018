from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành của sinh viên: ")
        diemTB = float(input("Nhập điểm trung bình của sinh viên: "))
        sv = SinhVien(name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            name = input("Nhập tên sinh viên mới: ")
            sex = input("Nhập giới tính mới: ")
            major = input("Nhập chuyên ngành mới: ")
            diemTB = float(input("Nhập điểm trung bình mới: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
            print("Cập nhật thành công.")
        else:
            print(f"Sinh viên có ID {ID} không tồn tại.")

    def deleteById(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)
            return True
        return False

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None

    def findByName(self, keyword):
        result = []
        for sv in self.listSinhVien:
            if keyword.lower() in sv._name.lower():
                result.append(sv)
        return result

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._major)

    def xepLoaiHocLuc(self, sv):
        if sv._diemTB >= 8:
            sv._hocLuc = "Giỏi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Khá"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"

    def showSinhVien(self, listSV=None):
        if listSV is None:
            listSV = self.listSinhVien
        print("{:<5} {:<18} {:<8} {:<14} {:<9} {:<10}".format("ID", "Tên", "Giới tính", "Chuyên ngành", "Điểm TB", "Học lực"))
        if listSV:
            for sv in listSV:
                print("{:<5} {:<18} {:<8} {:<14} {:<9} {:<10}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        else:
            print("Danh sách sinh viên trống.")

    def getListSinhVien(self):
        return self.listSinhVien