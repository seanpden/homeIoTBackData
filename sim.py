from house import House
from datetime import datetime, timedelta
import random

class Sim:
    def __init__(self, weeks = 26) -> None:
        self.hs = House()
        self.end = datetime.now()
        self.start = self.end + timedelta(weeks=-weeks)
        self.isMF = False
        self.delta = timedelta(days=1)

    def big_sim(self):
        while self.start <= self.end:
            if self.start.weekday() > 4:
                # --- DOORS ---

                # door, leaving for work/school at 7:30am
                self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, 7, 30))
                self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, 7, 30, 30))
                 # door, coming back from school at 4pm
                self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, 16))
                self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, 16, 0, 30))
                # Door, coming back from work at 5:30pm
                self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, 17, 30))
                self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, 17, 30, 30))
                # Random door times 13
                sample_hour = random.choices(range(0,5), k=13)
                sample_minute = random.sample(range(0, 60), 13)
                for i in range(len(sample_hour)):
                    self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, 17+sample_hour[i], sample_minute[i]))
                    self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, 17+sample_hour[i], sample_minute[i], 30))

                # -------------

                # LIGHTS
                self.hs.toggle_bedroom_overhead_light(datetime(self.start.year, self.start.month, self.start.day, 5), (60*2.5))
                self.hs.toggle_bedroom_overhead_light(datetime(self.start.year, self.start.month, self.start.day, 7, 30), (60*2.5))

            else:
                # --- DOORS ---
                sample_hour = random.choices(range(5, 22), k=32)
                sample_minute = random.sample(range(0,60), 32)
                for i in range(len(sample_hour)):
                    self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, sample_hour[i], sample_minute[i]))
                    self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, sample_hour[i], sample_minute[i], 30))

            self.start += self.delta
            
        print(self.hs.get_df())

if __name__ == "__main__":
    sm = Sim()
    sm.big_sim()