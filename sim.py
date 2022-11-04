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
        self.weeks = weeks

    def big_sim(self):
        self.hs.toggle_fridge(datetime(self.start.year, self.start.month, self.start.day, self.start.hour, self.start.minute), 150*24*7*self.weeks)
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

                # --- BEDROOM ---

                # Bedroom lights 5-7:30am
                self.hs.toggle_bedroom_overhead_light(datetime(self.start.year, self.start.month, self.start.day, 5), (60*2.5))
                self.hs.toggle_bedroom_overhead_light(datetime(self.start.year, self.start.month, self.start.day, 7, 30), (60*2.5))

                # Bedroom lights 4-10:30pm
                self.hs.toggle_bedroom_overhead_light(datetime(self.start.year, self.start.month, self.start.day, 5), (60*2.5))
                self.hs.toggle_bedroom_overhead_light(datetime(self.start.year, self.start.month, self.start.day, 7, 30), (60*2.5))

                # Bedroom lights 5-7:30am
                self.hs.toggle_bedroom_lamp_one(datetime(self.start.year, self.start.month, self.start.day, 5), (60*2.5))
                self.hs.toggle_bedroom_lamp_one(datetime(self.start.year, self.start.month, self.start.day, 7, 30), (60*2.5))

                # Bedroom lights 4-10:30pm
                self.hs.toggle_bedroom_lamp_one(datetime(self.start.year, self.start.month, self.start.day, 5), (60*2.5))
                self.hs.toggle_bedroom_lamp_one(datetime(self.start.year, self.start.month, self.start.day, 7, 30), (60*2.5))

                # Bedroom lights 5-7:30am
                self.hs.toggle_bedroom_lamp_one(datetime(self.start.year, self.start.month, self.start.day, 5), (60*2.5))
                self.hs.toggle_bedroom_lamp_one(datetime(self.start.year, self.start.month, self.start.day, 7, 30), (60*2.5))

                # Bedroom lights 4-10:30pm
                self.hs.toggle_bedroom_lamp_two(datetime(self.start.year, self.start.month, self.start.day, 5), (60*2.5))
                self.hs.toggle_bedroom_lamp_two(datetime(self.start.year, self.start.month, self.start.day, 7, 30), (60*2.5))

                # Bedroom TV 2hr/day
                temp = random.randint(16,20)
                self.hs.toggle_bedroom_TV(datetime(self.start.year, self.start.month, self.start.day, temp), (60*2))
                self.hs.toggle_bedroom_TV(datetime(self.start.year, self.start.month, self.start.day, temp + 2, 30), (60*2))

                # --------------

                # --- BATH ---

                # 2 shower 2 bath / day
                for i in range(2):
                    temp = random.randint(17,21)
                    _temp = random.choice([0,29])
                    self.hs.toggle_bath_light_one(datetime(self.start.year, self.start.month, self.start.day, temp, _temp), 60*30)
                    self.hs.toggle_bath_light_two(datetime(self.start.year, self.start.month, self.start.day, temp, _temp), 60*30)
                    self.hs.toggle_bath(datetime(self.start.year, self.start.month, self.start.day, temp, _temp), 30)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, temp, _temp), (.65*30), 4500/2)

                    self.hs.toggle_bath(datetime(self.start.year, self.start.month, self.start.day, temp, _temp + 30), 30)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30), (.65*30), 4500/2)
                    self.hs.toggle_bath_light_one(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30), 60*30)
                    self.hs.toggle_bath_light_two(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30), 60*30)

                for i in range(2):
                    temp = random.randint(17,21)
                    _temp = random.choice([0,29])
                    self.hs.toggle_bath_light_one(datetime(self.start.year, self.start.month, self.start.day, temp, _temp), 60*30)
                    self.hs.toggle_bath_light_two(datetime(self.start.year, self.start.month, self.start.day, temp, _temp), 60*30)
                    self.hs.toggle_shower(datetime(self.start.year, self.start.month, self.start.day, temp, _temp), 25)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, temp, _temp), (.65*25), 4500/2)
                    self.hs.toggle_shower(datetime(self.start.year, self.start.month, self.start.day, temp, _temp + 30), 25)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30), (.65*25), 4500/2)
                    self.hs.toggle_bath_light_one(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30), 60*30)
                    self.hs.toggle_bath_light_two(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30), 60*30)

                # ------------

                # --- LR ---

                # 4 hrs mf
                temp = random.randint(16,18)
                self.hs.toggle_lr_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp), 60*4)
                self.hs.toggle_lr_lamp_one(datetime(self.start.year, self.start.month, self.start.day, temp), 60*4)
                self.hs.toggle_lr_lamp_two(datetime(self.start.year, self.start.month, self.start.day, temp), 60*4)
                self.hs.toggle_lr_tv(datetime(self.start.year, self.start.month, self.start.day, temp), 636*4)

                self.hs.toggle_lr_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp+4), 60*4)
                self.hs.toggle_lr_lamp_one(datetime(self.start.year, self.start.month, self.start.day, temp+4), 60*4)
                self.hs.toggle_lr_lamp_two(datetime(self.start.year, self.start.month, self.start.day, temp+4), 60*4)
                self.hs.toggle_lr_tv(datetime(self.start.year, self.start.month, self.start.day, temp+4), 636*4)
                # ----------
                
                # --- KITCHEN ---

                # Dryer

                # Stove
                temp_hour = random.randint(17, 21)
                temp_min = random.randint(0, 44)
                self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min), 60*.25)
                self.hs.toggle_stove(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min), 3500*.25)
                self.hs.toggle_stove(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min+15), 3500*.25)
                self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min), 60*.25)

                # Oven
                temp_hour = random.randint(17, 21)
                temp_min = random.randint(0, 14)
                self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min), 60*.75)
                self.hs.toggle_oven(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min), 4000*.75)
                self.hs.toggle_oven(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min+45), 4000*.75)
                self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min), 60*.75)

                # Microwave 1100w mf 20min/day
                temp = random.choice(range(0, 6))
                _temp = random.randint(17,22)
                __temp = random.randint(0, 56)
                for i in range(0, 6):
                    if i == temp:
                        self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp), (60/60)*2)
                        self.hs.toggle_microwave(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp), (1100/60)*2)
                        self.hs.toggle_microwave(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp+2), (1100/60)*2)
                        self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp), (60/60)*2)
                    else:
                        self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp), (60/60)*3)
                        self.hs.toggle_microwave(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp), (1100/60)*3)
                        self.hs.toggle_microwave(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp+3), (1100/60)*3)
                        self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp), (60/60)*3)

                # ---------------



            else:
                # --- DOORS ---
                sample_hour = random.choices(range(5, 22), k=32)
                sample_minute = random.sample(range(0,60), 32)
                for i in range(len(sample_hour)):
                    self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, sample_hour[i], sample_minute[i]))
                    self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, sample_hour[i], sample_minute[i], 30))
                # -------------

                # --- BEDROOM ---

                # Bedroom Lights 5-10:30pm
                self.hs.toggle_bedroom_overhead_light(datetime(self.start.year, self.start.month, self.start.day, 5), (60*17))
                self.hs.toggle_bedroom_overhead_light(datetime(self.start.year, self.start.month, self.start.day, 22, 30), (60*17))

                self.hs.toggle_bedroom_lamp_two(datetime(self.start.year, self.start.month, self.start.day, 5), (60*17))
                self.hs.toggle_bedroom_lamp_two(datetime(self.start.year, self.start.month, self.start.day, 22, 30), (60*17))

                self.hs.toggle_bedroom_lamp_one(datetime(self.start.year, self.start.month, self.start.day, 5), (60*17))
                self.hs.toggle_bedroom_lamp_one(datetime(self.start.year, self.start.month, self.start.day, 22, 30), (60*17))

                # Bedroom TV 4 hrs/day 5am-10:30
                temp = random.randint(5,19)
                self.hs.toggle_bedroom_TV(datetime(self.start.year, self.start.month, self.start.day, temp), (60*2))
                self.hs.toggle_bedroom_TV(datetime(self.start.year, self.start.month, self.start.day, temp + 4, 30), (60*4))
                # --------------

                # --- BATH ---

                # 3 showers 3 baths / day
                for i in range(3):
                    temp = random.randint(5,21)
                    _temp = random.choice([0,29])
                    self.hs.toggle_bath_light_one(datetime(self.start.year, self.start.month, self.start.day, temp, _temp), 60*30)
                    self.hs.toggle_bath_light_two(datetime(self.start.year, self.start.month, self.start.day, temp, _temp), 60*30)
                    self.hs.toggle_bath(datetime(self.start.year, self.start.month, self.start.day, temp, _temp), 30)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, temp, _temp), (.65*30), 4500/2)
                    self.hs.toggle_bath(datetime(self.start.year, self.start.month, self.start.day, temp, _temp + 30), 30)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30), (.65*30), 4500/2)
                    self.hs.toggle_bath_light_one(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30), 60*30)
                    self.hs.toggle_bath_light_two(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30), 60*30)

                for i in range(3):
                    temp = random.randint(5,21)
                    _temp = random.choice([0,29])
                    self.hs.toggle_bath_light_one(datetime(self.start.year, self.start.month, self.start.day, temp, _temp), 60*30)
                    self.hs.toggle_bath_light_two(datetime(self.start.year, self.start.month, self.start.day, temp, _temp), 60*30)
                    self.hs.toggle_shower(datetime(self.start.year, self.start.month, self.start.day, temp, _temp), 25)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, temp, _temp), (.65*25), 4500/2)
                    self.hs.toggle_shower(datetime(self.start.year, self.start.month, self.start.day, temp, _temp + 30), 25)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30), (.65*25), 4500/2)
                    self.hs.toggle_bath_light_one(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30), 60*30)
                    self.hs.toggle_bath_light_two(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30), 60*30)


                # ------------

                # --- LR ---

                # 8hrs
                temp = random.randint(5,15)
                self.hs.toggle_lr_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp), 60*8)
                self.hs.toggle_lr_lamp_one(datetime(self.start.year, self.start.month, self.start.day, temp), 60*8)
                self.hs.toggle_lr_lamp_two(datetime(self.start.year, self.start.month, self.start.day, temp), 60*8)
                self.hs.toggle_lr_tv(datetime(self.start.year, self.start.month, self.start.day, temp), 636*8)

                self.hs.toggle_lr_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp+8), 60*8)
                self.hs.toggle_lr_lamp_one(datetime(self.start.year, self.start.month, self.start.day, temp+8), 60*8)
                self.hs.toggle_lr_lamp_two(datetime(self.start.year, self.start.month, self.start.day, temp+8), 60*8)
                self.hs.toggle_lr_tv(datetime(self.start.year, self.start.month, self.start.day, temp+8), 636*8)

                # ----------

                # --- KITCHEN ---

                # Dryer

                # Dishwasher

                # Stove
                temp_hour = random.randint(17, 21)
                temp_min = random.randint(0, 29)
                self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min), 60*.5)
                self.hs.toggle_stove(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min), 3500*.5)
                self.hs.toggle_stove(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min+30), 3500*.5)
                self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min), 60*.5)

                # Oven
                temp_hour = random.randint(17, 21)
                temp_min = random.randint(0, 59)
                self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min), 60)
                self.hs.toggle_oven(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min), 4000)
                self.hs.toggle_oven(datetime(self.start.year, self.start.month, self.start.day, temp_hour+1, temp_min), 4000)
                self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min), 60)

                # Microwave 1100w ss 30min/day
                temp = random.choice(range(0, 8))
                _temp = random.randint(17,22)
                __temp = random.randint(0, 53)
                for i in range(0, 8):
                    if i == temp:
                        self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp), (60/60)*6)
                        self.hs.toggle_microwave(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp), (1100/60)*6)
                        self.hs.toggle_microwave(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp+6), (1100/60)*6)
                        self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp), (60/60)*6)
                    else:
                        self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp), (60/60)*3)
                        self.hs.toggle_microwave(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp), (1100/60)*3)
                        self.hs.toggle_microwave(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp+3), (1100/60)*3)
                        self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp), (60/60)*3)

                # ---------------

            # NON DAY CONSTRAINED ITEMS

            # Washer 4/week
            rand_days = random.choices(range(0, 6), k=4)
            rand_hours = random.sample(range(16,22), k=4)
            for i in range(len(rand_days)):
                if self.start.weekday() == rand_days[i]:
                    self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]), 60/2)
                    self.hs.toggle_washer(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]), 20, 500/2)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]), .85*20, 4500/2)
                    self.hs.toggle_washer(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i], 30), 20, 500/2)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i], 30), .85*20, 4500/2)
                    self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]), 60/2)

            # Dishwasher 4/week
            rand_days = random.choices(range(0, 6), k=4)
            rand_hours = random.sample(range(16,22), k=4)
            for i in range(len(rand_days)):
                if self.start.weekday() == rand_days[i]:
                    self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]), 60*.75)
                    self.hs.toggle_dishwasher(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]), 20, 1800*.75)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]), .85*20, 4500*.75)
                    self.hs.toggle_dishwasher(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i], 30), 20, 1800*.75)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i], 30), .85*20, 4500*.75)
                    self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]), 60*.75)

            # Dryer 4/week 3000w 30 min
            rand_days = random.choices(range(0, 6), k=4)
            rand_hours = random.sample(range(16,22), k=4)
            for i in range(len(rand_days)):
                if self.start.weekday() == rand_days[i]:
                    self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]), 60/2)
                    self.hs.toggle_dryer(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]), 1800*.5)
                    self.hs.toggle_dryer(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i], 30), 1800*.5)
                    self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]), 60/2)



            self.start += self.delta
        
        self.hs.toggle_fridge(datetime(self.start.year, self.start.month, self.start.day, self.start.hour, self.start.minute), 150*24*7*self.weeks)

        self.hs.get_df().to_html()

if __name__ == "__main__":
    sm = Sim()
    sm.big_sim()