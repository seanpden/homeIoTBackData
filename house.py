import psycopg2
from datetime import datetime, timedelta

class House:
    def __init__(self) -> None:
        # Doors - 30 seconds, 16/day enter/exit M-F, 32/day e/e S-S
        self.door_front = False # DONE
        self.door_back = False
        self.door_garage_out = False
        self.door_garage_one = False
        self.door_garage_two = False
 
        # Lights - 60 watts, 5:00 - 7:30, 16:00 - 22:30
        self.bedroom_overhead_light = False # DONE
        self.bedroom_lamp_one = False # DONE
        self.bedroom_lamp_two = False # DONE
        self.bath_light_one = False #DONE
        self.bath_light_two = False #DONE
        self.lr_overhead_light = False
        self.lr_lamp_one = False
        self.lr_lamp_two = False
        self.kitchen_overhead_light = False

        # TVs
        self.bedroom_TV = False # 100 watts, 2hr/day MF, 4hr/day SS DONE
        self.lr_tv = False # 636 watts, 4hr/day MF, 8hr/day SS

        # Baths - Exhaust fans 30 w
        self.bath = False # 2/day MF, 3/day SS. 30 gallons (65% hot, 35% cold) DONE
        self.shower = False # 2/day MF, 3/day SS. 25 gallons (65% hot, 35% cold) DONE

        # Appliances
        self.washer = False # 500 watts, 4 loads a week, 30 min, 20 gallons (85% hot)
        self.dryer = False # 3000 watts, 4 loads a week, 30 min
        self.dishwasher = False # 1800 watts, 4 loads a week, 45 min, 6 gallons (100% hot)
        self.stove = False # 3500 watts, 15 min/day MF, 30 min/day SS
        self.oven = False # 4000 watts, 45 min/day MF, 60 min/day SS
        self.microwave = False # 1100w, 20 min/day MF, 30 min/day SS
        self.fridge = False # 150w
        self.htwater = False # 4500w
        self.hvac = False # 3500w


    def toggle_door_front(self, timestamp, cur):
        self.door_front = not self.door_front

        if self.door_front == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "door_front", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "door_front", False))

    def toggle_door_back(self, timestamp, cur):
        self.door_back = not self.door_back

        if self.door_back == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "door_back", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "door_back", False))

    def toggle_door_garage_out(self, timestamp, cur):
        self.door_garage_out = not self.door_garage_out

        if self.door_garage_out == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "garage_door_out", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "garage_door_out", False))

    def toggle_door_garage_one(self, timestamp, cur):
        self.door_garage_one = not self.door_garage_one

        if self.door_garage_one == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "garage_door_one", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "garage_door_one", False))

    def toggle_door_garage_two(self, timestamp, cur):
        self.door_garage_two = not self.door_garage_two

        if self.door_garage_two == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "garage_door_two", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "garage_door_two", False))

    def toggle_bedroom_overhead_light(self, timestamp, elect, cur):
        self.bedroom_overhead_light = not self.bedroom_overhead_light

        if self.bedroom_overhead_light == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "bedroom_overhead_light", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "bedroom_overhead_light", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))

    def toggle_bedroom_lamp_one(self, timestamp, elect, cur):
        self.bedroom_lamp_one = not self.bedroom_lamp_one

        if self.bedroom_lamp_one == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "bedroom_lamp_one", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "bedroom_lamp_one", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))

    def toggle_bedroom_lamp_two(self, timestamp, elect, cur):
        self.bedroom_lamp_two = not self.bedroom_lamp_two

        if self.bedroom_lamp_two == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "bedroom_lamp_two", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "bedroom_lamp_two", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))

    def toggle_bath_light_one(self, timestamp, elect, cur):
        self.bath_light_one = not self.bath_light_one

        if self.bath_light_one == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "bath_light_one", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "bath_light_one", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))

    def toggle_bath_light_two(self, timestamp, elect, cur):
        self.bath_light_two = not self.bath_light_two

        if self.bath_light_two == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "bath_light_two", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "bath_light_two", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))

    def toggle_lr_overhead_light(self, timestamp, elect, cur):
        self.lr_overhead_light = not self.lr_overhead_light

        if self.lr_overhead_light == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "lr_overhead_light", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "lr_overhead_light", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))

    def toggle_lr_lamp_one(self, timestamp, elect, cur):
        self.lr_lamp_one = not self.lr_lamp_one

        if self.lr_lamp_one == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "lr_lamp_one", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "lr_lamp_one", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))

    def toggle_lr_lamp_two(self, timestamp, elect, cur):
        self.lr_lamp_two = not self.lr_lamp_two

        if self.lr_lamp_two == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "lr_lamp_two", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "lr_lamp_two", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))

    def toggle_kitchen_overhead_light(self, timestamp, elect, cur):
        self.kitchen_overhead_light = not self.kitchen_overhead_light

        if self.kitchen_overhead_light == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "kitchen_overhead_light", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "kitchen_overhead_light", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))

    def toggle_bedroom_TV(self, timestamp, elect, cur):
        self.bedroom_TV = not self.bedroom_TV

        if self.bedroom_TV == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "bedroom_TV", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "bedroom_TV", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))

    def toggle_lr_tv(self, timestamp, elect, cur):
        self.lr_tv = not self.lr_tv

        if self.lr_tv == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "lr_tv", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "lr_tv", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))

    def toggle_bath(self, timestamp, wtr, cur):
        self.bath = not self.bath

        if self.bath == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "bath", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "bath", False))
            cur.execute("INSERT INTO water (cost, time) VALUES (%s, %s)", (wtr, timestamp))

    def toggle_htwater(self, timestamp, wtr, elect, cur):
        self.htwater = not self.htwater

        if self.htwater == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "htwater", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "bath", False))
            cur.execute("INSERT INTO water (cost, time) VALUES (%s, %s)", (wtr, timestamp))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))
    
    def toggle_shower(self, timestamp, wtr, cur):
        self.shower = not self.shower

        if self.shower == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "shower", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "shower", False))
            cur.execute("INSERT INTO water (cost, time) VALUES (%s, %s)", (wtr, timestamp))

    def toggle_washer(self, timestamp, wtr, elect, cur):
        self.washer = not self.washer

        if self.washer == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "washer", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "washer", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))
            cur.execute("INSERT INTO water (cost, time) VALUES (%s, %s)", (wtr, timestamp))

    def toggle_dryer(self, timestamp, elect, cur):
        self.dryer = not self.dryer

        if self.dryer == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "dryer", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "dryer", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))
        

    def toggle_dishwasher(self, timestamp, wtr, elect, cur):
        self.dishwasher = not self.dishwasher

        if self.dishwasher == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "dishwasher", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "dishwasher", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))
            cur.execute("INSERT INTO water (cost, time) VALUES (%s, %s)", (wtr, timestamp))

    def toggle_stove(self, timestamp, elect, cur):
        self.stove = not self.stove

        if self.stove == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "stove", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "stove", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))

    def toggle_oven(self, timestamp, elect, cur):
        self.oven = not self.oven

        if self.oven == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "oven", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "oven", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))

    def toggle_microwave(self, timestamp, elect, cur):
        self.microwave = not self.microwave

        if self.oven == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "microwave", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "microwave", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))

    def toggle_fridge(self, timestamp, elect, cur):
        self.fridge = not self.fridge

        if self.fridge == True:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "fridge", True))
        else:
            cur.execute("INSERT INTO events (time, type, status) VALUES (%s, %s, %s)", (timestamp, "fridge", False))
            cur.execute("INSERT INTO electric (cost, time) VALUES (%s, %s)", (elect, timestamp))
