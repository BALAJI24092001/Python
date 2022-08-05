i = int(input())
quarters = 0;
dimes = 0;
nickles = 0;
pennies = 0;

# " // " is quotent operator

if(i/25 > 0): # quarter = 25
    quarters = i // 25;
    i = i - quarters*25;

if(i/10 > 0): # dime = 10
    dimes = i // 10;
    i = i - dimes*10;

if(i/5 > 0): # nickle = 5
    nickles = i // 5;
    i = i - nickles*5;

if(i != 0 and i > 0): # penny = 1
    pennies = i;
    i = i - pennies;

# customize printing
if(i == 0):
    print("quarters : " , quarters)
    print("dimes : " , dimes)
    print("nickles : " , nickles)
    print("pennies : " , pennies)
