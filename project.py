class Movie:
    def __init__(self,movie_name:str,total_seats:int,ticket_price:int):
        self.movie_name = movie_name
        self.total_seats=total_seats 
        self.ticket_price=ticket_price 
        self.booked_seats = 0
    
    def book_ticket(self,numOfTickets:int):
        if numOfTickets>=self.total_seats:
            print (f"{self.booked_seats} seats are not available")
        else:
            self.booked_seats=self.booked_seats+numOfTickets 
            self.total_seats=self.total_seats-numOfTickets 
            print (f"Your tickets are booked")
            print(f"total amt to pay : {self.ticket_price * numOfTickets}")
    
    def showStatus(self)->None:
        print (f"Movie name : {self.movie_name}")
        print (f"tickets available : {self.total_seats}")
        print (f"Price per ticket : {self.ticket_price}")
            

m1=Movie()
m1.showStatus()
m1.book_ticket()

