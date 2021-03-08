# Slice
# Pizzabot Code Challenge for Slice

SOLUTION ALGORITM:
- Start at position 0,0 and move along a horizontal axis ("EAST"). Record each move in the route list.
- Keep track of the bot's current location, check each horizontal axis if there are deliveries along that axis
- If there are deliveries, determine a direction("NORTH" or "SOUTH") to the nearest delivery location. 
- When delivery location is reached, record the delivery in the route list.
- When all deliveries in that direction are done, reverse the direction. 
- Upon each delivery, remove the order from the order list.
- When all deliveries are done (the order list is empty), end the process.

SOLUTION STRUCTURE (PYTHON):
- Class Pizzabot in the file pizzabot.py has __init__ constructor to intialize an instance of a bot, and runPizzabot method
- File testpizzabot.py has 4 test cases to test various scenarioes:
	- Test Case 1 - The challenge example case
	- Test Case 2 - Added a test case to test a scenario when not all axies have deliveries
	- Test Case 3 - Added a test case to test a scenario when there is only one delivery order
	- Test Case 4 - Added a test case to test a scenario when attempting to run the pizzabot but there are no orders
- Each test case result is checked with "assert" method. The result is either "OK" or "Failed"

INSTALLATION AND RUNNING INSTRUCTION:
- Copy pizzabot.py to the current working directory
- Copy testpizzabot.py to the current working directory
- Execute testpizzabot.py
- Evaluate the result on stdout
