class FileSystem:

    def __init__(self):
        self.hashmap = {}

    def createPath(self, path: str, value: int) -> bool:
        currPath = path.split('/')
        if len(currPath) > 2:
            parent = '/'.join(currPath[:-1])
            print(parent)
            if parent not in self.hashmap:
                return False

        if path in self.hashmap or path == '/':
            return False
        
        self.hashmap[path] = value
        return True

    def get(self, path: str) -> int:
        return self.hashmap[path] if path in self.hashmap else -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)