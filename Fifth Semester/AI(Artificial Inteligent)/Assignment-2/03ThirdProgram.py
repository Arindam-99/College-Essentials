# iii. Fuzzy Washing Machine Controller
def load_low(x):
 if x <= 2: return 1
 elif 2 < x < 4: return (4 - x) / 2
 return 0
def load_medium(x):
 if 2 < x < 4: return (x - 2) / 2
 elif 4 <= x <= 6: return (6 - x) / 2
 return 0
def load_high(x):
 if x >= 6: return 1
 elif 4 < x < 6: return (x - 4) / 2
 return 0
def dirt_light(x):
 if x <= 20: return 1
 elif 20 < x < 40: return (40 - x) / 20
 return 0
def dirt_medium(x):
 if 20 < x < 40: return (x - 20) / 20
 elif 40 <= x <= 60: return (60 - x) / 20
 return 0
def dirt_heavy(x):
 if x >= 60: return 1
 elif 40 < x < 60: return (x - 40) / 20
 return 0
def defuzzify(short, normal, long):
 numerator = (short * 10) + (normal * 30) + (long * 50)
 denominator = short + normal + long
 if denominator == 0: return 0
 return numerator / denominator
def washing_machine_controller(load, dirt):
 L_low = load_low(load); L_med = load_medium(load); L_high = load_high(load)
 D_light = dirt_light(dirt); D_med = dirt_medium(dirt); D_heavy = dirt_heavy(dirt)
 print("Membership Values:")
 print("Load → Low:", round(L_low,2), "Medium:", round(L_med,2), "High:", round(L_high,2))
 print("Dirt → Light:", round(D_light,2), "Medium:", round(D_med,2), "Heavy:", round(D_heavy,2))
 short = max(min(L_low, D_light), D_light)
 normal = max(min(L_med, D_med), min(L_low, D_med))
 long = max(min(L_high, D_heavy), min(L_med, D_heavy), D_heavy)
 final_time = defuzzify(short, normal, long)
 return final_time
load = 5; dirt = 55
print("Input Load:", load, "kg")
print("Input Dirt Level:", dirt, "%")
wash_time = washing_machine_controller(load, dirt)
print("\nFinal Wash Time:", round(wash_time, 2), "minutes")