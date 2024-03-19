#Yote Burger
from statistics import mode
def main():
    n = 3
    print("Welcome to Yote Burger")
    hour_11 = 0
    hour_12 = 0
    hour_1 = 0
    hour_2 = 0
    hour_3 = 0
    hour_4 = 0
    hour_5 = 0
    hour_6 = 0
    hour_7 = 0
    hour_8 = 0
    hour_9 = 0
    hour_10 = 0
    counter = 0
    clientNames = []
    day_Time = []
    totalSales = []
    allBurgers = []

    while counter < 5:
        burgerType =[]
        name = input("Hello user please input your name for the order: ")
        menu = "Hamburger(1), Cheeseburger(2), Double Cheeseburger(3), Bacon Burger(4), Impossible Burger(5)"
    
    
        totalAmount = 0
        while True:
            burgerS = int(input(f"Please choose the number of burger you would like from the menu {menu} Press 0 if you would like to complete the order: " ))
            if burgerS == 0:
                break
            elif burgerS > 5:
                print("Invalid input please try again")  
            else:
                burgerType.append(burgerS)
                allBurgers.append(burgerS)
    
        price = 2
    
    
        for i in burgerType:
            if i == 3:
                price = 3
            totalAmount += price
    
    
        print("Your order is ", burgerType, "The price is " , totalAmount)
        totalSales.append(totalAmount)
    
     
        while True:
            dayTime= int(input("Please enter the hour at which you came (11-10): "))
            if dayTime == 11:
                day_Time.append("11")
                hour_11 = hour_11 + totalAmount
                break
            elif dayTime == 12:
                day_Time.append("12")
                hour_12 = hour_12 + totalAmount
                break
            elif dayTime == 1:
                day_Time.append("1")
                hour_1 = hour_1 + totalAmount
                break
            elif dayTime == 2:
                day_Time.append("2")
                hour_2 = hour_2 + totalAmount
                break
            elif dayTime == 3:
                day_Time.append("3")
                hour_3 = hour_3 + totalAmount
                break
            elif dayTime == 4:
                day_Time.append("4")
                hour_4 = hour_4 + totalAmount
                break
            elif dayTime == 5:
                day_Time.append("5")
                hour_5 = hour_5 + totalAmount
                break
            elif dayTime == 6:
                day_Time.append("6")
                hour_6 = hour_6 + totalAmount
                break
            elif dayTime == 7:
                day_Time.append("7")
                hour_7 = hour_7 + totalAmount
                break
            elif dayTime == 8:
                day_Time.append("8")
                hour_8 = hour_8 + totalAmount
                break
            elif dayTime == 9:
                day_Time.append("9")
                hour_9 = hour_9 + totalAmount
                break
            elif dayTime == 10:
                day_Time.append("10")
                hour_10 = hour_10 + totalAmount
                break
            elif dayTime < 1 or dayTime > 12:
                print("Time is invalid please try again.")   
        
        
        
        
        clientNames.append(name)
        counter += 1
        
        
    print("Sorry we have are unable to take any more orders for today.")


    print("This was our 10th Client: " , clientNames[4])
    print(max(clientNames, key = len) , " had the longest name")
    print( "The top 3 selling burgers were ", Top_3_Burgers(allBurgers, n))
    print("Top 3 best clients:", bestThree(clientNames, totalSales))
    print("Client with second-to-last lowest bill:",secondLowest(totalSales, clientNames))
    print("Busiest Hour: ",mode(day_Time))
    print("Best Hour of day (Sales, hour)",  bestSalesHour(hour_11, hour_12, hour_1, hour_2,hour_3, hour_4, hour_5, hour_6, hour_7, hour_8, hour_9, hour_10))
    print("Total Sales of the Day:", sum(totalSales))
 


def Top_3_Burgers(allBurgers, n):
    most_common_numbers = [ ]

    for i in range(n):
        the_mode = mode(allBurgers)
        most_common_numbers.append(the_mode)

        # remove all occurrences of the most common number from the list
        allBurgers = [num for num in allBurgers if num != the_mode]

    return most_common_numbers




#Function for 3 best clients(IN PROGRESS) (+how to print)
def bestThree(bill, clientNames):
    clientBill=list(zip(bill, clientNames))
    clientBill.sort()
    top_3= [clientBill[-1],clientBill[-2],clientBill[-3]]
    return top_3




#client with 2nd to last lowest bill
def secondLowest(totalSales, clientNames):
    clientBill=list(zip(totalSales, clientNames))
    clientBill.sort()
    return clientBill [1]


#Best hour of the day
def bestSalesHour(hour_11, hour_12, hour_1, hour_2,hour_3, hour_4, hour_5, hour_6, hour_7, hour_8, hour_9, hour_10): 
    hourSales = [hour_11, hour_12, hour_1, hour_2, hour_3, hour_4, hour_5, hour_6, hour_7, hour_8, hour_9, hour_10]
    hourNames = ["11", '12', '1','2','3','4','5','6','7','8','9','10']
    corrolate = list(zip(hourSales, hourNames))
    topCorrolate = max(corrolate)
    return topCorrolate


main()
