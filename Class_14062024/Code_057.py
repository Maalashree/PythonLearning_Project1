# def allowed_to_attend_python_class(name, password):
#     if name == "Maala":
#         if password == "yes":
#             print("you are allowed to enter")
#         else:
#             print("you are not allowed")
#
#
# allowed_to_attend_python_class("Maala", "yes")

def allowed_to_attend_python_class(name):
    match name:
        case "DEll":
              print("DEll is allowed")
        case "Maala":
              print("Maala is allowed")
        case _:
              print("Not allowed")

allowed_to_attend_python_class("Maala")


