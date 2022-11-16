# Control Structures Task - Program task 16.11.2022

# User inputs
customer_name = input("Enter your name: ")
customer_address = input("Enter your address: ")
customer_phone_number = int(input("Enter your phone number: "))

width_of_lawn = int(input("Enter lawn width: "))
length_of_lawn = int(input("Enter lawn length: "))
quality_of_lawn = input("Enter lawn care product: ")

# Default cost per square meter is 0
cost_per_square_metre = 0

# Validation of width and length input
if width_of_lawn >= 2 and width_of_lawn <= 30:

    if length_of_lawn >= 2 and length_of_lawn <= 50:
        # Cost per square metre is different depending on what lawn care product is selected by the user
        if quality_of_lawn.lower() == "luxury":
            cost_per_square_metre = 1.15
        elif quality_of_lawn.lower() == "standard":
            cost_per_square_metre = 0.80
        elif quality_of_lawn.lower() == "economy":
            cost_per_square_metre = 0.45

# Variables for calculating costs
calculation_of_labour = width_of_lawn * length_of_lawn
round(calculation_of_labour, 2)
cost_of_labour = calculation_of_labour * cost_per_square_metre
lawn_care_calculation = cost_per_square_metre * calculation_of_labour
total_cost = cost_of_labour + lawn_care_calculation
vat = total_cost * 0.2
vat = vat + total_cost

# Output including cost calculation and customer information
print(f'\nTotal cost: £{total_cost}')
print(f'Quality of lawn: {quality_of_lawn}')
print(f'Customer name: {customer_name}')
print(f'Customer address: {customer_address}')
print(f'Customer phone number: {customer_phone_number}')
print(f'Calculation of labour: {width_of_lawn} * {length_of_lawn} = {calculation_of_labour}')
print(f'Cost of labour: {calculation_of_labour} * {cost_per_square_metre} = {cost_of_labour}')
print(f'Lawn care calculation: {cost_per_square_metre} + {calculation_of_labour} = {lawn_care_calculation}')
print(f'Total cost: £{total_cost}')
print(f'Total cost + VAT: £{vat}')
