#this will be a compound interest calculator

def comp_int_calc():
    starting_amount = int(input('What is the starting amount?: '))
    #contributing_amount = int(input('What is the amount you will be contributing monthly?: '))
    #contributing_timeframe = int(input('What is the '))
    #length_of_time = int(input('What is the length of time you would like to model?: '))
    interest_rate_per_year = int(input('What is the interest rate per year?: '))
    interest_multiplier = (interest_rate_per_year/100)+1
    x = starting_amount
    i=0
    while x < (starting_amount*2):
        x = round(x*interest_multiplier)
        i = i+1
        print('after ', i ,' years the amount is' , x)


comp_int_calc()


