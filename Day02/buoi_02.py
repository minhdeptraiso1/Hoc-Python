def dtb_l(scores: list[float]) -> None:
    """
    ham tinh diem trung binh
    :param scores: list [float]
    :return: diem trung binh /cao nhat /thap nhat
    """
    max_score = 0
    min_score = 10
    dtb = 0.0
    for score in scores:
        dtb += score
        if score > max_score:
            max_score = score
        if score < min_score:
            min_score = score
    print("diem trung binh :", dtb/len(scores))
    print("diem trung binh cao nhat :", max_score)
    print("diem trung binh thap nhat :", min_score)
score_list = [7.5 , 8.0, 6.5, 9.0, 8.5]
dtb_l(score_list)



def remove_negative_number(list: list[int]) -> None:
    for num in list.copy():
        if num < 0:
            list.remove(num)
    return list

negative_number = [-1, 0, 1]
print(remove_negative_number(negative_number))

def list_concatenation (list1: list[int], list2: list[int], list3: list[int]) -> None:
    list1.extend(list2)
    list1.extend(list3)
    return list1

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
print(list_concatenation(list1, list2, list3))

from typing import Any

student: dict[str, Any] = {
    "name": "Nguyen Van A",
    "age": 20,
    "scores": [7.5, 8.0, 6.5, 9.0],
}

def print_student(student: dict[str, Any]) -> None:
    for k in student:
        print(f"{k}: {student[k]}")
def avg(student: dict[str, Any]) -> float:
    return sum(student["scores"]) / len(student["scores"])

student.update(avg = avg(student))
print_student(student)

s = "hello world"
couter = {}

for s in s:
    couter.setdefault(s, 0)
    couter[s] += 1
print(couter)

students: dict[str, dict[str, Any]] = {
    "SV01": {"name": "Nguyen Van A", "age": 20},
    "SV02": {"name": "Tran Thi B", "age": 21},
}

students.update(SV03 = {"name": "Nguyen Van C", "age": 20})
students["SV01"]["age"] += 1

for student_id, infor in students.items():
    print(student_id, infor)