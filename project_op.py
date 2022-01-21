# Part 1
# 1. Import tkinter module
# 2. Creating class
# 3. Creating the constructor
# 4. Create application window
# 5. Create title for the app window
# 6. Set bg color for app window.
# 7. Add labels for input feild.
from tkinter import *

class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("loan Calculator")
        window.configure(background='red')

        Label(window,font='Helvetica 20 bold',bg='light green',text='Annual Interest Rate').grid(row=1,column=1,sticky=W)
        Label(window, font='Helvetica 20 bold', bg='light green', text='Number of Years').grid(row=2, column=1, sticky=W)
        Label(window, font='Helvetica 20 bold', bg='light green', text='Loan Amount').grid(row=3, column=1, sticky=W)
        Label(window, font='Helvetica 20 bold', bg='light green', text='Monthly Payment').grid(row=4, column=1, sticky=W)
        Label(window, font='Helvetica 20 bold', bg='light green', text='Total Payment').grid(row=5, column=1, sticky=W)


# part 2
# Add label widgets
# Create objects to take user input & display values.

        self.AnnualRateInterestVar=StringVar()
        Entry(window,textvariable=self.AnnualRateInterestVar,justify=RIGHT).grid(row=1,column=2)

        self.numberOfYearVar = StringVar()
        Entry(window, textvariable=self.numberOfYearVar, justify=RIGHT).grid(row=2, column=2)

        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)


        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window,font='Helvetica 12 bold',bg='light green', textvariable=self.monthlyPaymentVar).grid(row=4,column=2,sticky=E)

        self.totalPaymentVar = StringVar()
        lbltotalPayment = Label(window,font='Helvetica 12 bold',bg='light green',textvariable=self.totalPaymentVar).grid(row=5,column=2,sticky=E)



# Part 3
# 1. Create buttons to calculate values.
# 2. Create a button to clear user input and values entered by user.
        btncalculatePayment = Button(window,text='Claculate Payment',bg='black',fg='red',font='Helvetica 14 bold',command=self.calculatePayment).grid(row=6,column=2,sticky=E)
        btnClear = Button(window,text='Clear',bg='blue',fg='red',font='Helvetica 14 bold',command=self.delete_all).grid(row=6,column=10,padx=20,pady=20,sticky=E)
        window.mainloop()

LoanCalculator()
