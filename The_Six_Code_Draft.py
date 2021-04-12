'''
Program: Ideal Turf Quote Generator
Developers: David Gaudin, Austin Hill, Nina Vu, Katie Mayfield, Jacob Mutscher, Jackson Coats
Date: April 20, 2021
Purpose: This Python-based application serves the purpose to enable Ideal Turf 
employees to enter all relevant information necessary to generate a turf installation 
quote for customers.
'''
print('\n-------------Employee Log In-------------\n') #start employee login page

employee_credentials = {'Dgaudin', 'Ahill', 'Nvu', 'Kmayfield', 'Jmutscher', 'Jcoats'} #dictionary for usernames and passwords

Dgaudin = {
    'tcufrogs'
}

Ahill = {
    'fortworth1234'

}

Nvu = {
    'purple1'

}

Kmayfield = {
    'turf55555'

}

Jmutscher = {
    'blue4242'

}

Jcoats = {
    'green1515'

}

employee_username = input('Employee Username:') #prompt employee for username
while employee_username not in employee_credentials: #if username is invalid, employee will re-enter username
    employee_username = input('\nError. Enter a valid username:')

if employee_username == 'Dgaudin': 
    employee_password = input('\nEmployee Password:') #if username is Dgaudin, employee will enter password
    while employee_password != 'tcufrogs': #if password is invalid for Dgaudin, employee will re-enter password
        employee_password = input('\nError. Enter a valid password:')

if employee_username == 'Ahill':
    employee_password = input('\nEmployee Password:') #if username is Ahill, employee will enter password
    while employee_password != 'fortworth1234': #if password is invalid for Ahill, employee will re-enter password
        employee_password = input('\nError. Enter a valid password:')

if employee_username == 'Nvu': 
    employee_password = input('\nEmployee Password:') #if username is Nvu, employee will enter password
    while employee_password != 'purple1': #if password is invalid for Nvu, employee will re-enter password
        employee_password = input('\nError. Enter a valid password:')

if employee_username == 'Kmayfield':
    employee_password = input('\nEmployee Password:') #if username is Kmayfield, employee will enter password
    while employee_password != 'turf55555': #if password is invalid for Kmayfield, employee will re-enter password
        employee_password = input('\nError. Enter a valid password:')

if employee_username == 'Jmutscher':
    employee_password = input('\nEmployee Password:') #if username is Jmutscher, employee will enter password
    while employee_password != 'blue4242': #if password is invalid for Jmutscher, employee will re-enter password
        employee_password = input('\nError. Enter a valid password:')

if employee_username == 'Jcoats':
    employee_password = input('\nEmployee Password:') #if username is Jcoats, employee will enter password
    while employee_password != 'green1515': #if password is invalid for Jcoats, employee will re-enter password
        employee_password = input('\nError. Enter a valid password:')

print('\n-------------Customer Information-------------\n') #start customer information page

customer_fname = input('\nCustomer First Name:') #prompt employee for the customer's first name
for char in customer_fname:
    if not char.isalpha(): #if the customer's first name is not containing only alphabetic, employee will re-enter customer's first name
        customer_fname = input('\nError. Input must contain alphabetic letters only. Enter a valid last name:')

customer_lname = input('\nCustomer Last Name:') #prompt employee for the customer's last name
for char in customer_lname:
    if not char.isalpha(): #if the customer's last name is not containing only alphabetic, employee will re-enter customer's last name
        customer_lname = input('\nError. Input must contain alphabetic letters only. Enter a valid last name:')

customer_phone = input('\nCustomer Phone Number') #prompt employee for the customer's phone number
for char in customer_phone:
    if not char.isnumeric():  #if the customer's phone number does not contain only numbers, employee will re-enter customer phone number
        customer_phone = input('\nError. Input must contain only numbers. Enter a valid phone number')
while len(customer_phone) != 10: #if the customer's phone number != 10 digits, employee will re-enter customer phone number
    customer_phone = input('Error. Phone Number must be 10 digits long and contain only numbers. Enter a valid phone number')

customer_email = str(input('\nCustomer Email:')) #prompt employee for the customer's email
while '@' not in customer_email: #if the customer's email does not contain the '@' symbol, employee will re-enter customer email
    customer_email = str(input('\nError. Enter valid email address:'))

customer_address_line1 = input('\nCustomer Address, Line 1:') #prompt employee for first line of customer's address

customer_address_line2 = input('\nCustomer Address, Line 2 (enter "n/a" if not needed):') #prompt employee for second line of customer's address

customer_address_city = input('\nCustomer Address, City:') #prompt employee for customer's city
for char in customer_address_city:
    if not char.isalpha(): #if the customer's city is not containing only alphabetic, employee will re-enter customer's city
        customer_address_city = input('\nError. Input must contain alphabetic letters only. Enter a valid city:')

customer_address_state = input('\nCustomer Address, State:') #prompt employee for customer's state
for char in customer_address_state:
    if not char.isalpha(): #if the customer's state is not containing only alphabetic, employee will re-enter customer's state
        customer_address_state = input('\nError. Input must contain alphabetic letters only. Enter a valid state:')

print('\n-------------Quote Generator-------------\n') #start customer information page

total_area = int(input('\nTotal Area (Square Feet):')) #prompt employee for total area of the project
for char in total_area:
    if not char.isnumeric():  #if the total area is not numeric, employee will re-enter total area
        total_area = int(input('\nError. Input must contain only numbers Total Area (Square Feet):'))





















