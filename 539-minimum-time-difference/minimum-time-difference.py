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
            return sorted(minutesList, reverse = True)

        currentList = parseData(timePoints, minutesList)
        rightBound = 24 * 60
        index = 0
        print(currentList)
        while index < len(currentList) - 1:

            time = currentList[index]
            valueBefore = int(currentList[index - 1])
            valueAfter = int(currentList[index + 1])

            leftTimeA = abs(time - valueBefore)
            leftTimeB = abs(time - valueAfter)

            rightTimeA = abs(rightBound - time + valueBefore)
            rightTimeB = abs(rightBound - time + valueAfter)
            print(time)
            print(rightTimeA)
            leftTimeMin = min(leftTimeA, rightTimeA)
            rightTimeMin = min(leftTimeB, rightTimeB)

            minCurrValue = min(leftTimeMin, rightTimeMin)
            minRes = min(minRes, minCurrValue)

            index += 1

        return minRes
