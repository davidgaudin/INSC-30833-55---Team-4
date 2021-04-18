'''
Program: Ideal Turf Quote Generator GUI
Developers: David Gaudin, Austin Hill, Nina Vu, Katie Mayfield, Jacob Mutscher, Jackson Coats
Date: April 20, 2021
Purpose: This Python-based application serves the purpose to enable Ideal Turf 
employees to enter all relevant information necessary to generate a turf installation 
quote for customers.

'''
from tkinter import *

def LoginValidation(): #Check employee's user name and password
    
    #dictionary for usernames and passwords
    employee_cred = {'Nvu':'purple1','Dgaudin':'tcufrogs', 'Ahill':'fortworth1234','Kmayfield':'turf55555', 'Jmutscher':'blue4242', 'Jcoats':'green1515'} #dictionary for usernames and passwords
    if username.get() not in employee_cred:
        LoginMess.set('Error. Enter a valid username')
    elif passcode.get() == employee_cred[username.get()]:
        LoginMess.set('Login')

        class QuoteGenerator:

            def __init__(self):
                window = Tk()
                window.title('Ideal Turf Quote Generator')
                window.configure(background='white')

                photo = PhotoImage(file=r'E:\School\TCU\Semester\Spring 2021\INSC-30833-Busi-Dev-Beata\Final Project\IdealTurfFinal\ITlogo.png')
            
            # Ideal Turf GUI with 10 inputs and 10 output
                Label(window, text = "Customer First Name").grid(row = 2, column = 1, sticky = W)
                Label(window, text = "Customer Last Name").grid(row = 3, column = 1, sticky = W)
                Label(window, text = "Customer Address").grid(row = 4, column = 1, sticky = W)
                Label(window, text = "City").grid(row = 5, column = 1, sticky = W)
                Label(window, text = "State").grid(row = 6, column = 1, sticky = W)
                Label(window, text = "Customer Email Address").grid(row = 7, column = 1, sticky = W)
                Label(window, text = "Square Footage").grid(row = 8, column = 1, sticky = W)
                Label(window, text = "Product Name").grid(row = 9, column = 1, sticky = W)
                Label(window, text = "Product Price").grid(row = 10, column = 1, sticky = W)
                Label(window, text = "Tax").grid(row = 11, column = 1, sticky = W)

            # Get string values
                self.firstname = StringVar()
                Entry(window, textvariable = self.firstname, justify = RIGHT).grid(row = 2, column = 2) #Customer first name
                self.lastname = StringVar()
                Entry(window, textvariable = self.lastname, justify = RIGHT).grid(row = 2, column = 2) #Customer last name
                self.address = StringVar()
                Entry(window, textvariable = self.address, justify = RIGHT).grid(row = 2, column = 2) #Customer address
                self.city = StringVar()
                Entry(window, textvariable = self.city, justify = RIGHT).grid(row = 2, column = 2) #Customer city
                self.state = StringVar()
                Entry(window, textvariable = self.state, justify = RIGHT).grid(row = 2, column = 2) #Customer state
                self.email = StringVar()
                Entry(window, textvariable = self.email, justify = RIGHT).grid(row = 2, column = 2) #Customer email
                self.productname = StringVar()
                Entry(window, textvariable = self.productname, justify = RIGHT).grid(row = 2, column = 2) #Product name
            # Get integer values
                self.squarefoot = IntVar()
                Entry(window, textvariable = self.numberOfYearsVar, justify = RIGHT).grid(row = 3, column = 2) #Sqft
                self.productprice = IntVar()
                Entry(window, textvariable = self.productprice, justify = RIGHT).grid(row = 4, column = 2) #Product Price
                self.tax = IntVar()
                Entry(window, textvariable = self.tax, justify = RIGHT).grid(row = 4, column = 2) #Tax

            #Output
                self.IdealTurfQuote = StringVar()
                Label(window, textvariable = self.IdealTurfQuote).grid(row = 5, column = 2, sticky = E)
            
            #Button to generate quote/ perform calculation
                Button(window, text = "Generate Quote", command = self.GeneratingQuote).grid(row = 7, column = 2, sticky = E)

                window.mainloop()
            
            def getOrderInfo(self, measurement, price, tax):
                OrderTotal = (measurement*price) + (measurement*price*tax)
                return OrderTotal;
            
            def GeneratingQuote(self):
                FinalQuote = self.OrderTotal(
                    float(self.squarefoot.get()),
                    float(self.productprice.get()),
                    float(self.tax.get()))

                self.IdealTurfQuote.set(format(FinalQuote, '10.2f'))
        QuoteGenerator()

#Employee Login Page
#Borrow from GUI Shopping Cart with replaced variables
Login=Tk()
Login.title("Ideal Turf Quote Generator") 
Login.configure(background='white')

logo = PhotoImage(file=r'E:\School\TCU\Semester\Spring 2021\INSC-30833-Busi-Dev-Beata\Final Project\IdealTurfFinal\ITlogo.png')

Label(Login, image=logo, background='white').grid(row=1, column=2, columnspan=3, sticky= W)
Label(Login, text='    ', background='white').grid(row=1, column=1, sticky=W)
Label(Login, text= 'Username', background='white').grid(row=2, column=2, sticky=W)
Label(Login, text= 'Password', background='white').grid(row=3, column=2, sticky=W)
Label(Login, text='    ', background='white').grid(row=4, column=4, sticky=W)

username = StringVar()
Entry(Login, textvariable = username, justify = LEFT, background='white').grid(row=2, column=3)
passcode = StringVar()
Entry(Login, textvariable = passcode, justify = LEFT, background='white', show='*').grid(row = 3, column = 3)

LoginMess= StringVar()

Label(Login, textvariable = LoginMess, background='white').grid(row = 4, column = 2, columnspan=2, sticky = S)

Button(Login, text = 'Login', command = LoginValidation).grid(row = 5, column = 2, columnspan=2)

Login.mainloop()






            
         
                
                








    
   
      
            





