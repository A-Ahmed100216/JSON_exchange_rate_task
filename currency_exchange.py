# Import the relevant libraries in this case, json
import json

# Access the json file containing the exchange rates
# Use the as keyword to alias the file for easier access.
with open("exchange_rates.json") as jsonrates:
    # Use the load method to copy the data in the json file and store as a variable.
    exchange_rates=json.load(jsonrates)
    # Print the variable to view the contents of the json file.
    print(exchange_rates)
    # Create a for loop to iterate through the nested dictionary, 'rates'
    for x,y in exchange_rates['rates'].items():
        # Print the items i.e. they key value pair, as a formatted string.
        print("{}: {}".format(x,y))
