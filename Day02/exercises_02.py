# Mỗi sản phẩm là 1 tuple (product_id, name, price)
products = [
    (1, "Ban Phim", 250_000),
    (2, "Chuot", 150_000),
    (3, "Man Hinh", 3_000_000),
    (4, "Tai Nghe", 500_000),
]

# Danh sách đơn hàng (list dict)
orders = [
    {"order_id": "HD01", "items": [1, 2, 4]},
    {"order_id": "HD02", "items": [2, 3]},
    {"order_id": "HD03", "items": [1, 4]},
]

#a. Tạo một dict product_map từ products để tra cứu nhanh theo product_id với dạng
def create_product_map(product_list: list[tuple[int, str, int]]) -> dict[int, dict]:
    product_map = {}
    for product_id, name, price in product_list:
        product_map[product_id] = {"name": name, "price": price}
    return product_map

product_map = create_product_map(products)
print(product_map)

# b. Với mỗi hóa đơn trong orders, hãy tính tổng tiền của hóa đơn đó, lưu vào key mới "total" trong từng dict hóa đơn
# Hints:
# items là list các product_id
# tra giá ở product_map (dict)
# cộng dồn


def calculate_order_total(order: dict, product_map: dict[int, dict]) -> None:
    total = 0
    for product_id in order["items"]:
        total += product_map[product_id]["price"]
    order["total"] = total

for order in orders:
    calculate_order_total(order, product_map)
    print(f"  {order['order_id']}: items = {order['items']}, total = {order['total']:,} VND")
#c. In ra danh sách hóa đơn theo format: HD01: 3 san pham, Tong tien = ...
def print_order_summary(order_list: list[dict]) -> None:
    for order in order_list:
        order_id = order["order_id"]
        num_products = len(order["items"])
        total = order["total"]
        print(f"  {order_id}: {num_products} san pham, Tong tien = {total:,} VND")

print_order_summary(orders)
#d. Tạo một set all_products_sold chứa tất cả product_id đã từng được bán trong mọi hóa đơn, sau đó in ra
def get_all_sold_products(order_list: list[dict]) -> set[int]:
    all_products_sold = set()
    for order in order_list:
        for product_id in order["items"]:
            all_products_sold.add(product_id)
    return all_products_sold
all_products_sold = get_all_sold_products(orders)
print("So luong san pham khac nhau da ban:", len(all_products_sold))