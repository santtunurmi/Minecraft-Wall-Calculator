def wallCalculator():
    #input your wall's total lenght (including pillars) as an integer
    while True:
        try:
            total_lenght = int(input("Input the lenght of the wall you are trying to build, here as an integer: "))
            break
        except:
            print("You did not input your time as an integer")
            continue
    #the programm establishes 2 pillars on either end and a single wall-segment in-between as the minimum number of segments necessary in order to constitute as a succesfull wall
    pillars = 2
    walls = 1
    #the program goes through all possible options for amount of pillars, wall segments and the block lenghts of the wall segments
    print("List of lengths that you can build your wall segments with to achieve and even distribution:")
    solutions = 0
    try:
        while pillars < total_lenght:
            wall_lenght = 0
            while pillars + wall_lenght + walls <= total_lenght:
                wall_lenght += 1
                #in the case that the amount of wall segments are just long enough to be fit evenly on the wall the program will print out the lenghts that you can build all of your wall segments with to achieve an even distribution
                if pillars + (wall_lenght * walls) == total_lenght and walls != 1 and wall_lenght != 1:
                    print("     Wall lenght:", wall_lenght)
                    solutions += 1
            walls += 1
            pillars += 1
        if solutions == 0:
            print("There were no possible solutions for the wall lenght you inputted. Try another wall lenght and run the program again!")
    except:
        print("Something went wrong with the programm. Please try again!")

while True:
    wallCalculator()