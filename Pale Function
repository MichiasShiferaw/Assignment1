def pale(n):
    n_string = str(n)   #convert the provided number into a string
    fourdigits = len(n_string) == 4  # with the string version of the input, determine if the value indeed has 4 digits
    rem = n % 10  #use modulo to place the last digit into a another formula
    divisble = rem % 4 == 0 and rem != 0  #determine if the last digit of the input is divisble by 4 and not 0.
    n = int(n / 10)
    rem1 = n % 10
    n = int(n / 10)
    rem2 = n % 10
    n = int(n / 10)
    rem3 = n % 10
    n = int(n / 10)
    rem4 = n % 10 # repeatedly separete reach four digits one by one
    threethree = (rem and rem1) or (rem1 and rem2) or (rem2 and rem4) or (rem3 and rem4) == 3  #verfify if any consecutive digits each equal to 3
    pale_verficiation = (threethree != divisble == fourdigits) or (fourdigits == threethree != divisble)  #determine if the results will equal to a pale or not
    return pale_verficiation   #output the determination
