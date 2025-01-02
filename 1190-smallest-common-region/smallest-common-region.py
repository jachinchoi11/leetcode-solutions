class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        # in this case, we can build a graph using an adjacency list
        # find kind of all the paths 
        # and then we can iterate through the grpah and find region1 and region2 
        # we then can find the path of one and put it in a set
        # as we iterate down and find region 2's path, we just return the latest time of when they are teogehr 
        # keep track of it as a variable 

        childParent = collections.defaultdict(list)

        for region in regions:
            for i in range(1, len(region)):
                childParent[region[i]] = region[0]
        
        # the adjacency list now set up and now we have to find the path, remember in this case we set up the lsit bottom up
        # as it makes it easier for us to find the path now that it is reversed 

        def findPath(currNode):
            path = []

            path.append(currNode)

            while currNode in childParent:
                currNode = childParent[currNode]
                path.append(currNode)
            
            path.reverse()
            return path
        pathA = findPath(region1)
        pathB = findPath(region2)
        res = regions[0][0]
        
        for currA, currB in zip(pathA, pathB):
            if currA != currB:
                return res
            else:
                res = currA
        return res







