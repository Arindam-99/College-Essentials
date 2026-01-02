# iv. Fuzzy Restaurant Rating System
def poor(x):
 if x <= 3: return 1
 elif 3 < x < 5: return (5 - x) / 2
 return 0
def average(x):
 if 3 < x < 5: return (x - 3) / 2
 elif 5 <= x <= 7: return (7 - x) / 2
 return 0
def excellent(x):
 if x >= 8: return 1
 elif 6 < x < 8: return (x - 6) / 2
 return 0
def bad(x):
 if x <= 3: return 1
 elif 3 < x < 5: return (5 - x) / 2
 return 0
def decent(x):
 if 3 < x < 5: return (x - 3) / 2
 elif 5 <= x <= 7: return (7 - x) / 2
 return 0
def great(x):
 if x >= 8: return 1
 elif 6 < x < 8: return (x - 6) / 2
 return 0
def cheap(x):
 if x <= 3: return 1
 elif 3 < x < 5: return (5 - x) / 2
 return 0
def moderate(x):
 if 3 < x < 5: return (x - 3) / 2
 elif 5 <= x <= 7: return (7 - x) / 2
 return 0
def expensive(x):
 if x >= 8: return 1
 elif 6 < x < 8: return (x - 6) / 2
 return 0
def defuzzify(low, medium, high):
 numerator = (low * 1) + (medium * 3) + (high * 5)
 denominator = (low + medium + high)
 if denominator == 0: return 0
 return numerator / denominator
def restaurant_rating(service, ambience, cost):
 S_poor = poor(service); S_avg = average(service); S_exc = excellent(service)
 A_bad = bad(ambience); A_dec = decent(ambience); A_great = great(ambience)
 C_cheap = cheap(cost); C_mod = moderate(cost); C_exp = expensive(cost)
 print("Membership Values:")
 print("Service → Poor:", round(S_poor,2), "Average:", round(S_avg,2), "Excellent:", round(S_exc,2))
 print("Ambience → Bad:", round(A_bad,2), "Decent:", round(A_dec,2), "Great:", round(A_great,2))
 print("Cost → Cheap:", round(C_cheap,2), "Moderate:", round(C_mod,2), "Expensive:", round(C_exp,2))
 high = max(S_exc, A_great, min(S_exc, A_great, C_mod))
 medium = max(S_avg, A_dec)
 low = max(min(C_exp, S_poor), A_bad)
 rating = defuzzify(low, medium, high)
 return rating
service = 7; ambience = 8; cost = 4
print("Input → Service:", service, "Ambience:", ambience, "Cost:", cost)
rating = restaurant_rating(service, ambience, cost)
print("\nFinal Restaurant Rating:", round(rating, 2), "stars")
