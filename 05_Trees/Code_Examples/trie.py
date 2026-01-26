# Trie (Prefix Tree) Implementation

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.is_end

    def starts_with(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True


# Example
trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("dog")

print("Search 'cat':", trie.search("cat"))
print("Search 'cap':", trie.search("cap"))
print("Prefix 'ca':", trie.starts_with("ca"))
print("Prefix 'do':", trie.starts_with("do"))

# Output
# Search 'cat': True
# Search 'cap': False
# Prefix 'ca': True
# Prefix 'do': True
