#i. Rule-Based Expert System for Medical Diagnosis

def diagnose(symptoms):
 symptoms = [s.lower() for s in symptoms]
 if "fever" in symptoms and "cough" in symptoms and "sore throat" in symptoms:
 return "Likely Diagnosis: Flu"
 if "fever" in symptoms and "headache" in symptoms and "vomiting" in symptoms:
 return "Likely Diagnosis: Dengue"
 if "runny nose" in symptoms and "sneezing" in symptoms:
 return "Likely Diagnosis: Common Cold"
 if "chest pain" in symptoms and "shortness of breath" in symptoms:
 return "Likely Diagnosis: Asthma"
 if "stomach pain" in symptoms and "diarrhea" in symptoms:
 return "Likely Diagnosis: Food Poisoning"
 return "Diagnosis Uncertain – More symptoms needed."
user_input = "fever, cough, sore throat"
symptom_list = [x.strip() for x in user_input.split(",")]
print("Symptoms:", symptom_list)