"""

Implementing this Undergrodund System, has a checkIn funciton, checkoutFinction , getAfverage time function

check in - checking it a tthe function, and the one caveat that we have here is that custmer can only be checked into one place at a tiem (stationName)
check out- checking out (userId, stationName)

getAverageTime - functon that resutrns teh average time it takes to tracle from start to end station 
    - we only look at the direct pahts from start to end station 

- getAverageTime 
customer check in hashmap, with the key being the id and the key being the stationName and startingTime
whenever we checkout, we'll check to see if that customer checked in or not, if not, we will print an error
    - if they did, then we should be able to compute the time it took and add 1 to the number of records 
    - we should make a hashmap from (startStation, endStation) as the key, and the value being the time, and num of records 

"""
class UndergroundSystem:

    def __init__(self):
        self.customer_check_in = {}
        self.start_to_end = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer_check_in[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.customer_check_in:
            start_station, start_time = self.customer_check_in[id]
            travel_time = t - start_time
            if (start_station, stationName) in self.start_to_end:
                self.start_to_end[(start_station, stationName)][0] += travel_time
                self.start_to_end[(start_station, stationName)][1] += 1
            else:
                self.start_to_end[(start_station, stationName)] = [travel_time, 1]
        self.customer_check_in.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) in self.start_to_end:
            total_time, num_of_records = self.start_to_end[(startStation, endStation)]
            return total_time / num_of_records


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)