# Activity 1: Basic Function Arguments (Animals)
def pet_info(species, nickname):
    print(f"I have a {species} and its name is {nickname}.")


# Function calls for Activity 1
pet_info("hamster", "Ferdinand Magellan")
pet_info("parrot", "José Protasio Rizal Mercado y Alonso Realonda")
pet_info("turtle", "Adolf Hitler")


# Activity 2: Positional vs Keyword Arguments

# Using positional arguments
pet_info("fish", "Rodrigo Duterte")

# Using keyword arguments (order reversed)
pet_info(nickname="Allan Peter Cayetano", species="cat")


# Activity 3: Default Arguments

# Redefining the function with a default species
def pet_info(nickname, species="dog"):
    print(f"I have a {species} and its name is {nickname}.")


# Function calls for Activity 3
pet_info("Bongbong Marcos Jr")#Uses default species"
pet_info("Kween Yasmin", "bird")   #Overrides default value


# Activity 4: Custom Function (Drink Order)
def place_order(drink_name, cup_size="medium", with_ice=False):
    # Determine if drink is iced or hot
    temperature = "iced" if with_ice else "hot"
    return f"Your order: {cup_size} {temperature} {drink_name}"


# Function calls for Activity 4
print(place_order("coffee"))                                   # Default order
print(place_order("chocolate", cup_size="large", with_ice=False))  # Large hot chocolate
print(place_order("milk tea", cup_size="small", with_ice=True))    # Small iced milk tea


# Activity 5: Mini Challenge - Calculator
def calculate(action, value1, value2=1):
    if action == "add":
        return value1 + value2
    elif action == "multiply":
        return value1 * value2
    elif action == "subtract":
        return value1 - value2
    else:
        return "Invalid operation"


# Function calls for Activity 5
print(calculate("add", 5, 10))
print(calculate("multiply", value1=3, value2=4))
print(calculate("subtract", 20))     # Uses default value2
print(calculate("divide", 10, 2))    # Invalid operation

