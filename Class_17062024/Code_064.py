def make_pizza(*topings):
    for topin in topings:
        print(topin)
        # return topin -return exits after returning the first iteration of the loop
        # -If the intention is to handle multiple toppings and return or print all of them,
        # you would need to adjust the function make_pizza to collect all toppings and possibly return
        # them as a list or tuple, or print them directly within the function rather than returning a single topping.

# maala = make_pizza("Olives", "mushroom", "paneer" )
# print("Maala order: Pizza with toppings- ", maala)

pramod = make_pizza("tomato")
bharkave = make_pizza("Olives","mushroom", "paneer" )
vinay = make_pizza("mushroom","pineapple","paneer","sweetcorn")
