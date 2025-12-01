class SinhVien:
    _id_auto = 1

    def __init__(self, name, sex, major, diemTB):
        self._id = SinhVien._id_auto
        SinhVien._id_auto += 1
        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self._hocLuc = ""