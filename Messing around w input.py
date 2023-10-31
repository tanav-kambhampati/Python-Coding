import math


print("This is a simple calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponent")
print("6. Area")


operation = int(input("Enter the number that corresponds to your operation?"))

if operation > 6:
    print("This is not a valid response, please try again.")

def addition(): 
    num1 = float(input("What is your first number?"))
    num2 = float(input("What is your second number?"))
    result =  num1 + num2
    print(result)

def subtraction():
    num1 = float(input("What is your first number?"))
    num2 = float(input("What is your second number?"))
    result = num1 - num2
    print(result)

def multiplication():
    num1 = float(input("What is your first number?"))
    num2 = float(input("What is your second number?"))
    result = num1 * num2
    print(result)
    
def division():
    num1 = float(input("What is your dividend?"))
    num2 = float(input("What is your divisor?"))
    result = num1 / num2
    print(result)

def exponent():
    base = float(input("What is your base?"))
    power = float(input("What is your power?"))
    result = math.pow(base, power)
    print(result)

#START OF AREA FUNCTIONS!!!!!!!!
def area():
    print("1. Rectangle Area")
    print("2. Circle Area")
    print("3. X-sided Regular Polygon Area")

    function = int(input("Enter the number that corresponds to your operation"))

    if function > 3:
        print("This is not a valid response, please try again.")

    def rectangle_area():
        num1 = float(input("What is the base of your rectangle?"))
        num2 = float(input("What is the height of your rectangle?"))
        result = num1 * num2
        print(result)

    def circle_area():
        print("1. Decimal Form")
        print("2. Exact Form")

        form_number = int(input("Enter the number that corresponds to the type of answer you would like to recive"))
        
        if form_number > 2:
            print("This is not a valid response, please try again.")
        def decimal_form(): 
            circle_radius = float(input("What is the radius of your circle?"))
            answer = math.pow(circle_radius, 2)
            print(answer * math.pi)

        def exact_form():
            circle_radius = float(input("What is the radius of your circle?"))
            answer = circle_radius*circle_radius
            print(answer + "pi")

        if form_number == 1:
            decimal_form()
        if form_number == 2:
            exact_form()

    def x_sided_shape():
        print("1. Do you have an interior angle given ")
        print("2. Do you have a side length given?")
        print("3. Do you have a central angle?")
        
        situation = int(input("Enter the number that corresponds to your situation:"))

        def int_angle_given():
            num_of_sides = int(input("How many sides does your shape have?"))
            int_angle = float(input("What is the measure of your interior angle"))
            tri_small_angle = int_angle / 2
            tri_large_angle = 90 - tri_small_angle
            apothem = math.asin()
# CONTINUE HERE
        def side_length_given():
            num_of_sides = int(input("How many sides does your shape have?"))
            if num_of_sides < 3:
                print("This is not a valid response, please try again.")
            sumointangles = 180(num_of_sides - 2)
            int_angle = sumointangles / num_of_sides
            smol_angle = int_angle / 2
            top_angle = 90 - smol_angle
            side_length = int(input("What is the lenth of the side that is given"))
            half_side = side_length / 2
            apothem = half_side * math.tan(smol_angle)
            triarea = (half_side * apothem) / 2
            atotal = triarea * 2(num_of_sides)


        def central_angle_given():
            num_of_sides = int(input("How many sides does your shape have?"))
            cent_angle = float(input("What is the measure of your central angle"))
            top_angle = cent_angle / 2
            right_left_angle = 90 - top_angle

        if situation == 1:
            int_angle_given
        if situation == 2:
            side_length_given()
        if situation == 3: 
            central_angle_given()

    if function == 1:
        rectangle_area()
    if function == 2:
        circle_area()
    if function == 3:
        x_sided_shape()

if operation == 1:
    addition()
if operation == 2: 
    subtraction()
if operation == 3: 
    multiplication()
if operation == 4:
    division()
if operation == 5:
    exponent()
if operation == 6:
    area()






#GOALS: FINSIH N SIDED AREA CALCULATOR
