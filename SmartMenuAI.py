"""
# This is a ruled based smart menu suggestion system.
# This AI will work with the given loops.
# You can select a budjet and select a the spice level and what type of food you need like veg or non veg or vegan. 
# As per your selection this will suggest the food for you.

"""
"""
# The food Menu Database

Food Name {

Portion Size : Small, Medium or large.
Type : Veg, Non Veg or Vegan 
Price: Total how much you need to pay
}

"""
"""
# The Below One Is a Sample Database that i am going to use as a 
reference and how the different type of foods available.

"""

Menu_Database ={
    
    "Kothu" :{
        
        "Veg":{
            
            "Vegetable Kothu" :{
                "Small" : 400,
                "Medium": 600,
                "Large" : 800
            }
        },
        
        "Non Veg":{
            
            "Egg Kothu":{
                "Small" :450,
                "Medium":650,
                "Large":850
            },
                        
            "Chicken Kothu":{
                "Small" :600,
                "Medium":800,
                "Large":1000
            },
            
            "Fish Kothu":{
                "Small" :500,
                "Medium":700,
                "Large":900
            },

            "Prawn Kothu":{
                "Small" :800,
                "Medium":1000,
                "Large":1200
            },

            "Beef Kothu":{
                "Small" :1000,
                "Medium":1300,
                "Large":1600
            },
        },

        "Vegan":{    
            "Vegan Kothu":{
                "Small" :700,
                "Medium":900,
                "Large":1100
            }
        }
    },

    "Nasi Goreng" :{
        
        "Non Veg":{
            
            "Chicken Nasi Goreng":{
                "Medium":800,
                "Large":1000
            },

            "Beef Nasi Goreng":{
                "Medium":1000,
                "Large":1200
            },

            "Sea Food Mix Nasi Goreng":{
                "Medium":1000,
                "Large":1200
            }
        }
    },

    "Biriyani":{
        
        "Veg":{
            "Vegetable Biriyani":{
                "Medium":400
            },
            "Paneer Biriyani":{
                "Medium":500,
                "Large":700
            }
        },
        
        "Non Veg":{
            
            "Egg Biriyani":{
                "Small" :550,
                "Medium":600,
                "Large":700
            },

            "Prawn Biriyani":{
                "Medium":700,
                "Large":900
           },
             
             "Chicken Biriyani":{
                "Medium":1000,
                "Large":1300
            },

           "Beef Biriyani":{
                "Medium":1000,
                "Large":1200
           },

            "Mutton Biriyani":{
                "Medium":1300,
                "Large":1500
           }             
        }
    }
}
Curry_MenuDataBase={
    
        "Curry":{
            "Veg":{
                "Paneer Curry":400,
                "Sambar Curry":250,
                "Dhaal Curry":150,
                "Potato Curry":200
        },
        
            "Non Veg":{
                "Chicken Curry":450,
                "Fish Curry":380,
                "Prawn Curry":500,
                "Beef Curry":600,
                "Mutton Curry":650
        }
    }
}

Menu_Drinkdatabase={   
    
    "Drinks":{
        
        "Hot":{
            "Tea":70,
            "Coffee":80,
            "Plain Tea":40
        },

        "Cool":{
            "Iced Tea":150,
            "Iced Coffee":200,
            "Lemon Mojito":250
        },

        "Fruit Juice":{
            "Apple Juice":350,
            "PineApple Juice":380,
            "Orange Juice":300,
            "Strawberry Juice":400,
            "Mango Juice":250
        }
   }
}

Spice_Database = {
    
    "Kothu": ["Low", "Medium", "Extra"],
    "Nasi Goreng": ["Low", "Medium", "Extra"]
}


# welcome user
user_name = input("Hello, could you please insert your name: ")
print(f"\nHello {user_name}..\nWelcome to Great Dine Restaurant..\nEnjoy your meal!\n")

# Show full food menu
print("...Here is our full food menu...")
for foods in Menu_Database:
    print(f"- {foods} -")


# food ordering

category = input("\nWhat would you like to order?: ").title()
while category not in Menu_Database:
    print("Sorry, this category is not available. Try again.")
    category = input("What would you like to order?: ").title()

foodtype = input(f"What type of food you like ({', '.join(Menu_Database[category].keys())}): ").title()
while foodtype not in Menu_Database[category]:
    print("Sorry, this option is not available. Try again.")
    foodtype = input("What type of food you like: ").title()

dish = input(f"Please select a dish ({', '.join(Menu_Database[category][foodtype].keys())}): ").title()
while dish not in Menu_Database[category][foodtype]:
    print("Sorry, this dish is not available. Try again.")
    dish = input("Please select a dish: ").title()

foodportionsize = input(f"What is your preferred portion size ({', '.join(Menu_Database[category][foodtype][dish].keys())})? ").title()
while foodportionsize not in Menu_Database[category][foodtype][dish]:
    print("Invalid portion size. Try again.")
    foodportionsize = input("What is your preferred portion size? ").title()

# Base food price

total_price = Menu_Database[category][foodtype][dish][foodportionsize]
print(f"\nYour first order is {dish} ({foodportionsize}) - Price: Rs.{total_price}")

# Drink order

userdrinksuggestion = input("\nDo you need any drinks? (yes/no): ").lower()
if userdrinksuggestion == "yes":
    print("\n...Here is our Drink Options...")
    for drink_category in Menu_Drinkdatabase["Drinks"]:
        print(f"- {drink_category} -")

    drinkselection = input("\nSelect drink category: ").title()
    while drinkselection not in Menu_Drinkdatabase["Drinks"]:
        print("Invalid drink category. Try again.")
        drinkselection = input("Select drink category: ").title()

    drinkselected = input(f"Select drink ({', '.join(Menu_Drinkdatabase['Drinks'][drinkselection].keys())}): ").title()
    while drinkselected not in Menu_Drinkdatabase["Drinks"][drinkselection]:
        print("Invalid drink. Try again.")
        drinkselected = input("Select drink: ").title()

    drink_price = Menu_Drinkdatabase["Drinks"][drinkselection][drinkselected]
    total_price += drink_price
    print(f"Drink added: {drinkselected} - Price: Rs.{drink_price}")
else:
    drinkselected = "Water"
    print(f"You chose no drinks. Water will be provided.")


# Curry Order

curryselection = input(f"\nDo you need any curry with {dish}? (yes/no): ").lower()
if curryselection == "yes":
    print("\n...Here is our Curry Options...")
    for curry_type in Curry_MenuDataBase["Curry"]:
        print(f"- {curry_type} -")

    currytype = input("Select curry type (Veg / Non Veg): ").title()
    while currytype not in Curry_MenuDataBase["Curry"]:
        print("Invalid option. Please select Veg or Non Veg.")
        currytype = input("Select curry type (Veg / Non Veg): ").title()

    curryselected = input(f"Select curry ({', '.join(Curry_MenuDataBase['Curry'][currytype].keys())}): ").title()
    while curryselected not in Curry_MenuDataBase["Curry"][currytype]:
        print("Invalid curry. Please select again.")
        curryselected = input(f"Select curry ({', '.join(Curry_MenuDataBase['Curry'][currytype].keys())}): ").title()

    curry_price = Curry_MenuDataBase["Curry"][currytype][curryselected]
    total_price += curry_price
    print(f"Curry added: {curryselected} - Price: Rs.{curry_price}")
else:
    curryselected = "Chicken Gravy"
    print(f"No curry selected. Default curry ({curryselected}) will be added.")


# Final Bill

print("\n-- Your Final Bill --")
print(f"Dish: {dish} ({foodportionsize})")
print(f"Curry: {curryselected}")
print(f"Drink: {drinkselected}")
print(f"Total Amount: Rs.{total_price}")

total_paid = 0  # Track cumulative payment other wise the while loop will stuck in a loop

while total_paid < total_price:
    try:
        paid_amount = int(input("Enter paid amount: Rs."))
        total_paid += paid_amount
        remaining = total_price - total_paid

        if remaining > 0:
            print(f"Insufficient money! You still need Rs.{remaining} more")
        else:
            balance = -remaining  # remaining is negative or 0
            print(f"Balance: Rs.{balance}")
            break

    except ValueError:
        print("Please enter a valid number.")

print(f"\nThank you for dining at Great Dine Restaurant! Enjoy your meal {user_name}\n Come Again...")