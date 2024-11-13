class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # essentially we have to have a helper function that computes the distance of the entire list 
        # parse x and y and send it into a function get out distance and make a new res 
        # go through that and heapify O(n) complexity
        # heapq.heappop(the new array) k amount of times 
        
        parsedDistance = []
        ans = []
        for point in points:
            # parses the integers and calculates the distance 
            x = point[0]
            y = point[1]
            currDistance = self.distanceCalc(x,y)
            parsedDistance.append((currDistance, x, y))
        
        heapq.heapify(parsedDistance)

        for times in range(k):
            currValue = heapq.heappop(parsedDistance)
            xVal = currValue[1]
            yVal = currValue[2]
            ans.append([xVal,yVal])
        return ans 
        
    def distanceCalc(self, x, y):
        distance = ((x ** 2) + (y**2)) ** 0.5
        return distance

    # O(nlogn) time 
    # O(n) space
