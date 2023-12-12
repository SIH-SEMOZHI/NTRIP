import datetime
class GNSSData:
    # Task 1 to add actual data from GNSS
    # def __init__(self,location,time,key):
    #     self.location=location
    #     self.time = time
    #     self.satID = key

    def __init__(self,lat,long,key,time=datetime.datetime.now()):
        self.lat = lat
        self.long = long
        self.time = time
        self.satID = key
    def __str__(self) -> str:
        return  str(self.lat)+","+str(self.long)

    def to_dict(self):
        return {
            "lat":self.lat,
            "long":self.long,
            "time":self.time,
            "key":self.satID
        }
    @classmethod
    def from_dict(cls,data):
        return cls(**data)
