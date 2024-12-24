class UndergroundSystem:
    # when we checkout we can compute teh average time and then remove it from the station
    # we can have a hashmap tha ttake sthe sationName and id as teh key in a typle 
    # and then the time fro the checkIn
    # we can then have another hashmpa that atakes the startStation, endStation as a tuple and then the running sum and number of checkin/checkou
    def __init__(self):
        self.idChecker = {}
        self.tracker = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.idChecker[id] = ((stationName, t))
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.idChecker:
            startStation, startTime = self.idChecker[id]
            endStation = stationName
            if (startStation, endStation) in self.tracker:
                self.tracker[(startStation, endStation)][0] += t - startTime
                self.tracker[(startStation, endStation)][1] += 1
            else:
                self.tracker[(startStation, endStation)] = [t-startTime, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        res = 0
        if (startStation, endStation) in self.tracker:
            totalTime, totalTrips = self.tracker[(startStation, endStation)]
        res = totalTime/totalTrips
        return res


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)