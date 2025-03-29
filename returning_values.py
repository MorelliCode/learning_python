
# This is how we can return a function
def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is:" , str(sum))

# This is how we can return MULTIPLE values from a function
# and map them onto MULTIPLE variables
def convert_seconds(seconds):
    hours = seconds //3600
    minutes = (seconds - hours * 3600)//60
    remaining_seconds = seconds - hours * 3600 - minutes *60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)


# This is what happens when you read a value from a function
# with no return value. It's "None"
def greeting(name):
    print ("Welcome, " + name)
result = greeting("Chris")
print(result) # "None"