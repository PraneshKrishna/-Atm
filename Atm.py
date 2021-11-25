class Atm:
     
   def Entering (self, money, pinNumber, cardNumber):
       self.money = money
       self.pinNumber = pinNumber
       self.cardNumber = cardNumber

       money = input('ENTER AMOUNT')
       pinNumber = input('ENTER PINNUMBER')
       cardNumber = input('ENTER CARDNUMBER')

   def cashWithdrawl (self):
       cashNeeded = input('ENTER THE AMOUNT YOU NEED')
       balence = cashNeeded - self.money
       print ('Cash is Withdrawn')  
Atm()










#def atm():
        #money = input("Enter the Amount you need: ")
        
        #pinNumber = input("Enter the Pin Number: ")
        #if ( pinNumber == money ) : 
           # print('WHAT??? Boy....')
        #cardNumber = input("Enter the Card Number: ")
        #if ( cardNumber == money ) : 
          #  print('Bro....at this point its not even funny')
#atm()
