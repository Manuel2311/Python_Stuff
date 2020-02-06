#First class function
# def add 5(number):
#     return number +5

# def add 10(number):
#     return number +10

def create_adder(value):
    def adder(number):
        return value +number

    return adder


process_func=create_adder(10)
#This gives the function a specification

print(process_func(110))
