import botfunc
import requests
from pyfiglet import Figlet
import os, time

# Help! I'm trying to make this cool bot but my code is too messy :( Please help me organise it into reusable components.

# Define your reusable functions here:
# Make sure each function only does ONE thing!!!!!!!!!!!

###########################################

def weird_weather_bot():
    
    f = Figlet(font="slant")
    print(f.renderText("HEY!"))

    print("Welcome to the weird weather bot :)")
    print("-----------------------------------\n")
    name = ""
    while len(name) <= 0:
        name = input("May I take your first name please?")
        if not name.isalpha():
            name = ""
            print("Name invalid. Try again.")
    gender_result = botfunc.guess_gender(name)
    gender = gender_result[0]
    prob_percent = gender_result[1]
    print(f"\nHmmm, I'm {prob_percent}% sure you are a {gender}.")
    
    gender_correct = input("Am I right? :) (Y/n)")
    if gender_correct.lower() in ["", "yes", "y", "ye"]:
        print("Wooooooh! Computer 1, Human 0.")
    else:
        print("Ahhhh, sorry! :(")

    postcode_raw = input("\nSo, what's your postcode? ")
    postcode_result = botfunc.postcode_fetcher(postcode_raw)
    area = postcode_result[0]
    longitude = postcode_result[1]
    latitude = postcode_result[2]
    print(f"Nice! so you live in {area}.\n")

    print("Let me just check the weather there today...\n")
    
    for i in range(3):
        time.sleep(1)
        print("...")
    
    input("\nWould you like a cat fact while you wait? ")
    print("Doesn't matter what you think, I'm going to give you one anyway :)")
    time.sleep(3)
    joke = botfunc.cat_facts()
    print("\n###########################")
    print("CAT FACT:")
    print(f"\n{joke}\n")
    print("So interesting isn't it!")
    print("###########################")

    print("\nWaiting 5 seconds for you to read the fact...")
    time.sleep(5)
    print("\nNow, back to getting the weather...")

    for i in range(3):
        time.sleep(1)
        print("...")

    weather_result = botfunc.weather_fetcher(latitude, longitude)
    weather_degrees = weather_result[0]
    main_weather_desc = weather_result[1]
    second_weather_desc = weather_result[2]
    print(f"\nThe weather in {area}:\n")
    print(str(weather_degrees) + "℃")
    print(f"{main_weather_desc} - {second_weather_desc}")
    print("\nThank you! Bye.")

weird_weather_bot()


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
# The name and postcode must be included in the respective databases.

# 2. Validate the user's input based on your preconditions.
#

# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
# It served as a way to greatly simplify the code, making it easier to read and debug the bot. In addition, there is now potential to reuse these functions within the bot without needing to re-write the functions.


# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# Done

# 2. Make sure all of your functions (except the main one) only do ONE thing or process.
# Done

# 3. Add your own twist to the code.
#

# Extension:
# Add the following apis as reusable components and use them in your code:
# https://www.exchangerate-api.com/docs/overview
