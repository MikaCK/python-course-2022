from datetime import datetime

session1_start = datetime(2021, 7, 1)
session1_end = datetime(2021, 8, 10)
session2_start = datetime(2021, 8, 11)
session2_end = datetime(2021, 8, 31)


ticket_date_input = input("Insert the booking date(DD.MM.YYYY): ")
ticket_number = int(input ("Insert the number of tickets: "))


ticket_date = datetime.strptime(ticket_date_input,"%d.%m.%Y")
print(ticket_date)

if ticket_date >= session1_start and ticket_date <= session1_end:
    print(ticket_number * 250)
elif ticket_date >= session2_start and ticket_date <= session2_end:
    print(ticket_number * 180)
else:
    print("Summer cinema is closed at this time")
    
