class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self._root = TrieNode()
 
    def insert(self, word: str) -> None:
        """Вставляє слово у дерево."""
        node = self._root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True
 
    def search(self, word: str) -> bool:
        """
        Повертає True, якщо слово повністю присутнє у дереві,
        інакше False.
        """
        node = self._find_node(word)
        return node is not None and node.is_end_of_word
 
    def starts_with(self, prefix: str) -> bool:
        """
        Повертає True, якщо у дереві є хоча б одне слово,
        що починається з prefix, інакше False.
        """
        return self._find_node(prefix) is not None
    
    def _find_node(self, prefix: str):
        node = self._root
        for char in prefix:
            node = node.children.get(char)
            if node is None:
                return None
        return node

 
def build_trie(patterns: list[str]) -> Trie:
    trie = Trie()
    for word in patterns:
        trie.insert(word)
    return trie
 
