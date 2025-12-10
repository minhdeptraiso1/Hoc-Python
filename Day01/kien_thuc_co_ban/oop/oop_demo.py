class Student:
    def __init__(self, id, name, scores):
        self.id = id
        self.name = name
        self.scores = scores

    def avg(self):
        """Tính điểm trung bình"""
        return sum(self.scores) / len(self.scores)

    def info(self):
        """Hiển thị thông tin sinh viên"""
        print(f"{self.id} - {self.name} - Điểm TB: {self.avg():.2f}")

    def get_grade(self):
        """Xếp loại học lực"""
        avg = self.avg()
        if avg >= 8.5:
            return "Xuất sắc"
        elif avg >= 7.0:
            return "Giỏi"
        elif avg >= 5.5:
            return "Khá"
        elif avg >= 4.0:
            return "Trung bình"
        else:
            return "Yếu"


class StudentManager:
    def __init__(self):
        self.list = []

    def add(self, student):
        """Thêm sinh viên"""
        self.list.append(student)
        print(f"✓ Đã thêm sinh viên: {student.name}")

    def show(self):
        """Hiển thị danh sách sinh viên"""
        if not self.list:
            print("Danh sách trống!")
            return

        print("\n" + "=" * 50)
        print("DANH SÁCH SINH VIÊN")
        print("=" * 50)
        for s in self.list:
            s.info()
        print("=" * 50)

    def find_by_id(self, id):
        """Tìm sinh viên theo ID"""
        for s in self.list:
            if s.id == id:
                return s
        return None

    def find_by_name(self, name):
        """Tìm sinh viên theo tên"""
        results = []
        for s in self.list:
            if name.lower() in s.name.lower():
                results.append(s)
        return results

    def remove(self, id):
        """Xóa sinh viên theo ID"""
        student = self.find_by_id(id)
        if student:
            self.list.remove(student)
            print(f"✓ Đã xóa sinh viên: {student.name}")
            return True
        print(f"✗ Không tìm thấy sinh viên có ID: {id}")
        return False

    def update_scores(self, id, new_scores):
        """Cập nhật điểm sinh viên"""
        student = self.find_by_id(id)
        if student:
            student.scores = new_scores
            print(f"✓ Đã cập nhật điểm cho: {student.name}")
            return True
        print(f"✗ Không tìm thấy sinh viên có ID: {id}")
        return False

    def sort_by_avg(self, reverse=True):
        """Sắp xếp theo điểm trung bình"""
        self.list.sort(key=lambda s: s.avg(), reverse=reverse)
        print("✓ Đã sắp xếp danh sách")

    def get_top_students(self, n=3):
        """Lấy top N sinh viên"""
        sorted_list = sorted(self.list, key=lambda s: s.avg(), reverse=True)
        return sorted_list[:n]

    def show_statistics(self):
        """Hiển thị thống kê"""
        if not self.list:
            print("Danh sách trống!")
            return

        print("\n" + "=" * 50)
        print("THỐNG KÊ")
        print("=" * 50)
        print(f"Tổng số sinh viên: {len(self.list)}")

        avg_scores = [s.avg() for s in self.list]
        print(f"Điểm TB cao nhất: {max(avg_scores):.2f}")
        print(f"Điểm TB thấp nhất: {min(avg_scores):.2f}")
        print(f"Điểm TB chung: {sum(avg_scores) / len(avg_scores):.2f}")

        # Thống kê xếp loại
        grades = {}
        for s in self.list:
            grade = s.get_grade()
            grades[grade] = grades.get(grade, 0) + 1

        print("\nXếp loại học lực:")
        for grade, count in grades.items():
            print(f"  {grade}: {count} sinh viên")
        print("=" * 50)


# ===== SỬ DỤNG =====
if __name__ == "__main__":
    # Tạo quản lý sinh viên
    manager = StudentManager()

    # Thêm sinh viên
    sv1 = Student("SV001", "Nguyễn Văn An", [8.5, 9.0, 7.5, 8.0])
    sv2 = Student("SV002", "Trần Thị Bình", [6.5, 7.0, 6.0, 7.5])
    sv3 = Student("SV003", "Lê Văn Cường", [9.0, 9.5, 8.5, 9.0])
    sv4 = Student("SV004", "Phạm Thị Dung", [5.0, 6.0, 5.5, 4.5])

    manager.add(sv1)
    manager.add(sv2)
    manager.add(sv3)
    manager.add(sv4)

    # Hiển thị danh sách
    manager.show()

    # Tìm kiếm
    print("\n--- TÌM KIẾM ---")
    found = manager.find_by_id("SV002")
    if found:
        print("Tìm thấy:")
        found.info()

    # Tìm theo tên
    results = manager.find_by_name("Văn")
    print(f"\nTìm thấy {len(results)} sinh viên có tên 'Văn':")
    for s in results:
        s.info()

    # Cập nhật điểm
    print("\n--- CẬP NHẬT ---")
    manager.update_scores("SV001", [9.0, 9.5, 8.5, 9.0])

    # Sắp xếp
    print("\n--- SAU KHI SẮP XẾP ---")
    manager.sort_by_avg()
    manager.show()

    # Top sinh viên
    print("\n--- TOP 3 SINH VIÊN ---")
    top = manager.get_top_students(3)
    for i, s in enumerate(top, 1):
        print(f"Top {i}:", end=" ")
        s.info()

    # Thống kê
    manager.show_statistics()

    # Xóa sinh viên
    print("\n--- XÓA SINH VIÊN ---")
    manager.remove("SV004")
    manager.show()