class Node:
    def __init__(self, c):
        self.c = c
        self.next = []

class Trie:

    def __init__(self):
        self.start = Node(None)

    '''
    Ideally the traversal code should be reused between helper and insert
    '''
    def insert(self, word: str) -> None:
        node = self.start
        idx = 0
        while True:
            if idx == len(word):
                if sum([i==None for i in node.next])==0:
                    node.next += [None]
                return
            found_next = False
            for child in node.next:
                if child == None:
                    continue
                if child.c == word[idx]:
                    idx += 1
                    node = child
                    found_next = True
                    break
            if not found_next:
                break
        for i in range(idx, len(word)):
            node.next = node.next + [Node(word[i])]
            node = node.next[-1]
        if sum([i==None for i in node.next])==0:
            node.next += [None] # indicates its a word
            
    def helper(self, word) -> (bool, bool):
        '''
        first return bool indicates if the word exists as a prefix
        the second one says if its a full word
        '''
        node = self.start
        idx = 0
        while True:
            if idx == len(word):
                return (True, sum([i==None for i in node.next]) == 1)
            found_next = False
            for child in node.next:
                if child == None:
                    continue
                if child.c == word[idx]:
                    idx += 1
                    node = child
                    found_next = True
                    break
            if not found_next:
                return (False, False)

    def search(self, word: str) -> bool:
        return self.helper(word)[1]
        

    def startsWith(self, prefix: str) -> bool:
        return self.helper(prefix)[0]

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
