"""
===============================================================================
                   TỔNG HỢP THUẬT TOÁN NÂNG CAO TRONG PYTHON
Gồm:
✔ Recursion nâng cao
✔ Backtracking
✔ BFS – DFS (Graph)
✔ Dijkstra (Shortest Path)
✔ Dynamic Programming (DP)
✔ Memoization
✔ Greedy Algorithm
✔ Heap Sort
✔ Binary Search nâng cao (lower/upper bound)
===============================================================================
"""

# =============================================================================
# 1) ĐỆ QUY (RECURSION) – NÂNG CAO
# =============================================================================

print("\n===== RECURSION NÂNG CAO =====")

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Giai thừa 5 =", factorial(5))


# =============================================================================
# 2) BACKTRACKING – QUAY LUI (VD: Tổ hợp)
# =============================================================================

print("\n===== BACKTRACKING – TỔ HỢP =====")

result = []
path = []

def combination(nums, start):
    result.append(path.copy())
    for i in range(start, len(nums)):
        path.append(nums[i])
        combination(nums, i + 1)
        path.pop()  # quay lui

combination([1, 2, 3], 0)
print("Các tổ hợp:", result)


# =============================================================================
# 3) DFS – Depth First Search
# =============================================================================

print("\n===== DFS – GRAPH =====")

graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: []
}

def dfs(node, visited=set()):
    if node in visited:
        return
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        dfs(neighbor, visited)

dfs(1)
print()


# =============================================================================
# 4) BFS – Breadth First Search
# =============================================================================

print("\n===== BFS – GRAPH =====")

from collections import deque

def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(neighbor)

bfs(1)
print()


# =============================================================================
# 5) DIJKSTRA – SHORTEST PATH
# =============================================================================

print("\n===== DIJKSTRA – SHORTEST PATH =====")

import heapq

def dijkstra(graph, start):
    dist = {node: float("inf") for node in graph}
    dist[start] = 0

    pq = [(0, start)]  # (distance, node)

    while pq:
        current_dist, node = heapq.heappop(pq)

        if current_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            newDist = current_dist + weight
            if newDist < dist[neighbor]:
                dist[neighbor] = newDist
                heapq.heappush(pq, (newDist, neighbor))

    return dist

weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 6)],
    'C': [('D', 3)],
    'D': []
}

print("Khoảng cách ngắn nhất:", dijkstra(weighted_graph, 'A'))


# =============================================================================
# 6) DYNAMIC PROGRAMMING (DP)
#    Ví dụ: Fibonacci tối ưu
# =============================================================================

print("\n===== DYNAMIC PROGRAMMING – FIBONACCI =====")

def fib_dp(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]

print("Fib(10) =", fib_dp(10))


# =============================================================================
# 7) MEMOIZATION – LƯU KẾT QUẢ ĐỆ QUY
# =============================================================================

print("\n===== MEMOIZATION – TỐI ƯU ĐỆ QUY =====")

memo = {}

def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

print("Fib(10) =", fib_memo(10))


# =============================================================================
# 8) GREEDY ALGORITHM – THUẬT TOÁN THAM LAM
# VD: Chọn số lượng tiền xu ít nhất
# =============================================================================

print("\n===== GREEDY ALGORITHM =====")

coins = [10, 5, 2, 1]

def min_coins(amount):
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count

print("Số xu ít nhất cho 27:", min_coins(27))


# =============================================================================
# 9) HEAP SORT – SẮP XẾP BẰNG HEAP
# =============================================================================

print("\n===== HEAP SORT =====")

def heap_sort(arr):
    h = []
    for v in arr:
        heapq.heappush(h, v)
    return [heapq.heappop(h) for _ in range(len(h))]

print("Heap Sort:", heap_sort([5, 1, 8, 3, 2]))


# =============================================================================
# 10) BINARY SEARCH NÂNG CAO – LOWER BOUND & UPPER BOUND
# =============================================================================

print("\n===== LOWER BOUND / UPPER BOUND =====")

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

arr = [1, 2, 2, 2, 3, 4, 5]

print("Lower bound của 2:", lower_bound(arr, 2))
print("Upper bound của 2:", upper_bound(arr, 2))


# =============================================================================
# TÓM TẮT
# =============================================================================

print("""
===================== TÓM TẮT THUẬT TOÁN NÂNG CAO =====================

✔ Recursion → đệ quy nâng cao
✔ Backtracking → giải tổ hợp, phân hoạch, sudoku…
✔ DFS/BFS → duyệt đồ thị
✔ Dijkstra → đường đi ngắn nhất
✔ DP → tối ưu đệ quy, bài toán tối ưu
✔ Memoization → cache kết quả để tăng tốc
✔ Greedy → chọn phương án tốt nhất tại mỗi bước
✔ Heap Sort → sắp xếp hiệu quả
✔ Binary Search nâng cao → lower/upper bound

=======================================================================
""")
