class UserProfile:
    def __init__(self, name, age, weight, height, physical_activity_level, dietary_preferences):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.physical_activity_level = physical_activity_level
        self.dietary_preferences = dietary_preferences

def get_user_profile():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in cm): "))
    physical_activity_level = input("Enter your physical activity level (sedentary, lightly active, moderately active, very active, or extra active): ")
    dietary_preferences = input("Enter your dietary preferences (vegan, vegetarian, pescatarian, or none): ")
    return UserProfile(name, age, weight, height, physical_activity_level, dietary_preferences)
