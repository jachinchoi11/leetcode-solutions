class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minRes = 24 * 60
        minutesList = []
        # essentially you have to check the negative -1 timePoint and the timePoint after - once you sort 
        # have a var that will keep track of the min distance 
        def parseData(timePoints, minutesList):
            for time in timePoints:
                hours = int(time[0:2])
                minutes = int(time[3:5])
                minutesList.append((hours * 60) + minutes)
            return sorted(minutesList)

        currentList = parseData(timePoints, minutesList)
        rightBound = 24 * 60
        index = 0
        print(currentList)
        while index < len(currentList):

            time = currentList[index]
            valueBefore = int(currentList[index - 1])
            leftTimeA = abs(time - valueBefore)
            minRes = min(minRes, leftTimeA)
            index += 1
        
        rightTimeA = abs(rightBound - currentList[-1] + currentList[0])
        return min(minRes, rightTimeA)
