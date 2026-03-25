import collections

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def get_diameter(self) -> int:
        self._max_diameter = 0
        self._calculate_height(self)
        return self._max_diameter

    def print_traversals(self):
        print("Pre-order: ", end="")
        self._pre_order(self)
        print("\nPost-order:", end="")
        self._post_order(self)
        print()

    def _calculate_height(self, node):
        if not node:
            return 0
        
        left_h = self._calculate_height(node.left)
        right_h = self._calculate_height(node.right)
        self._max_diameter = max(self._max_diameter, left_h + right_h)
        
        return max(left_h, right_h) + 1

    def _pre_order(self, node):
        if node:
            print(node.value, end=" ")
            self._pre_order(node.left)
            self._pre_order(node.right)

    def _post_order(self, node):
        if node:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node.value, end=" ")
            
def build_tree(nodes):
    if not nodes or nodes[0] is None: return None
    root = BinaryTree(nodes[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()
        if i < len(nodes) and nodes[i] is not None:
            node.left = BinaryTree(nodes[i]); queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = BinaryTree(nodes[i]); queue.append(node.right)
        i += 1
    return root


