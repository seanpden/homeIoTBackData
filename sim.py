from house import House
from datetime import datetime, timedelta
import random
import psycopg2

class Sim:
    def __init__(self, should_get = False, weeks = 26) -> None:
        self.hs = House()
        self.end = datetime.now()
        self.start = self.end + timedelta(weeks=-weeks)
        self.isMF = False
        self.delta = timedelta(days=1)
        self.weeks = weeks

    def big_sim(self):
        self.hs.toggle_fridge(datetime(self.start.year, self.start.month, self.start.day, self.start.hour, self.start.minute).strftime("%m/%d/%Y, %H:%M:%S"), 150*24*7*self.weeks, cur)
        while self.start <= self.end:
            if self.start.weekday() > 4:
                # --- DOORS ---

                # door, leaving for work/school at 7:30am
                door_old = datetime(self.start.year, self.start.month, self.start.day, 7, 30)
                self.hs.toggle_door_front(door_old.strftime("%m/%d/%Y, %H:%M:%S"), cur)
                door_new = datetime(self.start.year, self.start.month, self.start.day, 7, 30, 30)
                self.hs.toggle_door_front(door_new.strftime("%m/%d/%Y, %H:%M:%S"), cur)
                 # door, coming back from school at 4pm
                self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, 16).strftime("%m/%d/%Y, %H:%M:%S"), cur)
                self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, 16, 0, 30).strftime("%m/%d/%Y, %H:%M:%S"), cur)
                # Door, coming back from work at 5:30pm
                self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, 17, 30).strftime("%m/%d/%Y, %H:%M:%S"), cur)
                self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, 17, 30, 30).strftime("%m/%d/%Y, %H:%M:%S"), cur)
                # Random door times 13
                sample_hour = random.choices(range(0,5), k=13)
                sample_minute = random.sample(range(0, 60), 13)
                for i in range(len(sample_hour)):
                    self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, 17+sample_hour[i], sample_minute[i]).strftime("%m/%d/%Y, %H:%M:%S"), cur)
                    self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, 17+sample_hour[i], sample_minute[i], 30).strftime("%m/%d/%Y, %H:%M:%S"), cur)

                # -------------

                # --- BEDROOM ---

                # Bedroom lights 5-7:30am
                self.hs.toggle_bedroom_overhead_light(datetime(self.start.year, self.start.month, self.start.day, 5).strftime("%m/%d/%Y, %H:%M:%S"), (60*2.5), cur)
                self.hs.toggle_bedroom_overhead_light(datetime(self.start.year, self.start.month, self.start.day, 7, 30).strftime("%m/%d/%Y, %H:%M:%S"), (60*2.5), cur)

                # Bedroom lights 4-10:30pm
                self.hs.toggle_bedroom_overhead_light(datetime(self.start.year, self.start.month, self.start.day, 5).strftime("%m/%d/%Y, %H:%M:%S"), (60*2.5), cur)
                self.hs.toggle_bedroom_overhead_light(datetime(self.start.year, self.start.month, self.start.day, 7, 30).strftime("%m/%d/%Y, %H:%M:%S"), (60*2.5), cur)

                # Bedroom lights 5-7:30am
                self.hs.toggle_bedroom_lamp_one(datetime(self.start.year, self.start.month, self.start.day, 5).strftime("%m/%d/%Y, %H:%M:%S"), (60*2.5), cur)
                self.hs.toggle_bedroom_lamp_one(datetime(self.start.year, self.start.month, self.start.day, 7, 30).strftime("%m/%d/%Y, %H:%M:%S"), (60*2.5), cur)

                # Bedroom lights 4-10:30pm
                self.hs.toggle_bedroom_lamp_one(datetime(self.start.year, self.start.month, self.start.day, 5).strftime("%m/%d/%Y, %H:%M:%S"), (60*2.5), cur)
                self.hs.toggle_bedroom_lamp_one(datetime(self.start.year, self.start.month, self.start.day, 7, 30).strftime("%m/%d/%Y, %H:%M:%S"), (60*2.5), cur)

                # Bedroom lights 5-7:30am
                self.hs.toggle_bedroom_lamp_one(datetime(self.start.year, self.start.month, self.start.day, 5).strftime("%m/%d/%Y, %H:%M:%S"), (60*2.5), cur)
                self.hs.toggle_bedroom_lamp_one(datetime(self.start.year, self.start.month, self.start.day, 7, 30).strftime("%m/%d/%Y, %H:%M:%S"), (60*2.5), cur)

                # Bedroom lights 4-10:30pm
                self.hs.toggle_bedroom_lamp_two(datetime(self.start.year, self.start.month, self.start.day, 5).strftime("%m/%d/%Y, %H:%M:%S"), (60*2.5), cur)
                self.hs.toggle_bedroom_lamp_two(datetime(self.start.year, self.start.month, self.start.day, 7, 30).strftime("%m/%d/%Y, %H:%M:%S"), (60*2.5), cur)

                # Bedroom TV 2hr/day
                temp = random.randint(16,20)
                self.hs.toggle_bedroom_TV(datetime(self.start.year, self.start.month, self.start.day, temp).strftime("%m/%d/%Y, %H:%M:%S"), (60*2), cur)
                self.hs.toggle_bedroom_TV(datetime(self.start.year, self.start.month, self.start.day, temp + 2, 30).strftime("%m/%d/%Y, %H:%M:%S"), (60*2), cur)

                # --------------

                # --- BATH ---

                # 2 shower 2 bath / day
                for i in range(2):
                    temp = random.randint(17,21)
                    _temp = random.choice([0,29])
                    self.hs.toggle_bath_light_one(datetime(self.start.year, self.start.month, self.start.day, temp, _temp).strftime("%m/%d/%Y, %H:%M:%S"), 60*30, cur)
                    self.hs.toggle_bath_light_two(datetime(self.start.year, self.start.month, self.start.day, temp, _temp).strftime("%m/%d/%Y, %H:%M:%S"), 60*30, cur)
                    self.hs.toggle_bath(datetime(self.start.year, self.start.month, self.start.day, temp, _temp).strftime("%m/%d/%Y, %H:%M:%S"), 30, cur)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, temp, _temp).strftime("%m/%d/%Y, %H:%M:%S"), (.65*30), 4500/2, cur)

                    self.hs.toggle_bath(datetime(self.start.year, self.start.month, self.start.day, temp, _temp + 30).strftime("%m/%d/%Y, %H:%M:%S"), 30, cur)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30).strftime("%m/%d/%Y, %H:%M:%S"), (.65*30), 4500/2, cur)
                    self.hs.toggle_bath_light_one(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30).strftime("%m/%d/%Y, %H:%M:%S"), 60*30, cur)
                    self.hs.toggle_bath_light_two(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30).strftime("%m/%d/%Y, %H:%M:%S"), 60*30, cur)

                for i in range(2):
                    temp = random.randint(17,21)
                    _temp = random.choice([0,29])
                    self.hs.toggle_bath_light_one(datetime(self.start.year, self.start.month, self.start.day, temp, _temp).strftime("%m/%d/%Y, %H:%M:%S"), 60*30, cur)
                    self.hs.toggle_bath_light_two(datetime(self.start.year, self.start.month, self.start.day, temp, _temp).strftime("%m/%d/%Y, %H:%M:%S"), 60*30, cur)
                    self.hs.toggle_shower(datetime(self.start.year, self.start.month, self.start.day, temp, _temp).strftime("%m/%d/%Y, %H:%M:%S"), 25, cur)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, temp, _temp).strftime("%m/%d/%Y, %H:%M:%S"), (.65*25), 4500/2, cur)
                    self.hs.toggle_shower(datetime(self.start.year, self.start.month, self.start.day, temp, _temp + 30).strftime("%m/%d/%Y, %H:%M:%S"), 25, cur)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30).strftime("%m/%d/%Y, %H:%M:%S"), (.65*25), 4500/2, cur)
                    self.hs.toggle_bath_light_one(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30).strftime("%m/%d/%Y, %H:%M:%S"), 60*30, cur)
                    self.hs.toggle_bath_light_two(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30).strftime("%m/%d/%Y, %H:%M:%S"), 60*30, cur)

                # ------------

                # --- LR ---

                # 4 hrs mf
                temp = random.randint(16,18)
                self.hs.toggle_lr_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp).strftime("%m/%d/%Y, %H:%M:%S"), 60*4, cur)
                self.hs.toggle_lr_lamp_one(datetime(self.start.year, self.start.month, self.start.day, temp).strftime("%m/%d/%Y, %H:%M:%S"), 60*4, cur)
                self.hs.toggle_lr_lamp_two(datetime(self.start.year, self.start.month, self.start.day, temp).strftime("%m/%d/%Y, %H:%M:%S"), 60*4, cur)
                self.hs.toggle_lr_tv(datetime(self.start.year, self.start.month, self.start.day, temp).strftime("%m/%d/%Y, %H:%M:%S"), 636*4, cur)

                self.hs.toggle_lr_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp+4).strftime("%m/%d/%Y, %H:%M:%S"), 60*4, cur)
                self.hs.toggle_lr_lamp_one(datetime(self.start.year, self.start.month, self.start.day, temp+4).strftime("%m/%d/%Y, %H:%M:%S"), 60*4, cur)
                self.hs.toggle_lr_lamp_two(datetime(self.start.year, self.start.month, self.start.day, temp+4).strftime("%m/%d/%Y, %H:%M:%S"), 60*4, cur)
                self.hs.toggle_lr_tv(datetime(self.start.year, self.start.month, self.start.day, temp+4).strftime("%m/%d/%Y, %H:%M:%S"), 636*4, cur)
                # ----------
                
                # --- KITCHEN ---

                # Dryer

                # Stove
                temp_hour = random.randint(17, 21)
                temp_min = random.randint(0, 44)
                self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min).strftime("%m/%d/%Y, %H:%M:%S"), 60*.25, cur)
                self.hs.toggle_stove(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min).strftime("%m/%d/%Y, %H:%M:%S"), 3500*.25, cur)
                self.hs.toggle_stove(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min+15).strftime("%m/%d/%Y, %H:%M:%S"), 3500*.25, cur)
                self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min).strftime("%m/%d/%Y, %H:%M:%S"), 60*.25, cur)

                # Oven
                temp_hour = random.randint(17, 21)
                temp_min = random.randint(0, 14)
                self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min).strftime("%m/%d/%Y, %H:%M:%S"), 60*.75, cur)
                self.hs.toggle_oven(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min).strftime("%m/%d/%Y, %H:%M:%S"), 4000*.75, cur)
                self.hs.toggle_oven(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min+45).strftime("%m/%d/%Y, %H:%M:%S"), 4000*.75, cur)
                self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min).strftime("%m/%d/%Y, %H:%M:%S"), 60*.75, cur)

                # Microwave 1100w mf 20min/day
                temp = random.choice(range(0, 6))
                _temp = random.randint(17,22)
                __temp = random.randint(0, 56)
                for i in range(0, 6):
                    if i == temp:
                        self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp).strftime("%m/%d/%Y, %H:%M:%S"), (60/60)*2, cur)
                        self.hs.toggle_microwave(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp).strftime("%m/%d/%Y, %H:%M:%S"), (1100/60)*2, cur)
                        self.hs.toggle_microwave(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp+2).strftime("%m/%d/%Y, %H:%M:%S"), (1100/60)*2, cur)
                        self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp).strftime("%m/%d/%Y, %H:%M:%S"), (60/60)*2, cur)
                    else:
                        self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp).strftime("%m/%d/%Y, %H:%M:%S"), (60/60)*3, cur)
                        self.hs.toggle_microwave(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp).strftime("%m/%d/%Y, %H:%M:%S"), (1100/60)*3, cur)
                        self.hs.toggle_microwave(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp+3).strftime("%m/%d/%Y, %H:%M:%S"), (1100/60)*3, cur)
                        self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp).strftime("%m/%d/%Y, %H:%M:%S"), (60/60)*3, cur)

                # ---------------



            else:
                # --- DOORS ---
                sample_hour = random.choices(range(5, 22), k=32)
                sample_minute = random.sample(range(0,60), 32)
                for i in range(len(sample_hour)):
                    self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, sample_hour[i], sample_minute[i]).strftime("%m/%d/%Y, %H:%M:%S"), cur)
                    self.hs.toggle_door_front(datetime(self.start.year, self.start.month, self.start.day, sample_hour[i], sample_minute[i], 30).strftime("%m/%d/%Y, %H:%M:%S"), cur)
                # -------------

                # --- BEDROOM ---

                # Bedroom Lights 5-10:30pm
                self.hs.toggle_bedroom_overhead_light(datetime(self.start.year, self.start.month, self.start.day, 5).strftime("%m/%d/%Y, %H:%M:%S"), (60*17), cur)
                self.hs.toggle_bedroom_overhead_light(datetime(self.start.year, self.start.month, self.start.day, 22, 30).strftime("%m/%d/%Y, %H:%M:%S"), (60*17), cur)

                self.hs.toggle_bedroom_lamp_two(datetime(self.start.year, self.start.month, self.start.day, 5).strftime("%m/%d/%Y, %H:%M:%S"), (60*17), cur)
                self.hs.toggle_bedroom_lamp_two(datetime(self.start.year, self.start.month, self.start.day, 22, 30).strftime("%m/%d/%Y, %H:%M:%S"), (60*17), cur)

                self.hs.toggle_bedroom_lamp_one(datetime(self.start.year, self.start.month, self.start.day, 5).strftime("%m/%d/%Y, %H:%M:%S"), (60*17), cur)
                self.hs.toggle_bedroom_lamp_one(datetime(self.start.year, self.start.month, self.start.day, 22, 30).strftime("%m/%d/%Y, %H:%M:%S"), (60*17), cur)

                # Bedroom TV 4 hrs/day 5am-10:30
                temp = random.randint(5,19)
                self.hs.toggle_bedroom_TV(datetime(self.start.year, self.start.month, self.start.day, temp).strftime("%m/%d/%Y, %H:%M:%S"), (60*2), cur)
                self.hs.toggle_bedroom_TV(datetime(self.start.year, self.start.month, self.start.day, temp + 4, 30).strftime("%m/%d/%Y, %H:%M:%S"), (60*4), cur)
                # --------------

                # --- BATH ---

                # 3 showers 3 baths / day
                for i in range(3):
                    temp = random.randint(5,21)
                    _temp = random.choice([0,29])
                    self.hs.toggle_bath_light_one(datetime(self.start.year, self.start.month, self.start.day, temp, _temp).strftime("%m/%d/%Y, %H:%M:%S"), 60*30, cur)
                    self.hs.toggle_bath_light_two(datetime(self.start.year, self.start.month, self.start.day, temp, _temp).strftime("%m/%d/%Y, %H:%M:%S"), 60*30, cur)
                    self.hs.toggle_bath(datetime(self.start.year, self.start.month, self.start.day, temp, _temp).strftime("%m/%d/%Y, %H:%M:%S"), 30, cur)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, temp, _temp).strftime("%m/%d/%Y, %H:%M:%S"), (.65*30), 4500/2, cur)
                    self.hs.toggle_bath(datetime(self.start.year, self.start.month, self.start.day, temp, _temp + 30).strftime("%m/%d/%Y, %H:%M:%S"), 30, cur)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30).strftime("%m/%d/%Y, %H:%M:%S"), (.65*30), 4500/2, cur)
                    self.hs.toggle_bath_light_one(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30).strftime("%m/%d/%Y, %H:%M:%S"), 60*30, cur)
                    self.hs.toggle_bath_light_two(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30).strftime("%m/%d/%Y, %H:%M:%S"), 60*30, cur)

                for i in range(3):
                    temp = random.randint(5,21)
                    _temp = random.choice([0,29])
                    self.hs.toggle_bath_light_one(datetime(self.start.year, self.start.month, self.start.day, temp, _temp).strftime("%m/%d/%Y, %H:%M:%S"), 60*30, cur)
                    self.hs.toggle_bath_light_two(datetime(self.start.year, self.start.month, self.start.day, temp, _temp).strftime("%m/%d/%Y, %H:%M:%S"), 60*30, cur)
                    self.hs.toggle_shower(datetime(self.start.year, self.start.month, self.start.day, temp, _temp).strftime("%m/%d/%Y, %H:%M:%S"), 25, cur)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, temp, _temp).strftime("%m/%d/%Y, %H:%M:%S"), (.65*25), 4500/2, cur)
                    self.hs.toggle_shower(datetime(self.start.year, self.start.month, self.start.day, temp, _temp + 30).strftime("%m/%d/%Y, %H:%M:%S"), 25, cur)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30).strftime("%m/%d/%Y, %H:%M:%S"), (.65*25), 4500/2, cur)
                    self.hs.toggle_bath_light_one(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30).strftime("%m/%d/%Y, %H:%M:%S"), 60*30, cur)
                    self.hs.toggle_bath_light_two(datetime(self.start.year, self.start.month, self.start.day, temp, _temp+30).strftime("%m/%d/%Y, %H:%M:%S"), 60*30, cur)


                # ------------

                # --- LR ---

                # 8hrs
                temp = random.randint(5,15)
                self.hs.toggle_lr_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp).strftime("%m/%d/%Y, %H:%M:%S"), 60*8, cur)
                self.hs.toggle_lr_lamp_one(datetime(self.start.year, self.start.month, self.start.day, temp).strftime("%m/%d/%Y, %H:%M:%S"), 60*8, cur)
                self.hs.toggle_lr_lamp_two(datetime(self.start.year, self.start.month, self.start.day, temp).strftime("%m/%d/%Y, %H:%M:%S"), 60*8, cur)
                self.hs.toggle_lr_tv(datetime(self.start.year, self.start.month, self.start.day, temp).strftime("%m/%d/%Y, %H:%M:%S"), 636*8, cur)

                self.hs.toggle_lr_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp+8).strftime("%m/%d/%Y, %H:%M:%S"), 60*8, cur)
                self.hs.toggle_lr_lamp_one(datetime(self.start.year, self.start.month, self.start.day, temp+8).strftime("%m/%d/%Y, %H:%M:%S"), 60*8, cur)
                self.hs.toggle_lr_lamp_two(datetime(self.start.year, self.start.month, self.start.day, temp+8).strftime("%m/%d/%Y, %H:%M:%S"), 60*8, cur)
                self.hs.toggle_lr_tv(datetime(self.start.year, self.start.month, self.start.day, temp+8).strftime("%m/%d/%Y, %H:%M:%S"), 636*8, cur)

                # ----------

                # --- KITCHEN ---

                # Dryer

                # Dishwasher

                # Stove
                temp_hour = random.randint(17, 21)
                temp_min = random.randint(0, 29)
                self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min).strftime("%m/%d/%Y, %H:%M:%S"), 60*.5, cur)
                self.hs.toggle_stove(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min).strftime("%m/%d/%Y, %H:%M:%S"), 3500*.5, cur)
                self.hs.toggle_stove(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min+30).strftime("%m/%d/%Y, %H:%M:%S"), 3500*.5, cur)
                self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min).strftime("%m/%d/%Y, %H:%M:%S"), 60*.5, cur)

                # Oven
                temp_hour = random.randint(17, 21)
                temp_min = random.randint(0, 59)
                self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min).strftime("%m/%d/%Y, %H:%M:%S"), 60, cur)
                self.hs.toggle_oven(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min).strftime("%m/%d/%Y, %H:%M:%S"), 4000, cur)
                self.hs.toggle_oven(datetime(self.start.year, self.start.month, self.start.day, temp_hour+1, temp_min).strftime("%m/%d/%Y, %H:%M:%S"), 4000, cur)
                self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, temp_hour, temp_min).strftime("%m/%d/%Y, %H:%M:%S"), 60, cur)

                # Microwave 1100w ss 30min/day
                temp = random.choice(range(0, 8))
                _temp = random.randint(17,22)
                __temp = random.randint(0, 53)
                for i in range(0, 8):
                    if i == temp:
                        self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp).strftime("%m/%d/%Y, %H:%M:%S"), (60/60)*6, cur)
                        self.hs.toggle_microwave(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp).strftime("%m/%d/%Y, %H:%M:%S"), (1100/60)*6, cur)
                        self.hs.toggle_microwave(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp+6).strftime("%m/%d/%Y, %H:%M:%S"), (1100/60)*6, cur)
                        self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp).strftime("%m/%d/%Y, %H:%M:%S"), (60/60)*6, cur)
                    else:
                        self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp).strftime("%m/%d/%Y, %H:%M:%S"), (60/60)*3, cur)
                        self.hs.toggle_microwave(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp).strftime("%m/%d/%Y, %H:%M:%S"), (1100/60)*3, cur)
                        self.hs.toggle_microwave(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp+3).strftime("%m/%d/%Y, %H:%M:%S"), (1100/60)*3, cur)
                        self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, _temp, __temp).strftime("%m/%d/%Y, %H:%M:%S"), (60/60)*3, cur)

                # ---------------

            # NON DAY CONSTRAINED ITEMS

            # Washer 4/week
            rand_days = random.choices(range(0, 6), k=4)
            rand_hours = random.sample(range(16,22), k=4)
            for i in range(len(rand_days)):
                if self.start.weekday() == rand_days[i]:
                    self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]).strftime("%m/%d/%Y, %H:%M:%S"), 60/2, cur)
                    self.hs.toggle_washer(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]).strftime("%m/%d/%Y, %H:%M:%S"), 20, 500/2, cur)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]).strftime("%m/%d/%Y, %H:%M:%S"), .85*20, 4500/2, cur)
                    self.hs.toggle_washer(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i], 30).strftime("%m/%d/%Y, %H:%M:%S"), 20, 500/2, cur)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i], 30).strftime("%m/%d/%Y, %H:%M:%S"), .85*20, 4500/2, cur)
                    self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]).strftime("%m/%d/%Y, %H:%M:%S"), 60/2, cur)

            # Dishwasher 4/week
            rand_days = random.choices(range(0, 6), k=4)
            rand_hours = random.sample(range(16,22), k=4)
            for i in range(len(rand_days)):
                if self.start.weekday() == rand_days[i]:
                    self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]).strftime("%m/%d/%Y, %H:%M:%S"), 60*.75, cur)
                    self.hs.toggle_dishwasher(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]).strftime("%m/%d/%Y, %H:%M:%S"), 20, 1800*.75, cur)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]).strftime("%m/%d/%Y, %H:%M:%S"), .85*20, 4500*.75, cur)
                    self.hs.toggle_dishwasher(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i], 30).strftime("%m/%d/%Y, %H:%M:%S"), 20, 1800*.75, cur)
                    self.hs.toggle_htwater(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i], 30).strftime("%m/%d/%Y, %H:%M:%S"), .85*20, 4500*.75, cur)
                    self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]).strftime("%m/%d/%Y, %H:%M:%S"), 60*.75, cur)

            # Dryer 4/week 3000w 30 min
            rand_days = random.choices(range(0, 6), k=4)
            rand_hours = random.sample(range(16,22), k=4)
            for i in range(len(rand_days)):
                if self.start.weekday() == rand_days[i]:
                    self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]).strftime("%m/%d/%Y, %H:%M:%S"), 60/2, cur)
                    self.hs.toggle_dryer(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]).strftime("%m/%d/%Y, %H:%M:%S"), 1800*.5, cur)
                    self.hs.toggle_dryer(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i], 30).strftime("%m/%d/%Y, %H:%M:%S"), 1800*.5, cur)
                    self.hs.toggle_kitchen_overhead_light(datetime(self.start.year, self.start.month, self.start.day, rand_hours[i]).strftime("%m/%d/%Y, %H:%M:%S"), 60/2, cur)



            self.start += self.delta
            conn.commit()
        self.hs.toggle_fridge(datetime(self.start.year, self.start.month, self.start.day, self.start.hour, self.start.minute).strftime("%m/%d/%Y, %H:%M:%S"), 150*24*7*self.weeks, cur)


if __name__ == "__main__":
    conn = psycopg2.connect(host="138.26.48.83", database="Team5DB", user="Team5", password="team5")
    cur = conn.cursor()
    print("Starting Sim")
    sm = Sim()
    sm.big_sim()
    conn.commit()
    print("Sim Complete")
    cur.close()
    conn.close()