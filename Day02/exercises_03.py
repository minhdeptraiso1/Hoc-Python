# Danh sách user: list tuple (user_id, name)
users = [
    ("U01", "Alice"),
    ("U02", "Bob"),
    ("U03", "Charlie"),
]

# Dict bài viết: key là post_id, value là dict thông tin
posts = {
    "P01": {
        "title": "Hoc Python co ban",
        "author_id": "U01",
        "tags": {"python", "beginner"},
    },
    "P02": {
        "title": "Lam viec voi List va Dict",
        "author_id": "U01",
        "tags": {"python", "data-structure"},
    },
    "P03": {
        "title": "Gioi thieu HTML CSS",
        "author_id": "U02",
        "tags": {"web", "frontend"},
    },
}

#a. Tạo một dict user_map từ users, map user_id sang name

def create_user_map(user_list: list[tuple[str, str]]) -> dict[str, str]:
    user_map = {}
    for user_id, name in user_list:
        user_map[user_id] = name
    return user_map

user_map = create_user_map(users)
print(user_map)

# b. Dùng vòng lặp duyệt posts.items() để in ra:
#     [P01] Hoc Python co ban - Alice - Tags: python, beginner
#     [P02] ...
# Hints:
# lấy author_id từ dict posts
# tra tên ở user_map
# tags là set, cần chuyển sang list/sorted trước rồi nối thành chuỗi

def print_posts(post_dict: dict, user_map: dict[str, str]) -> None:
    for post_id, post_info in post_dict.items():
        title = post_info["title"]
        author_name = user_map[post_info["author_id"]]
        tags_str = ", ".join(sorted(post_info["tags"]))
        print(f"[{post_id}] {title} - {author_name} - Tags: {tags_str}")

print_posts(posts, user_map)

# c. Tạo một set all_tags chứa toàn bộ tag xuất hiện trong mọi bài viết
# Hints: duyệt từng post, lấy post["tags"] (set), dùng update() để dồn vào all_tags
def get_all_tags(post_dict: dict) -> set[str]:
    all_tags = set()
    for post_info in post_dict.values():
        all_tags.update(post_info["tags"])
    return all_tags

all_tags = get_all_tags(posts)
print(all_tags)
# d. Tạo một dict tag_counter để đếm số bài viết chứa mỗi tag
#   Ví dụ:
#   {
#         "python": 2,
#         "beginner": 1,
#         "data-structure": 1,
#         "web": 1,
#         "frontend": 1,
#   }
# Hints:
# Khởi tạo tag_counter = {}
# Duyệt từng post, với mỗi tag trong post["tags"]:
# nếu tag chưa có trong dict => gán = 1
# nếu đã có => tăng lên 1
def count_tags(post_dict: dict) -> dict[str, int]:
    tag_counter = {}
    for post_info in post_dict.values():
        for tag in post_info["tags"]:
            if tag in tag_counter:
                tag_counter[tag] += 1
            else:
                tag_counter[tag] = 1
    return tag_counter

tag_counter = count_tags(posts)
print(tag_counter)