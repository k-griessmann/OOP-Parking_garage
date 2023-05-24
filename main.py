class Garage():

    def __init__(self):
        self.tickets = [0,1,2,3,4,5,6,7,8,9,10]
        self.spaces = [0,1,2,3,4,5,6,7,8,9,10]
        self.current_ticket = {}

    def takeTicket(self):
        if len(self.spaces) == 0:
            print('Sorry the Garage is full')
        else:
            self.tickets.remove(self.tickets[-1])
            self.spaces.remove(self.spaces[-1])
        
    def payForParking(self):
        pay = input('Enter 1 to pay now ')
        if pay == '1':
            self.current_ticket['Paid'] = True
            print('Ticket has been paid, you have 15 minutes to leave')
        
    def leaveGarage(self):
        if self.current_ticket['Paid']==True:
            print('Thank you, have a nice day!')

        else:

            pay = input('Enter 1 to pay now: ')

            while amount!='1':
                amount = input('Enter 1 to pay now: ')

            # increase the amount of tickets available by 1
            self.tickets.append(self.tickets[-1]+1)

            # increase the amount of parkingSpaces available by 1
            self.parkingSpaces.append(self.parkingSpaces[-1]+1)

def main():
    
    car = Garage()
    print('Welcome to the Parking Garage!\n')

    print('Please take a ticket.')

    printedTicket = input('Enter T to take ticket: ')

    if printedTicket.upper() == "T":
        car.takeTicket()

        car.payForParking()

        car.leaveGarage()

    else:
        print('Error')

main()