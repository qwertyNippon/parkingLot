


class Parking():
    tickets=10
    parkingSpaces=10
    currentTicket={"paid":False, "amount":0}

    def __init__(self, currentTicketCount=0):
        self.currentTicketCount = currentTicketCount

    def take_ticket(self):
        print("congrats you have a ticket")
        self.tickets -= 1
        self.parkingSpaces -= 1
            
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
    def pay_parking(self):
        payment = input(f"Welcome to sustainable pavement car parking.\nIt is $1.00 for 15 mins or parking, entre 1 dollar for 15 minutes.\nIf you wish to end press 'q'. ")
        
        if payment == 'q':
            return
        elif payment == "1" or payment == "1.00":
            # just incase user inputs 1 or 1.00
            print("Your ticket has been paid and you have 15 mins to leave or else...")
            self.currentTicketCount += 1
            self.currentTicket["paid"] = True
            # referring to the key.
            print(self.currentTicketCount)
            print(self.currentTicket)
        else:
            print(f"sorry we do not serve dinosaur juice lovers here.")
            # update the "currentTicket" dictionary key "paid" to True

            
        
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display
#   a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
    # def leave_garage(self):
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

qwerty = Parking()
qwerty.take_ticket()
qwerty.pay_parking()