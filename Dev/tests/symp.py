import re

# Define doctors and their specialties
doctors = {
    "family_doctor": "Family Doctor",
    "ent_specialist": "Ear, Eyes, and Throat Specialist",
    "orthopedic_specialist": "Orthopedic Specialist",
    "gynecologist": "Gynecologist"
}


keywords = {
    "family_doctor": ["fever", "cough", "cold", "headache", "fatigue", "stomach ache", "flu"],
    "ent_specialist": ["ear", "throat", "eyes", "hearing", "vision", "infection", "sinus", "sore throat"],
    "orthopedic_specialist": ["bone", "joint", "fracture", "arthritis", "sprain", "back pain", "knee pain", "shoulder pain"],
    "gynecologist": ["pregnancy", "baby", "menstruation", "period", "fertility", "cramps", "contraception", "ovary", "uterus"]
}


def classify_symptoms(symptoms):
    symptoms = symptoms.lower()
    symptom_counts = {doctor: 0 for doctor in doctors} 

    for doctor, kw_list in keywords.items():
        for keyword in kw_list:
            if re.search(r'\b' + re.escape(keyword) + r'\b', symptoms):
                symptom_counts[doctor] += 1


    suggested_doctor = max(symptom_counts, key=symptom_counts.get)

    if symptom_counts[suggested_doctor] == 0:
        return "General Physician (None of the specialists matched your symptoms)"
    else:
        return doctors[suggested_doctor]


user_symptoms = input("Please describe your symptoms: ")

suggested_doctor = classify_symptoms(user_symptoms)

print(f"You should see: {suggested_doctor}")
