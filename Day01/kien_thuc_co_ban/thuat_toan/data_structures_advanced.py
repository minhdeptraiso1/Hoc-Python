"""
===============================================================================
                DATA STRUCTURES NÂNG CAO TRONG PYTHON
Gồm:
✔ Heap (MinHeap, MaxHeap)
✔ Tree (Binary Tree, Binary Search Tree)
✔ Graph (Adjacency List, DFS, BFS)
✔ Priority Queue (heapq)
✔ Dijkstra (Shortest Path)
===============================================================================
"""

import heapq
from collections import deque


# ============================================================================
# 1) HEAP – MIN HEAP & MAX HEAP
# ============================================================================

print("\n===== HEAP (MIN HEAP / MAX HEAP) =====")

# Python có sẵn MinHeap qua heapq
min_heap = []
nums = [5, 1, 8, 3]

for n in nums:
    heapq.heappush(min_heap, n)

print("MinHeap:", min_heap)
print("Pop nhỏ nhất:", heapq.heappop(min_heap))

# MaxHeap → chuyển số thành âm rồi lưu vào minheap
max_heap = []
for n in nums:
    heapq.heappush(max_heap, -n)

print("MaxHeap:", max_heap)
print("Pop lớn nhất:", -heapq.heappop(max_heap))


# ============================================================================
# 2) TREE – BINARY TREE (CÂY NHỊ PHÂN)
# ============================================================================

print("\n===== BINARY TREE =====")

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Tạo cây:
#        10
#       /  \
#      5    15

root = Node(10)
root.left = Node(5)
root.right = Node(15)

def preorder(node):
    if not node:
        return
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)

print("Preorder tree:", end=" ")
preorder(root)
print()


# ============================================================================
# 3) BINARY SEARCH TREE – BST
# ============================================================================

print("\n===== BINARY SEARCH TREE (BST) =====")

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)


bst = BST()
for v in [10, 5, 15, 3, 7]:
    bst.insert(v)

print("BST search 7:", bst.search(7))
print("BST search 20:", bst.search(20))


# ============================================================================
# 4) GRAPH – BIỂU DIỄN BẰNG ADJACENCY LIST
# ============================================================================

print("\n===== GRAPH – ADJACENCY LIST =====")

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

print("Graph:", graph)


# ============================================================================
# 5) DFS – Depth First Search
# ============================================================================

print("\n===== DFS (Depth First Search) =====")

visited = set()

def dfs(node):
    if node in visited:
        return
    visited.add(node)
    print(node, end=" ")
    for nxt in graph[node]:
        dfs(nxt)

dfs("A")
print()


# ============================================================================
# 6) BFS – Breadth First Search
# ============================================================================

print("\n===== BFS (Breadth First Search) =====")

def bfs(start):
    q = deque([start])
    visited = set([start])
    while q:
        node = q.popleft()
        print(node, end=" ")
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)

bfs("A")
print()


# ============================================================================
# 7) DIJKSTRA – TÌM ĐƯỜNG ĐI NGẮN NHẤT
# ============================================================================

print("\n===== DIJKSTRA (Shortest Path) =====")

weighted_graph = {
    "A": [("B", 2), ("C", 5)],
    "B": [("C", 1), ("D", 3)],
    "C": [("D", 2)],
    "D": []
}

def dijkstra(start):
    dist = {node: float("inf") for node in weighted_graph}
    dist[start] = 0

    pq = [(0, start)]  # (khoảng cách, node)

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue

        for (nxt, weight) in weighted_graph[node]:
            new_dist = d + weight
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(pq, (new_dist, nxt))

    return dist

print("Khoảng cách ngắn nhất từ A:", dijkstra("A"))


# ============================================================================
# TÓM TẮT
# ============================================================================

print("""
====================== TÓM TẮT DATA STRUCTURES NÂNG CAO ======================

✔ HEAP (MinHeap / MaxHeap)
    - heapq → mặc định MinHeap
    - MaxHeap → push giá trị âm

✔ TREE
    - Binary Tree: trái / phải
    - Preorder, Inorder, Postorder

✔ BST – Binary Search Tree
    - Mọi giá trị bên trái < node < giá trị bên phải
    - Tìm kiếm O(log n)

✔ GRAPH (Adjacency List)
    - Lưu dạng dictionary

✔ DFS
    - Đi sâu trước
    - Dùng stack hoặc đệ quy

✔ BFS
    - Đi rộng trước
    - Dùng queue

✔ DIJKSTRA
    - Tìm đường đi ngắn nhất với trọng số dương
    - Dùng Priority Queue (heapq)

===============================================================================
""")
