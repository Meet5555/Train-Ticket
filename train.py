from math import fabs


class Train:
    a = []

    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        for i in range(1, (self.seats)+1):
            self.a.append(i)

    def getStatus(self):
        print("--------------------------------------------")
        print(f"\nThe name of train is {self.name}")
        print(f"\nThe available seats in train are: {self.seats}")

    def fareInfo(self):
        print("--------------------------------------------")
        print(f"\nThe fare amount is: Rs {self.fare}")

    def bookTicket(self):
        if len(self.a) != 0:
            print("--------------------------------------------")
            print(
                f"\nYour ticket is booked! and your seat number is {self.a[0]}")
            self.a.remove(self.a[0])
            self.seats = len(self.a)
        else:
            print("--------------------------------------------")
            print("\nTrain is full!")

    def isEmpty(self):
        if self.seats == 250:
            return True
        else:
            return False

    def isFull(self):
        if self.seats == 0:
            return True
        else:
            return False

    def cancleTicket(self, seatNo):
        if seatNo in self.a:
            print("--------------------------------------------")
            print("\nThis ticket is not Booked!")
        else:
            print("--------------------------------------------")
            print("\nYour ticket is cancled!")
            self.a.append(seatNo)
            self.a.sort()
            self.seats = len(self.a)


Rajdhani = Train("Rajdhani Express", 500, 250)

while(True):
    welcomeMsg = "\n------ Welcome to Rajdhani Express ------ \n 1. Train info \n 2. Fair info \n 3. Book Ticket \n 4. Cancle ticket \n 5. Exit"
    print(welcomeMsg)
    a = int(input("Enter your choice: "))
    if a == 1:
        Rajdhani.getStatus()
    elif a == 2:
        Rajdhani.fareInfo()
    elif a == 3:
        if Rajdhani.isFull():
            print("\nTrain is Full!!")
        else:
            Rajdhani.bookTicket()
    elif a == 4:
        if Rajdhani.isEmpty():
            print("--------------------------------------------")
            print("\nCan't cancle, any seat is not Boooked!!")
        else:
            seat = int(input("Enter seat number to cancle: "))
            Rajdhani.cancleTicket(seat)
    elif a == 5:
        print("\nThank you for using this Program. Have a Great Day!!")
        exit()
    else:
        print("--------------------------------------------")
        print("\nOops! Invalid Choice")