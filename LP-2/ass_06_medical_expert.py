knowledge_base = {
    "cold": [
        "1: Tylenol",
        "2: Panadol",
        "3: Nasal spray",
        "4: Please wear warm clothes!"
    ],
    "influenza": [
        "1: Tamiflu",
        "2: Panadol",
        "3: Zanamivir",
        "4: Please take a warm bath and do salt gargling!"
    ],
    "typhoid": [
        "1: Chloramphenicol",
        "2: Amoxicillin",
        "3: Ciproflaxacin",
        "4: Azithromycin",
        "5: Please do complete bed rest and take soft diet!"
    ],
    "chicken pox": [
        "1: Varicella vaccine",
        "2: Immunoglobulin",
        "3: Acetomenaphin",
        "4: Acyclovir",
        "5: Please do have oatmeal and stay at home!"
        "6: Take frequent baths with neem tree leaves soaked in it"
    ],
    "measles": [
        "1: Tylenol",
        "2: Aleve",
        "3: Advil",
        "4: Vitamin A",
        "5: Please get rest and use more liquid!"
    ],
    "malaria": [
        "1: Aralen",
        "2: Qualaquin",
        "3: Plaquenil",
        "4: Mefloquine",
        "5: Please do not sleep in open air and cover your full skin!"
    ]
}


def ask_symptoms():
    symptoms = []
    print("Please enter your symptoms one by one.\n\n Type 'done' when finished.")
    while True:
        symptom = input("Symptom: ").lower()
        if symptom == 'done':
            break
        symptoms.append(symptom)
    return symptoms

def determine_facility(symptoms):
    
    if (symptom in symptoms for symptom in ["fever","rash","cold"]):
        print("you have chicken pox")
        return knowledge_base["chicken pox"]
    
    elif (symptom in symptoms for symptom in ["diarrhea","nausia","fatigue"]):
        print("you have Malaria")
        return knowledge_base["malaria"]
    
    elif (symptom in symptoms for symptom in ["fever","headache","fatigue"]):
        print("you have Typhoid")
        return knowledge_base["typhoid"]
    
    elif (symptom in symptoms for symptom in ["fever","muscle ache","dry cough"]):
        print("you have Influenza")
        return knowledge_base["influenza"]
    
    elif (symptom in symptoms for symptom in ["runny nose","eyes inflamation","sore throat"]):
        print("you have Measles")
        return knowledge_base["measles"]
    
    else:
        return "Your symptom is generic type \n  You can consider visiting a primary care physician."

def main():
    print("Welcome to the Medical Facility Recommendation System! \n")
    print("This system will help you determine the type of medications you need for treatment.\n\n DISCLAIMER : This bot is just a prototype, don't fully trust its authenticity)\n\n")
    symptoms = ask_symptoms()
    recommendation = determine_facility(symptoms)
    print("\n Suggested treatment measures:\n\n\n", recommendation)
    print("\n\n")

if __name__ == "__main__":
    main()
