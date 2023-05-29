tickets=[10]
parkingSpaces=[10]
currentTicket={}

class Parking():

    def __init__(self, ticket, parkingSpace):
        self.ticket = ticket
        self.parkingSpace = parkingSpace

    def take_ticket(self):
        for i in tickets:
            tickets -= i
            print(i)
            print(tickets)
            for i in parkingSpaces:
                parkingSpaces -= i
                print(i)
                print(parkingSpaces)
            

# for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    # i = i - 1
    # print i
            
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
    def pay_parking(self):
        payment = input(f"Welcome to sustainable pavement car parking."
                        f"It is $1.00 for 15 mins or parking, select space to continue." 
                        f"If you wish to end press 'q'. ")
        if payment == 'q':
            return
        elif '':
            print("Your ticket has been aid and you have 15 mins to leave or else...")
            currentTicket +=1

            
        
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display
#   a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
    def leave_garage(self):
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)