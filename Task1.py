# Help! My code is too messy :( Please help me organise it and extract out the duplications.

# Define your reusable functions here:
import mathsfunc

# Make sure each function only does ONE thing!!!!!!!!!!!



###########################################

def weird_pythagoras():
    # get the length and width of the first triangle from the user
    opp1 = mathsfunc.side_length("first", "opposite")
    adj1 = mathsfunc.side_length("first", "adjacent")

    # work out the hyp
    hyp1 = mathsfunc.pythago(opp1, adj1)

    # get the length and width of the second triangle from the user
    opp2 = mathsfunc.side_length("second", "opposite")
    adj2 = mathsfunc.side_length("second", "adjacent")

    # work out the hyp
    hyp2 = mathsfunc.pythago(opp2, adj2)

    # create a third triangle with the hyp1 as the opp and hyp2 as the adj
    hyp3 = mathsfunc.pythago(hyp1, hyp2)
    return hyp3

def weird_sohcahtoa(trigno, nth):
    if trigno == 1:
        missing = mathsfunc.weird_soh(1, nth)
    
    if trigno == 2:
        missing = mathsfunc.weird_soh(2, nth)
    
    if trigno == 3:
        missing = mathsfunc.weird_cah(1, nth)
    
    if trigno == 4:
        missing = mathsfunc.weird_cah(2, nth)
    
    if trigno == 5:
        missing = mathsfunc.weird_toa(1, nth)
    
    if trigno == 6:
        missing = mathsfunc.weird_toa(2, nth)
    
    return missing

def weird_sine(nth):
    side_a = mathsfunc.side_length(nth, "first")
    angle_A = mathsfunc.angle_size(nth)
    angle_B = mathsfunc.angle_size(nth)
    missing = mathsfunc.sine_side(side_a, angle_A, angle_B)
    return missing

def weird_cosine(nth):
    side_b = mathsfunc.side_length(nth, "first")
    side_c = mathsfunc.side_length(nth, "second")
    angle_A = mathsfunc.angle_size(nth)
    missing = mathsfunc.cosine_side(side_b, side_c, angle_A)
    return missing


method = 999
sub_method = 999
while method < 1 or method > 4:
    method = int(input("Which method would you like to use to solve your triangle?\n1. Pythagoras' theorem\n2. SOHCAHTOA\n3. The Sine rule\n4. The Cosine rule\n"))
    mathsfunc.invalid_response(method, 1, 4)
if method == 1:
    weird_answer = weird_pythagoras()
    print(f"The answer is {weird_answer}.")

elif method == 2:
    while sub_method < 1 or sub_method > 6:
        sub_method = int(input("1. Find opposite with SOH\n2. Find hypotenuse with SOH\n3. Find adjacent with CAH\n4. Find hypotenuse with CAH\n5. Find opposite with TOA\n6. Find adjacent with TOA\n"))
        mathsfunc.invalid_response(method, 1, 6)
    side_1 = weird_sohcahtoa(sub_method, "first")
    while sub_method < 1 or sub_method > 6:
        sub_method = int(input("1. Find opposite with SOH\n2. Find hypotenuse with SOH\n3. Find adjacent with CAH\n4. Find hypotenuse with CAH\n5. Find opposite with TOA\n6. Find adjacent with TOA\n"))
        mathsfunc.invalid_response(method, 1, 6)
    side_2 = weird_sohcahtoa(sub_method, "second")
    weird_answer = mathsfunc.pythago(side_1, side_2)
    print(f"The answer is {weird_answer}.")

elif method == 3:
    side_1 = weird_sine("first")
    side_2 = weird_sine("second")
    weird_answer = mathsfunc.pythago(side_1, side_2)
    print(f"The answer is {weird_answer}.")

elif method == 4:
    side_1 = weird_cosine("first")
    side_2 = weird_cosine("second")
    weird_answer = mathsfunc.pythago(side_1, side_2)
    print(f"The answer is {weird_answer}.")

# After you have written the reusable functions, answer the following:

# Questions:
# 1. What are the preconditions for your code not to break?
# The inputs must be numbers in order to perform the division subroutines.

# 2. Validate the user's input based on your preconditions.
# Done

# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
# As I was extending the code for the side length calculation, using reusable components greatly simplify my code, which, without them, would require me to re-type the same extended block of code numerous times, and making my code more difficult to read and debug. In addition, as I have saved my subroutines in a separate file, I can reuse them in multiple programs without having to type them out again, simplifying writing code even further.

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# Done

# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
# Done

# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
# 

# 4. Make sure all of your functions (except the main one) only do ONE thing or process.
#

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle.