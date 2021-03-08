import re
import pizzabot

def main():

    print (50*'*')
    print ("Pizzabot delivers for you!")
    print (' ')

# Testcase 1 Moving horizontal, each axis have at least one delivery

    testCase1 = '5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)'
    myPizzabot1 = pizzabot.Pizzabot(testCase1)
    myPizzabot1.runPizzabot()
    print (50*'-')
    print ('Test Case 1 - Each axis delivery')
    print ('Pizzabot Delivery Orders - ' , testCase1)
    print ('Pizzabot Delivery Route  - ' , myPizzabot1.getRoute())
    try:
        assert myPizzabot1.getRoute() == 'DNDENNDEDESDESDNDDNND'
        print ('Test Case 1 - OK')
    except:
        print ('Test Case 1 - Failed')
    print (' ')

# Testcase 2 Moving horizontal, some axis have at least one delivery but some have none

    testCase2 = '5x5 (0, 0) (4, 4) (4, 2) (4, 2) (0, 1) (2, 3) (4, 1)'
    myPizzabot2 = pizzabot.Pizzabot(testCase2)
    myPizzabot2.runPizzabot()
    print (50*'-')
    print ('Test Case 2 - Some axises delivery')
    print ('Pizzabot Delivery Orders - ' , testCase2)
    print ('Pizzabot Delivery Route  - ' , myPizzabot2.getRoute())
    try:
        assert myPizzabot2.getRoute() == 'DNDEENNDEESSDNDDNND'
        print ('Test Case 2 - OK')
    except:
        print ('Test Case 2 - Failed')
    print (' ')

# Testcase 3 Delivery area is not a square, and only one delivery

    testCase3 = '15x40 (3, 3)'
    myPizzabot3 = pizzabot.Pizzabot(testCase3)
    myPizzabot3.runPizzabot()
    print (50*'-')
    print ('Test Case 3 - Single delivery')
    print ('Pizzabot Delivery Orders - ' , testCase3)
    print ('Pizzabot Delivery Route  - ', myPizzabot3.getRoute())
    try:
        assert myPizzabot3.getRoute() == 'EEENNND'
        print ('Test Case 3 - OK')
    except:
        print ('Test Case 3 - Failed')
    print (' ')

# Testcase 4 Attempt to launch a pizzabot with no delivery orders

    testCase4 = '15x4'
    myPizzabot4 = pizzabot.Pizzabot(testCase4)
    myPizzabot4.runPizzabot()
    print (50*'-')
    print ('Test Case 4 - No orders')
    print ('Pizzabot Delivery Orders - ' , testCase4)
    print ('Pizzabot Delivery Route  - ', myPizzabot4.getRoute())
    try:
        assert myPizzabot4.getRoute() == ''
        print ('Test Case 4 - OK')
    except:
        print ('Test Case 4 - Failed')
    print (' ')

    print ("Thank you for your order - please come again!")
    print (50*'*')

if __name__ == '__main__':

    main()
