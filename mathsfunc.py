import math

def side_length(nth, side_type):
    side = ""
    side_check = False
    while side_check != True:
        side = input("Enter your " + nth + " triangle's " + side_type + " side length.\n")
        try:
            side = float(side)
            side_check = True
        except ValueError:
            print("Error: input not valid. Try again.")
    return float(side)

def angle_size(nth):
    angle = ""
    angle_check = False
    while angle_check != True:
        angle = input("Enter the size of your " + nth + " triangle's angle.\n")
        try:
            angle = float(angle)
            angle_check = True
        except ValueError:
            print("Error: input not valid. Try again.")
    return float(angle)

# Pythagoras
def pythago(opp, adj):
    hyp = math.sqrt(opp**2 + adj**2)
    return hyp

# SOH
def soh_opposite(hyp, angle):
    opp = hyp * math.sin(math.radians(angle))
    return opp

def soh_hypotenuse(opp, angle):
    hyp = opp / math.sin(math.radians(angle))
    return hyp

# CAH
def cah_adjacent(hyp, angle):
    adj = hyp * math.cos(math.radians(angle))
    return adj

def cah_hypotenuse(adj, angle):
    hyp = adj / math.cos(math.radians(angle))
    return hyp

# TOA
def toa_opposite(adj, angle):
    opp = adj * math.tan(math.radians(angle))
    return opp

def toa_adjacent(opp, angle):
    adj = opp / math.tan(math.radians(angle))
    return adj

# Sine rule
def sine_side(side_a, angle_A, angle_B):
    side_b = math.sin(math.radians(angle_B)) * (side_a / math.sin(math.radians(angle_A)))
    return side_b

def sine_angle(side_a, angle_A, side_b):
    angle_B = side_b * (math.sin(math.radians(angle_A)) / side_a)
    return angle_B

# Cosine rule
def cosine_side(side_b, side_c, angle_A):
    side_a = math.sqrt((side_b ** 2) + (side_c ** 2) - (2 * side_b * side_c * math.cos(math.radians(angle_A))))
    return side_a

def cosine_angle(side_b, side_c, side_a):
    angle_A = math.degrees(math.acos(((side_b ** 2) + (side_c ** 2) - (side_a **2))/(2 * side_b * side_c)))
    return angle_A

# Invalid response
def invalid_response (var, min, max):
    if var < min or var > max:
        print("Invalid. Try again.")

# Weird sohcahtoa
def weird_soh(type, nth):
    if type == 1:
        side = side_length(nth, "hypotenuse")
        angle = angle_size(nth)

        side2 = soh_opposite(side, angle)
    
    elif type == 2:
        side = side_length(nth, "opposite")
        angle = angle_size(nth)

        side2 = soh_hypotenuse(side, angle)

    return side2


def weird_cah(type, nth):
    if type == 1:
        side = side_length(nth, "hypotenuse")
        angle = angle_size(nth)

        side2 = cah_adjacent(side, angle)
    
    elif type == 2:
        side = side_length(nth, "adjacent")
        angle = angle_size(nth)

        side2 = cah_hypotenuse(side, angle)

    return side2


def weird_toa(type, nth):
    if type == 1:
        side = side_length(nth, "adjacent")
        angle = angle_size(nth)

        side2 = toa_opposite(side, angle)
    
    elif type == 2:
        side = side_length(nth, "opposite")
        angle = angle_size(nth)

        side2 = toa_adjacent(side, angle)

    return side2

#print(math.sin(math.radians(30)))
#print(math.degrees(math.asin(1/2)))