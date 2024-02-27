""" The Project is done by Tamreen, Ali and Ziad, 
we will use the return statement to return to send a result back to the caller function
all the constant rates we have used in this program, was found from google
we will use the print statement which displays output to the terminal """

def aed_to_eur(money): # money is the parameter and this option willl let you convert from aed to euro
    rate = 0.25 
    return money * rate #, we are multiplying "money * rate", to calculate the equivalent amount of money in another currency.

def eur_to_aed(amount): #def is used to define a function
    rate = 3.97
    return amount * rate #amount and money means the same thing, don't confuse yourself

def aed_to_usddollar(money):
    rate = 0.27
    return money * rate 

def usddollar_to_aed(amount):
    rate = 3.67
    return amount * rate

def aed_to_britishPound(money):
    rate = 0.21
    return money * rate

def britishPound_to_aed(amount):
    rate = 4.66
    return amount * rate


print("Main menu! this is the conversion game")

local_currencies = ["AED to Foreign currency"]
for local_currency in local_currencies:
     print(local_currency)

print("or")

foreign_currencies = ["Foreign currency to AED"]
for foreign_currency in foreign_currencies:
     print(foreign_currency)


    
while True: #while loop will constantly execute a block of code as long as a specified condition is true
       main_menu = print("Select the conversion direction:")
       print("1. AED to other currencies")
       print("2. Other currencies to AED")
       print("3. Exit")
        
       main_choice = input("Enter your choice: ")
       if main_choice == '1':
           print("1. AED to EUR")
           print("2. AED to USD DOLLAR")
           print("3. AED to BRITISH POUND")
           sub_choice = input("Enter your choice (1, 2, or 3): ")
           money = float(input("Enter the amount in AED: ")) #float represents numbers with decimal points

           if sub_choice == '1':
            converted_amount = aed_to_eur(money)
            print(money, "AED is equal to converted_amount: EUR",converted_amount,) 
            break
           
           elif sub_choice == '3':
            converted_amount = aed_to_britishPound(money)
            print(money, "AED is equal to converted_amount: GBP", converted_amount,)
            break
           elif sub_choice == '2':
            converted_amount = aed_to_usddollar(money)
            print(money, "AED is equal to converted_amount: USD", converted_amount,)
            break
           else:
            print("Your option is invalid")
            break

            
    
       elif main_choice == '2':
          print("1. USD to AED")
          print("2. British Pound to AED")
          print("3. EUR to AED")
        
          sub_choice = input("Enter your choice (1, 2, or 3): ")
          amount = float(input("Enter the amount: "))
          if sub_choice == '1':
            converted_amount = usddollar_to_aed(amount)
            print(amount, "USD is equal to converted_amount: AED", converted_amount) 
            break
          elif sub_choice == '2':
            converted_amount = britishPound_to_aed(amount)
            print(amount, "GBP is equal to converted_amount: AED", converted_amount)
            break
          elif sub_choice == '3':
            converted_amount = eur_to_aed(amount)
            print(amount, "EUR is equal to converted_amount: AED", converted_amount)
            break
          else:
            print("Your Choice is invalid")
            break




       elif main_choice == '3':
          print("Exiting")
          break
       


       else:
            print("your option is invalid")
            break

while True:     
      continue_game = input("did you enjoy the game (yes or no):")

      if continue_game == 'yes':
         print("thank you for your positive feedback")
         break 

      elif continue_game == 'no':
        input("why did you not enjoy it?:")
        print("thank you for your feedback")
        break

      else:
         print("your statement is invalid")
         break
      
      


def main():
   
 if __name__ == "__main__":
    main()