# Function to validate input
def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# BMI Calculator
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Function to categorize BMI
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")

    # Input weight and height
    weight = get_valid_input("Enter your weight in kilograms: ")
    height = get_valid_input("Enter your height in meters: ")

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Categorize BMI
    category = categorize_bmi(bmi)

    # Display the result
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()
