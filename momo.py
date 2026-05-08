secret_pin = "2345"
balance = 1000

pin = input("Enter your pin: ")
if pin == secret_pin:
    print("Welcome to your account!")
    print("Your balance is: ", balance) 

else:    print("Incorrect pin. Please try again.")



