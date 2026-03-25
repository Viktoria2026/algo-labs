class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1

class AVLPriorityQueue:
    def __init__(self, log_filename="queue_log.txt"):
        self.root = None
        self.log_filename = log_filename
        with open(self.log_filename, "w", encoding="utf-8") as f:
            f.write("AVL-ЧЕРГИ \n")

    def insert(self, value, priority):
        self.root = self._insert_recursive(self.root, value, priority)
        
        with open(self.log_filename, "a", encoding="utf-8") as f:
            f.write(f"Вставка: {value} (пріоритет {priority})\n")

    def _insert_recursive(self, node, value, priority):
        if not node:
            return Node(value, priority)
        
        if priority >= node.priority:
            node.left = self._insert_recursive(node.left, value, priority)
        else:
            node.right = self._insert_recursive(node.right, value, priority)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1:
            if priority >= node.left.priority:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        if balance < -1:
            if priority < node.right.priority:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        return node

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def pop_highest_priority(self):
        if not self.root: return None
        current = self.root
        while current.left: current = current.left
        res_val, res_pri = current.value, current.priority
        self.root = self._delete_recursive(self.root, res_pri, res_val)
        
        with open(self.log_filename, "a", encoding="utf-8") as f:
            f.write(f"ВИДАЛЕННЯ: {res_val} ({res_pri})\n")
        return res_val, res_pri

    def _delete_recursive(self, node, priority, value):
        if not node: return node
        if priority > node.priority:
            node.left = self._delete_recursive(node.left, priority, value)
        elif priority < node.priority:
            node.right = self._delete_recursive(node.right, priority, value)
        else:
            if node.value != value:
                node.left = self._delete_recursive(node.left, priority, value)
            else:
                if not node.left: return node.right
                elif not node.right: return node.left
                temp = self._get_max_node(node.left)
                node.value, node.priority = temp.value, temp.priority
                node.left = self._delete_recursive(node.left, temp.priority, temp.value)
        if not node: return node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)
        if balance > 1:
            if self._get_balance(node.left) >= 0: return self._rotate_right(node)
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._get_balance(node.right) <= 0: return self._rotate_left(node)
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _get_max_node(self, node):
        while node.right: node = node.right
        return node

    def peek_queue(self):
        res = []
        self._in_order(self.root, res)
        return res

    def _in_order(self, node, res):
        if node:
            self._in_order(node.left, res)
            res.append({'value': node.value, 'priority': node.priority})
            self._in_order(node.right, res)