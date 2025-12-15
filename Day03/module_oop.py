#
# #doc file
# f = open("data.txt.txt","r")
# print(f.read())
# f.close()
# f = open("data.txt.txt","a")
# f.write("Hello Minh \n")
# f.close()
#
# with open("data.txt.txt","r") :
#     print(f.read())
#exception
# try :
#     i = int("acv")
#     print(i)
# except Exception as e :
#     print("Loi khong xac dinh", e)
# try:
#     int = int(input("Enter a number: "))
#     print(f"so ban nhap {int}")
# except ValueError:
#     print("nhap sai kieu so")
# try:
#     swich_key = int(input("Enter swich key: "))
#     while True:
#         if swich_key == 1:
#             with open("data2.txt", "r") as file:
#                 print(file.readline())
#                 break
#         if swich_key == 2:
#             with open("data.txt.txt", "r") as file:
#                 print(file.readline())
#                 break
#         if swich_key == 3:
#             with open("data.txt.txt", "w") as file:
#                 data_new = input("Enter new data.txt: ")
#                 file.write(data_new)
#                 break
#         if swich_key == 4:
#             with open("data.txt.txt", "a") as file:
#                 data_add = input("Enter add data.txt: ")
#                 file.write(data_add)
#                 break
#         else:
#             print("Invalid input")
#             break
#
#
# except FileNotFoundError:
#     print("File not found")
# except Exception as e:
#     print(e)

