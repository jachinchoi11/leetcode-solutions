class FileSystem:
    # essentially, the idea of this problem is to check if soemthing is already there, so we'll have a hashmap
    # of waht we have and assign itt o a value 
    def __init__(self):
        self.path_to_value = {}
    def createPath(self, path: str, value: int) -> bool:
        if path in self.path_to_value:
            return False
        
        curr_path = path.split('/')
        if len(curr_path) > 2:
            parent = '/'.join(curr_path[:-1])
            if parent not in self.path_to_value:
                return False
        self.path_to_value[path] = value
        return True

    def get(self, path: str) -> int:

        if path in self.path_to_value:
            return self.path_to_value[path]
        return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)