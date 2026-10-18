# Ticketing system in python


# DICTIONARY
# The Destination Station (DS) : string
# Number of passenger (P) : integer
# Price ticket (PT) : integer
# Passenger Data (PD) : string
# Seat Configuration (SC)
# Total Payment (TP) : string

# SEAT CONFIGURATION
SC = [
    ["O", "O", "O", "O"],
    ["O", "O", "O", "O"],
    ["O", "O", "O", "O"],
    ["O", "O", "O", "O"]
]

# INPUT DESTINATION AND EACH TICKET PRICE
print("Welcome to whoosh")
DS = input("enter your destination: ")
PT = 1000000

# INPUT THE NUMBER OF PASSENGER
P = 0
while (P <= 0 or P > 16): 
    P = int(input("Enter the number of passenger: "))
    if P <= 0:
        print("the minimum passenger is 1 please add more people")
    elif (P > 16):
        print(f"Only 16 seats are available, please reduce the passengers")

# INITIALIZING AN EMPTY LIST TO STORE PASSENGER DATA
PD = []

# LOOPING BASED ON THE PASSENGERS TO INPUT DATA AND SELECT SEATS
for i in range(P):
    print(f"\n Passenger {i + 1}")
    name = input("Enter Name: ")
    nik = input("Enter NIK: ")

# LOOP TO SELECT A SEAT UNTIL A VALID AND AVAILABLE SEAT IS CHOSEN
    while True:
        print("\nSeat Map:")
        for row in SC:
            print(row)
        r = int(input("Choose row (0-3): "))
        c = int(input("Choose column (0-3): "))

        # VALIDATING THAT THE SEAT EXISTS
        if r < 0 or r > 3 or c < 0 or c > 3:
           print("Invalid seat! Row and column must be between 0 and 3.")
           continue 

        # VALIDATING AND CHECKING IF THE SEAT IS AVAILABLE
        if SC[r][c] == "O":
            SC[r][c] = "X"
            PD.append({"name": name, "nik": nik, "seat": f"({r}, {c})"})
            break
        else:
            print("Seat is already booked! Choose another.")

# CALCULATING TOTAL PAYMENT AND PRINTING THE SUMMARY TICKET
TP = P * PT
print("\n=== WHOOSH TICKET SUMMARY ===")
print(f"Destination : {DS}")
print(f"Total Passengers : {P}")

for data in PD:
    print(f"- {data['name']} | NIK: {data['nik']} | Seat: {data['seat']}")

print(f"TOTAL PAYMENT : Rp {TP:,}")
print("Thank you!")
