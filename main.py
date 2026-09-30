class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minCameraCover(root):
    cameras = 0

    # Стани:
    # 0 — вузол не контролюється
    # 1 — вузол контролюється
    # 2 — на вузлі встановлена камера

    def dfs(node):
        nonlocal cameras

        # Порожній вузол вважаємо контрольованим
        if node is None:
            return 1

        left = dfs(node.left)
        right = dfs(node.right)

        # Якщо хоча б одна дитина не контролюється,
        # встановлюємо камеру на поточний вузол
        if left == 0 or right == 0:
            cameras += 1
            return 2

        # Якщо хоча б одна дитина має камеру,
        # поточний вузол контролюється
        if left == 2 or right == 2:
            return 1

        # Інакше поточний вузол поки не контролюється
        return 0

    # Якщо корінь не контролюється,
    # встановлюємо на ньому камеру
    if dfs(root) == 0:
        cameras += 1

    return cameras


# Приклад 1
root1 = TreeNode(0)
root1.left = TreeNode(0)
root1.left.left = TreeNode(0)
root1.left.right = TreeNode(0)

print("Приклад 1:", minCameraCover(root1))


# Приклад 2
root2 = TreeNode(0)
root2.left = TreeNode(0)
root2.left.left = TreeNode(0)
root2.left.left.left = TreeNode(0)
root2.left.left.left.left = TreeNode(0)

print("Приклад 2:", minCameraCover(root2))


# Додатковий приклад
root3 = TreeNode(0)

print("Приклад 3:", minCameraCover(root3))