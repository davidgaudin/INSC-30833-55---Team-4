
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
    
    #Dictionary for Ideal Turf's employees
    employee_cred = {'Nvu':'purple1','Dgaudin':'tcufrogs', 'Ahill':'fortworth1234','Kmayfield':'turf55555', 'Jmutscher':'blue4242', 'Jcoats':'green1515'}
    if username.get() not in employee_cred:
        LoginMess.set('Error. Enter a valid username')
    elif passcode.get() != employee_cred[username.get()]:
        LoginMess.set('Error. Enter a valid password')
    elif passcode.get() == employee_cred[username.get()]:
        LoginMess.set('Login successful')

        class QuoteGenerator:

            #def FinalMessage(self):
            #    EmailAddress = self.email.get()

            #    self.IdealTurfQuote = StringVar()
            #    #FinalQuote = self.IdealTurfQuote.get()
            #    self.Message.set("Final Quote of " + self.IdealTurfQuote + " was sent to " + EmailAddress)
            
            def __init__(self):
                form = Toplevel() #To overwrite Tk as the second window popup
                form.title('Ideal Turf Quote Generator')
                form.configure(background='white')
                
                photo = PhotoImage(file=r"C:\Users\19722\Downloads\ITlogo.PNG")
                Label(form, image = photo).grid(row = 1, column = 1, columnspan=3, sticky = W) # Display image on the quote generator form
                
                # Create and display fields that need to be filled out on the form 
                Label(form, text = "Customer First Name").grid(row = 2, column = 1, sticky = W)
                Label(form, text = "Customer Last Name").grid(row = 3, column = 1, sticky = W)
                Label(form, text = "Customer Address").grid(row = 4, column = 1, sticky = W)
                Label(form, text = "City").grid(row = 5, column = 1, sticky = W)
                Label(form, text = "State").grid(row = 6, column = 1, sticky = W)
                Label(form, text = "Customer Email Address").grid(row = 7, column = 1, sticky = W)
                Label(form, text = "Product Name").grid(row = 8, column = 1, sticky = W)
                Label(form, text = "Square Footage").grid(row = 9, column = 1, sticky = W)
                Label(form, text = "Product Price").grid(row = 10, column = 1, sticky = W)
                Label(form, text = "Tax").grid(row = 11, column = 1, sticky = W)

                # Get string values when employee entering in customer information
                self.firstname = StringVar()
                Entry(form, textvariable = self.firstname, justify = RIGHT).grid(row = 2, column = 3) #Customer first name
                self.lastname = StringVar()
                Entry(form, textvariable = self.lastname, justify = RIGHT).grid(row = 3, column = 3) #Customer last name
                self.address = StringVar()
                Entry(form, textvariable = self.address, justify = RIGHT).grid(row = 4, column = 3) #Customer address
                self.city = StringVar()
                Entry(form, textvariable = self.city, justify = RIGHT).grid(row = 5, column = 3) #Customer city
                self.state = StringVar()
                Entry(form, textvariable = self.state, justify = RIGHT).grid(row = 6, column = 3) #Customer state
                self.email = StringVar()
                Entry(form, textvariable = self.email, justify = RIGHT).grid(row = 7, column = 3) #Customer email
                self.productname = StringVar()
                Entry(form, textvariable = self.productname, justify = RIGHT).grid(row = 8, column = 3) #Product name

                # Get float values when employee entering in measurement, product, and price information
                self.squarefoot = DoubleVar()
                Entry(form, textvariable = self.squarefoot, justify = RIGHT).grid(row = 9, column = 3) #Sqft
                self.productprice = DoubleVar()
                Entry(form, textvariable = self.productprice, justify = RIGHT).grid(row = 10, column = 3) #Product Price
                self.tax = DoubleVar()
                Entry(form, textvariable = self.tax, justify = RIGHT).grid(row = 11, column = 3) #Tax

                #Output Final Quote
                self.MessageShow = StringVar()
                self.SendtoCustomer = StringVar()
                
                # Create buttons to generate quote/ perform calculation
                Button(form, text = 'Generate Quote', command = self.DataValidation).grid(row = 12, column = 2)

                form.mainloop()

            def ShowQuote(self):
                OrderTotal = (1 + self.tax.get()/100) * self.squarefoot.get() * self.productprice.get() #Calculation
                self.MessageShow.set("Final quote (in USD): " + str(format(OrderTotal,"10.2f")))

            def DataValidation(self): # First verify that there is input for all of the variables, then verify that the numerical values are valid
                if len(self.firstname.get()) > 0 and len(self.lastname.get()) > 0 and len(self.city.get()) > 0 and len(self.address.get()) > 0 and len(self.state.get()) > 0 and len(self.email.get()) > 0 and len(self.productname.get()) > 0:
                    if self.squarefoot.get() > 0 and self.productprice.get() > 0 and self.tax.get() >=0:
                        self.GeneratingQuote()
                    else:
                        self.ErrorMessage()
                else:
                    self.ErrorMessage()
       
                

            def ErrorMessage(self):
                errorwindow = Toplevel()
                errorwindow.title("Negative Value")
                errorwindow.configure(background="white")

                photo4 = PhotoImage(file=r"C:\Users\19722\Downloads\ITlogo.PNG")
                Label(errorwindow, image = photo4).grid(row = 1, sticky = W)

                Label(errorwindow, text="Please verify all fields are complete and correct").grid(row = 2)

                def CloseWindow():
                    errorwindow.destroy()

                Button(errorwindow, text = 'Close', command = CloseWindow).grid(row = 3)

                

                errorwindow.mainloop()
                
            
            def GeneratingQuote(self): # Create another window that output info from the form
                show = Toplevel()
                show.title("Final Quote")
                show.configure(background='white')
                
                photo1 = PhotoImage(file=r"C:\Users\19722\Downloads\ITlogo.PNG")
                Label(show, image = photo1).grid(row = 1, column = 1, sticky = W)

                MessageShow = self.ShowQuote()
                Label(show, textvariable = self.MessageShow).grid(row = 2, column = 1, sticky = W)
                Button(show, text = 'Send Email', command = self.EmailMessage).grid(row = 3, column = 1)

                show.mainloop()
            

            def EmailCustomer(self): # Email to customer
                EmailAddress = self.email.get() 
                self.SendtoCustomer.set('Quote was emailed to ' + EmailAddress)

            def EmailMessage(self):
                ewindow = Toplevel()
                ewindow.title("Email Sent")
                ewindow.configure(background='white')
                
                photo2 = PhotoImage(file=r"C:\Users\19722\Downloads\ITlogo.PNG")
                Label(ewindow, image = photo2).grid(row = 1, column = 1, sticky = W)

                SendtoCustomer = self.EmailCustomer()
                Label(ewindow, textvariable = self.SendtoCustomer).grid(row = 2, column = 1, sticky = W)
                Button(ewindow, text = 'Close', command = self.LoggingOff).grid(row = 3, column = 1)

                ewindow.mainloop()

            def LoggingOff(self): #Logging off function
                Login.destroy()
                

            
        QuoteGenerator()

#Employee Login Page
 
Login = Tk()
Login.title("Ideal Turf Quote Generator") 
Login.configure(background='white')

logo = PhotoImage(file=r'C:\Users\19722\Downloads\ITlogo.PNG')
Label(Login, image=logo, background='white').grid(row=1, column=2, columnspan=3, sticky= W) #Display image on login form

#Display username and password field
Label(Login, text= 'Employee Username', background='white').grid(row=2, column=2, sticky=W) 
Label(Login, text= 'Password', background='white').grid(row=3, column=2, sticky=W)

username = StringVar()
Entry(Login, textvariable = username, justify = LEFT, background='white').grid(row=2, column=3)
passcode = StringVar()
Entry(Login, textvariable = passcode, justify = LEFT, background='white', show='*').grid(row = 3, column = 3)

#Display login message
LoginMess= StringVar()
Label(Login, textvariable = LoginMess, background='white').grid(row = 4, column = 2, columnspan=2, sticky = S)

#Button on login form
Button(Login, text = 'Login', command = LoginValidation).grid(row = 5, column = 2, columnspan=2)

Login.mainloop()
