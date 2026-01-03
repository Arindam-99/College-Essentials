#v. Bayes' Theorem-Based Classifier
dataset = [
 ('Sunny', 'Hot', 'No'),
 ('Sunny', 'Mild', 'Yes'),
 ('Overcast', 'Cool', 'Yes'),
 ('Rainy', 'Mild', 'Yes'),
]
def separate_by_class(data):
 separated = {}
 for w, t, c in data:
 separated.setdefault(c, []).append((w, t))
 return separated
def class_probabilities(separated, total_samples):
 return {cls: len(separated[cls]) / total_samples for cls in separated}
def conditional_probability(separated, feature, index, cls):
 count = 0
 total = len(separated[cls])
 for sample in separated[cls]:
 if sample[index] == feature: count += 1
 return count / total if total > 0 else 0
def predict(weather, temp):
 sep = separate_by_class(dataset)
 class_probs = class_probabilities(sep, len(dataset))
 results = {}
 for cls in sep:
 pw = conditional_probability(sep, weather, 0, cls)
 pt = conditional_probability(sep, temp, 1, cls)
 pc = class_probs[cls]
 results[cls] = pw * pt * pc
 predicted = max(results, key=results.get)
 print("Posterior Probabilities:", results)
 return predicted
weather = "Sunny"; temp = "Cool"
print("Classifying Weather =", weather, "Temp =", temp)
result = predict(weather, temp)
print("Predicted Class:", result)