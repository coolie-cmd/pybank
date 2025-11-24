import sys

class Bank:
    def __init__(self, balance ,pin):
      self.balance = balance
      self.pin = pin 

    def pinCheck(self):
       i = 1
       trial = 0
       while i<=5:
          while trial == self.pin:
             trial = input("enter secret pin: ")
             if trial == self.pin:
                print("u may proceed 😊 ")
                break
             else:
                print(f"u are wrong. u have {5-i} trials left.")
                if 5-i == 0 :
                   print("u have failed in all allowed trials. u cant login again.")
                   break
          i+=1   

    def deposit(self):
       amount = int(input("enter amount u wnat to deposit int ur bank account: "))
       self.balance += amount

    def withdraw(self):
       amountw = int(input("enter amount u want to withdraw from ur account: "))
       if self.balance > amountw:
           self.balance -= amountw
       else :
          print ("insufficient balance!")
    def checkBalance(self):
       print(f"ur current balance is: {self.balance}tshs")

if __name__== "__main__":
   print("hello there😊👋")
   print("welcome to pybank 💳🏧")
   print("before u begin using our services,sign up")
   name = input("whats ur name? ")
   print(f"well its nice having u {name}")
   password = 1
   veri = 0
   while password != veri:
      password = int(input("set up ur secret pin: "))
      veri = int (input("verify the entered pin: "))
      if password == veri :
         print("pin is set 👍")
      else:
         print("pin doesnt match verification")
         print("try again.")
   
   initialAmount =int(input("enter the initial amount u want to deposit in ur bank account:"))
   
   bank = Bank(initialAmount,password)
   print("welcome to pybank services💸")
   print(f"ur bank account is set {name} ")
   choice =0
   while choice != 4:
      print("MAIN MENU")
      print("1.deposit")
      print("2.withdraw")
      print("3.check balance")
      print("4.exit")
      choice=input('enter ur choice according to the numbers: ')
      if choice == '1':
         bank.pinCheck()
         bank.deposit()
         bank.checkBalance()
      elif choice == '2':
         bank.pinCheck()
         bank.withdraw()
         bank.checkBalance()
      elif choice == "3":
         bank.checkBalance()
      elif choice == '4':
         sys.exit("goodbye!")
      
      else:
         print("invalid choice")

         print("thank u for choosing pybank")
         print("u are very welcome.")



    



