def min_CAD_coins(price, payment):
    # Determine quantity of coin change that needs to be given
    #Just a creative way of doing it
    #my personal interpretation of greedy algorithm
    money_till = []  #declare an array
    toonie_val, loonie_val, quart_val, dime_val, nckel_val = 0,0,0,0,0  #Declare all demonination of coins


    change = cad_cashier(price, payment) #call for the cad_cashier() to determine the change
    # my personal interpretation of greedy algorithm
    #if the change val can be divisble by any denominat. of a coin it will circulate in respective while loop
    # until the condition is not valid
    while change >= 2.00:
        toonie_val = toonie_val + 1
        change = change - 2.00
    while change >= 1.00:
        loonie_val = loonie_val + 1
        change = change - 1.00
    while change >= .25:
        quart_val = quart_val + 1
        change = change - .25
    while change >= .10:
        dime_val = dime_val + 1
        change = change - .10
    while change >= .05:
        nckel_val = nckel_val + 1
        change = change - .05
    money_till = (toonie_val, loonie_val, quart_val, dime_val, nckel_val)
    return money_till  #return output
