class FoodItem:
    # Constructor to initialize instance attributes (name, fat, carbs, protein)
    def __init__(self, name="Water", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = float(fat)
        self.carbs = float(carbs)
        self.protein = float(protein)

    def get_calories(self, num_servings=1):
        # Calorie formula: fat*9 + carbs*4 + protein*4 per serving
        calories_per_serving = (self.fat * 9) + (self.carbs * 4) + (self.protein * 4)
        return calories_per_serving * num_servings

    def print_info(self):
        print(f"Nutritional information per serving of {self.name}:")
        print(f"  Fat: {self.fat:.2f} g")
        print(f"  Carbohydrates: {self.carbs:.2f} g")
        print(f"  Protein: {self.protein:.2f} g")


# Example usage
if __name__ == '__main__':
    # create a few food items and display info
    apple = FoodItem(name="Apple", fat=0.2, carbs=14.0, protein=0.3)
    peanut_butter = FoodItem(name="Peanut Butter", fat=50.0, carbs=20.0, protein=25.0)

    apple.print_info()
    print(f"  Calories per serving: {apple.get_calories(1):.2f} kcal\n")

    peanut_butter.print_info()
    print(f"  Calories per serving: {peanut_butter.get_calories(1):.2f} kcal")
