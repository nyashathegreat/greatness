#A vending machine that allows the customer to enter their money and select an item they want to purchase and returns the product purchased so is the change.

def vendingMachine():
    print("Dear Customer, You are so welcome!")
    print ("Please find pleasure whilist you shop with us & remember to follow the instructions below")
    print("")
    count = 0
    totalCredit  = 0
    
    #user inputs credit
    coinNum = int(input( "How many coins would you like to enter: "))
    while count in range (coinNum):
        coin = float(input( "Enter coin amount in R: "))
        totalCredit+= coin
        count += 1
    print("You have R{0} in your bank.".format(round(totalCredit,2)))
    print("")
    
     #user purchases product
    print("Please choose your item: ")
    print("")
    print("1.Ice Tea ")
    print("2.Fresh Juice")
    print("3.Coca-Cola")
    print("4.Water")
    print("5.Redbull")
    print("")

    finalCredit = totalCredit
    round (finalCredit,2)
    
    #transaction in process. Returns change and product purchased.
    item = int (input("Please enter the number of the item you want to purchase: "))
    while item < item :
        print("Your requested item is not available")
        item = int (input(" Enter the number of your items: "))
    if item == 1:
        finalCredit = totalCredit - 0.59
        print("You have purchased a an Ice Tea Peach, costing 0.59 rands")
        print("You have {0} remaining in your bank.".format(round(finalCredit,2)))
    elif item == 2:
        finalCredit  = totalCredit - 0.75
        print("You have purchased Fresh Juice, costing 0.75 rands")
        print("You have {0} remaining in your bank.".format(round(finalCredit,2)))
    elif item == 3:
        finalCredit  = totalCredit - 0.99
        print("You have purchased a Coca-Cola can, costing 0.99 rands")
        print("You have {0} remaining in your bank.".format(round(finalCredit,2)))
    elif item == 4:
        finalCredit  = totalCredit - 0.82
        print("You have purchased a bottle of water, costing 0.82 rands")
        print("You have {0} remaining in your bank.".format(round(finalCredit,2)))
    elif item == 5:
        finalCredit  = totalCredit - 1.09
        print("You have purchased a Coca-Cola, costing 1.09 rands")
        print("You have {0} remaining in your bank.".format(round(finalCredit,2)))
    else:
        print("Transaction not permmisible")
        print("")
        print("The rest of your money R{0}, has been outputted.".format(round(finalCredit,2)))

vendingMachine()
    
    
        
    
