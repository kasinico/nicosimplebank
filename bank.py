import pickle
import os
import pathlib
from unicodedata import name

#create a class called BankAccount
class BankAccount :

   account_number = 0
   owner = ""
   balance = 0
   type = ""

   def createAccount(self):
       self.account_number = int (input ('Enter the account no : '))
       self.owner = input('Enter the account holder owner :')
       self.type = input('Ente the type of account [C/S] : ')
       self.balance = int(input('Enter The Initial amount(>=500 for Saving and >=1000 for current'))

       print('\n\n\nAccount Created', self.account_number)

#Create a class called Bank
class Bank : 
   accounts = 1035101067
   def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.accounts= int(input ('Enter the account no : '))
        self.balance += amount
        print("\n\n Amount Deposited:",amount,)
   


#Create a class called Customer
class Customer :

   name = ""
   accounts = 0

#Create a class called Transcations
class Transactions :

   account = ""
   amount = 0
   type = ""
   def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
   def display(self):
        print("\n Net Available Balance=",self.balance)
 


 #Object

#Print the Bank  Acc object
Acc = BankAccount()
Acc.createAccount()
#Print the Customer object

#Print the BankAccount object

#Create a new Transaction object
Transc = Transactions()
Transc.withdraw()


#Add the Transaction object to the BankAccount