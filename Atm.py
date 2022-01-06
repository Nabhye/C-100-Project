class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceinquiry(self):
        print("Enter Balance is: $100")

    def cashwithdrawal(self, amount):
        new_amount = 100-amount
        print("You withdrawed: " + str(amount) + "Your remaining balance is: " + str(new_amount))

def main():
    name = input("Hello what is your name?")
    print("Hello," + name)
    cardnumber = input("Insert your card number: ")
    pin = input("Enter your pin: ")
    new_user = Atm(cardnumber, pin)

    print("Choose your activity")
    print("1. Balance Inquiry")
    print("2. Cash Withdrawl")
    activity = int(input("Enter your activity choice: "))

    if(activity == 1):
        new_user.balanceinquiry()
    elif(activity == 2):
        amount = int(input("Enter the amount: "))
        new_user.cashwithdrawal(amount)

if __name__ == "__main__":
    main()