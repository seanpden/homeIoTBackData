from datetime import datetime, timedelta
import time
import random
import psycopg2
from house import House
import meteostat as ms
from meteostat import units

conn = psycopg2.connect(host="138.26.48.83", database="Team5DB", user="Team5", password="team5")
cur = conn.cursor()

class RealtimeSim:
    def __init__(self, door_front = False, door_back = False, door_garage_out = False, door_garage_one = False, door_garage_two = False, bedroom_overhead_light = False, 
                 bedroom_lamp_one = False, bedroom_lamp_two = False, bath_light_one = False, bath_light_two = False, lr_overhead_light = False, lr_lamp_one = False,
                 lr_lamp_two = False, kitchen_overhead_light = False, bedroom_tv = False, lr_tv = False, fridge = False, hvac = False) -> None:
        self.hs = House()
        self.current_time = datetime.now()
        self.inside_temp = 70
        self.target_temp = 70
        self.cooldown = 0
        self.outside_temp = ms.Hourly('72228', datetime.now(), datetime.now()).convert(units.imperial).fetch()['temp'].iloc[0]
        self.df_last = datetime.now()
        self.db_last = datetime.now()
        self.dgo_last = datetime.now()
        self.dg1_last = datetime.now()
        self.dg2_last = datetime.now()
        self.beol_last = datetime.now()
        self.bel1_last = datetime.now()
        self.bel2_last = datetime.now()
        self.bal1_last = datetime.now()
        self.bal2_last = datetime.now()
        self.lrol_last = datetime.now()
        self.lrl1_last = datetime.now()
        self.lrl2_last = datetime.now()
        self.kol_last = datetime.now()
        self.btv_last = datetime.now()
        self.lrtv_last = datetime.now()
        self.hvac_last = datetime.now()
        self.hs.set_door_front(door_front)
        self.hs.set_door_back(door_back)
        self.hs.set_door_garage_out(door_garage_out)
        self.hs.set_door_garage_one(door_garage_one)
        self.hs.set_door_garage_two(door_garage_two)
        self.hs.set_bedroom_overhead_light(bedroom_overhead_light)
        self.hs.set_bedroom_lamp_one(bedroom_lamp_one)
        self.hs.set_bedroom_lamp_two(bedroom_lamp_two)
        self.hs.set_bath_light_one(bath_light_one)
        self.hs.set_bath_light_two(bath_light_two)
        self.hs.set_lr_overhead_light(lr_overhead_light)
        self.hs.set_lr_lamp_one(lr_lamp_one)
        self.hs.set_lr_lamp_two(lr_lamp_two)
        self.hs.set_kitchen_overhead_light(kitchen_overhead_light)
        self.hs.set_bedroom_tv(bedroom_tv)
        self.hs.set_lr_tv(lr_tv)
        self.hs.set_fridge(fridge)
        self.hs.set_hvac(hvac)

    def start_sim(self):
        while True:
            if self.current_time.weekday < 5:
                while ((self.current_time.hour >= 5) and (self.current_time.hour <= 7 and self.current_time.minute < 30)):
                    if self.hs.door_front == True:
                        d = datetime.now() - self.df_last
                        self.hs.toggle_door_front(datetime.now(), cur)
                    if self.hs.door_back == True:
                        d = datetime.now() - self.db_last
                        self.hs.toggle_door_front(datetime.now(), cur)
                    if self.hs.door_garage_out == True:
                        d = datetime.now() - self.dgo_last
                        self.hs.toggle_door_front(datetime.now(), cur)
                    rand = random.randint(1, 2880)
                    if 1 <= rand < 20:
                        self.hs.toggle_door_front(datetime.now(), cur)
                        self.df_last(datetime.now())
                    if 20 <= rand < 40:
                        self.hs.toggle_door_back(datetime.now(), cur)
                        self.db_last(datetime.now())
                    if 20 <= rand < 40:
                        self.hs.toggle_door_garage_out(datetime.now(), cur)
                        self.dgo_last(datetime.now())
                    delta = datetime.now() - self.current_time
                    time.sleep(30 - delta.seconds)
                    self.current_time = datetime.now()
                while ((self.current_time.hour >= 7 and self.current_time.minute >= 30) and (self.current_time.hour < 16)):
                    print('helo')
                    delta = datetime.now() - self.current_time
                    time.sleep(30 - delta.seconds)
                    self.current_time = datetime.now()
                while ((self.current_time.hour >= 16) and (self.current_time.hour <= 22 and self.current_time.minute < 30)):
                    print('helo')
                    delta = datetime.now() - self.current_time
                    time.sleep(30 - delta.seconds)
                    self.current_time = datetime.now()
                while (((self.current_time.hour >= 22 and self.current_time.minute >= 30) and (self.current_time.hour < 24 and self.current_time.minute < 59 and self.current_time.second < 59)) or ((self.current_time.hour >= 0) and (self.current_time.hour < 5))):
                    if self.current_time.weekday >= 5:
                        break
                    print('helo')
                    delta = datetime.now() - self.current_time
                    time.sleep(30 - delta.seconds)
                    self.current_time = datetime.now()
            else:
                while ((self.current_time.hour >= 5) and (self.current_time.hour >= 22 and self.current_time.minute >= 30)):
                    print('helo')
                    delta = datetime.now() - self.current_time
                    time.sleep(30 - delta.seconds)
                    self.current_time = datetime.now()
                while (((self.current_time.hour >= 22 and self.current_time.minute >= 30) and (self.current_time.hour < 24 and self.current_time.minute < 59 and self.current_time.second < 59)) or ((self.current_time.hour >= 0) and (self.current_time.hour < 5))):
                    if self.current_time.weekday < 5:
                        break
                    print('helo')
                    delta = datetime.now() - self.current_time
                    time.sleep(30 - delta.seconds)
                    self.current_time = datetime.now()
    def hvac_update(self):
        temp_sum = 0
        temp_dif = self.outside_temp - self.inside_temp
        temp_thresh = self.inside_temp - self.target_temp
        self.outside_temp = ms.Hourly('72228', datetime.now(), datetime.now()).convert(units.imperial).fetch()['temp'].iloc[0]
        if temp_dif > 0:
            temp_sum = temp_sum + (temp_dif/600)
            if self.hs.door_front == True:
                temp_sum = temp_sum + .2
            if self.hs.door_back == True:
                temp_sum = temp_sum + .2
            if self.hs.door_garage_out == True:
                temp_sum = temp_sum + .2
            if temp_thresh > 2:
                if self.cooldown == 0:
                    self.hs.toggle_hvac(datetime.now(), 0, cur)
                    self.hvac_last = datetime.now()
                    self.cooldown = 10
                    temp_sum = temp_sum - .5
            else:
                if self.hs.hvac == True:
                    if temp_thresh > 0:
                        temp_sum = temp_sum - .5
                        self.cooldown -= 1
                    else:
                        temp_sum = temp_sum + .5
                        self.cooldown -= 1
        elif temp_dif < 0:
            temp_sum = temp_sum + (temp_dif/600)
            if self.hs.door_front == True:
                temp_sum = temp_sum - .2
            if self.hs.door_back == True:
                temp_sum = temp_sum - .2
            if self.hs.door_garage_out == True:
                temp_sum = temp_sum - .2
            if temp_thresh < -2:
                if self.cooldown == 0:
                    self.hs.toggle_hvac(datetime.now(), 0, cur)
                    self.hvac_last = datetime.now()
                    self.cooldown = 10
                    temp_sum = temp_sum + .5
            else:
                if self.hs.hvac == True:
                    if temp_thresh < 0:
                        temp_sum = temp_sum + .5
                        self.cooldown -= 1
                    else:
                        temp_sum = temp_sum - .5
                        self.cooldown -= 1
        self.inside_temp = self.inside_temp + temp_sum
        cur.execute("INSERT INTO hvac (time, interior_temp, exterior_temp, target_temp) VALUES (%s, %s, %s, %s)", (datetime.now(), self.inside_temp, self.outside_temp, self.target_temp))
        conn.commit()
        
        
