def categorize_age(age):
    if age < 13:
        return "a child"
    elif age < 20:
        return "a teenager"
    elif age < 60:
        return "an adult"
    else:
        return "a senior citizen"


def main():
    # Taking user inputs
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    hobby = input("Enter your hobby: ")
    
    # Categorizing age
    category = categorize_age(age)
    
    # Printing personalized message
    print("\n--- Personalized Message ---")
    print(f"Hello {name}!")
    print(f"You are {category}.")
    print(f"It's great that you enjoy {hobby}!")
    print("Keep doing what you love!")


if __name__ == "__main__":
    main()