# ii. Fuzzy Logic-Based Temperature Controller
def cold(x):
 if x <= 10: return 1
 elif 10 < x < 20: return (20 - x) / 10
 else: return 0
def warm(x):
 if 15 < x < 25: return (x - 15) / 10
 elif 25 <= x <= 35: return (35 - x) / 10
 else: return 0
def hot(x):
 if x >= 40: return 1
 elif 30 < x < 40: return (x - 30) / 10
 else: return 0
def defuzzify(power_low, power_med, power_high):
 numerator = (power_low * 20) + (power_med * 50) + (power_high * 90)
 denominator = (power_low + power_med + power_high)
 if denominator == 0: return 0
 return numerator / denominator
def fuzzy_temperature_controller(temp):
 µ_cold = cold(temp)
 µ_warm = warm(temp)
 µ_hot = hot(temp)
 print("Membership Values:")
 print("Cold:", round(µ_cold, 2))
 print("Warm:", round(µ_warm, 2))
 print("Hot :", round(µ_hot, 2))
 power_low = µ_hot; power_med = µ_warm; power_high = µ_cold
 final_output = defuzzify(power_low, power_med, power_high)
 return final_output
temp = 18
print("Input Temperature:", temp)
heater_power = fuzzy_temperature_controller(temp)
print("\nFinal Heater Power Output:", round(heater_power, 2), "%")