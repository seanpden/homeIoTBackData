import pandas as pd
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
        self.bath_light_one = False
        self.bath_light_two = False
        self.lr_overhead_light = False
        self.lr_lamp_one = False
        self.lr_lamp_two = False
        self.kitchen_overhead_light = False

        # TVs
        self.bedroom_TV = False # 100 watts, 2hr/day MF, 4hr/day SS DONE
        self.lr_tv = False # 636 watts, 4hr/day MF, 8hr/day SS

        # Baths - Exhaust fans 30 w
        self.bath = False # 2/day MF, 3/day SS. 30 gallons (65% hot, 35% cold)
        self.shower = False # 2/day MF, 3/day SS. 25 gallons (65% hot, 35% cold)

        # Appliances
        self.washer = False # 500 watts, 4 loads a week, 30 min, 20 gallons (85% hot)
        self.dryer = False # 3000 watts, 4 loads a week, 30 min
        self.dishwasher = False # 1800 watts, 4 loads a week, 45 min, 6 gallons (100% hot)
        self.stove = False # 3500 watts, 15 min/day MF, 30 min/day SS
        self.oven = False # 4000 watts, 45 min/day MF, 60 min/day SS
        self.microwave = False # 1100w, 20 min/day MF, 30 min/day SS
        self.fridge = False # 150w
        self.hvac = False # 3500w

        self.df = {"Time": [], "Device": [], "Action": [], "Water Usage": [], "Electric Usage": []}
        self.df = pd.DataFrame(self.df)

    def toggle_door_front(self, timestamp):
        self.door_front = not self.door_front

        if self.door_front == True:
            self.df.loc[len(self.df.index)] = [timestamp, "door_front", "Open", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "door_front", "Close", 0, 0]

    def toggle_door_back(self, timestamp):
        self.door_back = not self.door_back

        if self.door_back == True:
            self.df.loc[len(self.df.index)] = [timestamp, "door_back", "Open", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "door_back", "Close", 0, 0]

    def toggle_door_garage_out(self, timestamp):
        self.door_garage_out = not self.door_garage_out

        if self.door_garage_out == True:
            self.df.loc[len(self.df.index)] = [timestamp, "door_garage_out", "Open", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "door_garage_out", "Close", 0, 0]

    def toggle_door_garage_one(self, timestamp):
        self.door_garage_one = not self.door_garage_one

        if self.door_garage_one == True:
            self.df.loc[len(self.df.index)] = [timestamp, "door_garage_one", "Open", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "door_garage_one", "Close", 0, 0]

    def toggle_door_garage_two(self, timestamp):
        self.door_garage_two = not self.door_garage_two

        if self.door_garage_two == True:
            self.df.loc[len(self.df.index)] = [timestamp, "door_garage_two", "Open", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "door_garage_two", "Close", 0, 0]

    def toggle_bedroom_overhead_light(self, timestamp, elect):
        self.bedroom_overhead_light = not self.bedroom_overhead_light

        if self.bedroom_overhead_light == True:
            self.df.loc[len(self.df.index)] = [timestamp, "bedroom_overhead_light", "On", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "bedroom_overhead_light", "Off", 0, elect]

    def toggle_bedroom_lamp_one(self, timestamp, elect):
        self.bedroom_lamp_one = not self.bedroom_lamp_one

        if self.bedroom_lamp_one == True:
            self.df.loc[len(self.df.index)] = [timestamp, "bedroom_lamp_one", "On", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "bedroom_lamp_one", "Off", 0, elect]

    def toggle_bedroom_lamp_two(self, timestamp, elect):
        self.bedroom_lamp_two = not self.bedroom_lamp_two

        if self.bedroom_lamp_two == True:
            self.df.loc[len(self.df.index)] = [timestamp, "bedroom_lamp_two", "On", 0, elect]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "bedroom_lamp_two", "Off", 0, 0]

    def toggle_bath_light_one(self, timestamp, elect):
        self.bath_light_one = not self.bath_light_one

        if self.bath_light_one == True:
            self.df.loc[len(self.df.index)] = [timestamp, "bath_light_one", "On", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "bath_light_one", "Off", 0, elect]

    def toggle_bath_light_two(self, timestamp, elect):
        self.bath_light_two = not self.bath_light_two

        if self.bath_light_two == True:
            self.df.loc[len(self.df.index)] = [timestamp, "bath_light_two", "On", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "bath_light_two", "Off", 0, elect]

    def toggle_lr_overhead_light(self, timestamp, elect):
        self.lr_overhead_light = not self.lr_overhead_light

        if self.lr_overhead_light == True:
            self.df.loc[len(self.df.index)] = [timestamp, "lr_overhead_light", "On", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "lr_overhead_light", "Off", 0, elect]

    def toggle_lr_lamp_one(self, timestamp, elect):
        self.lr_lamp_one = not self.lr_lamp_one

        if self.lr_lamp_one == True:
            self.df.loc[len(self.df.index)] = [timestamp, "lr_lamp_one", "On", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "lr_lamp_one", "off", 0, elect]

    def toggle_lr_lamp_two(self, timestamp, elect):
        self.lr_lamp_two = not self.lr_lamp_two

        if self.lr_lamp_two == True:
            self.df.loc[len(self.df.index)] = [timestamp, "lr_lamp_two", "On", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "lr_lamp_two", "Off", 0, elect]

    def toggle_kitchen_overhead_light(self, timestamp, elect):
        self.kitchen_overhead_light = not self.kitchen_overhead_light

        if self.kitchen_overhead_light == True:
            self.df.loc[len(self.df.index)] = [timestamp, "kitchen_overhead_light", "On", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "kitchen_overhead_light", "Off", 0, elect]

    def toggle_bedroom_TV(self, timestamp, elect):
        self.bedroom_TV = not self.bedroom_TV

        if self.bedroom_TV == True:
            self.df.loc[len(self.df.index)] = [timestamp, "bedroom_TV", "On", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "bedroom_TV", "Off", 0, elect]

    def toggle_lr_tv(self, timestamp, elect):
        self.lr_tv = not self.lr_tv

        if self.lr_tv == True:
            self.df.loc[len(self.df.index)] = [timestamp, "lr_tv", "On", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "lr_tv", "Off", 0, elect]

    def toggle_bath(self, timestamp, wtr):
        self.bath = not self.bath

        if self.bath == True:
            self.df.loc[len(self.df.index)] = [timestamp, "bath", "On", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "bath", "Off", wtr, 0]
    
    def toggle_shower(self, timestamp, wtr):
        self.shower = not self.shower

        if self.bath == True:
            self.df.loc[len(self.df.index)] = [timestamp, "shower", "On", 0, 0]
        else:
            self.df.loc[len(self.df.index)] = [timestamp, "shower", "Off", wtr, 0]

    def get_df(self):
        return self.df

    def export_df(self, how):
        if how == "CSV":
            self.df.to_csv()

if __name__ == "__main__":
    hs = House()
    hs.toggle_door_front(datetime.now())
    hs.toggle_door_front(datetime.now() + timedelta(seconds=+30))
    print(hs.get_df())
