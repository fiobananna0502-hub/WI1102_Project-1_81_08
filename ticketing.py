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

# STATIONS AND PRICES BASED ON DEPARTURE
ROUTES = {
    "Halim (Jakarta)": {
        "1": ("Karawang", 100000),
        "2": ("Padalarang (Bandung)", 150000),
        "3": ("Tegalluar Summarecon (Bandung)", 150000)
    },
    "Karawang": {
        "1": ("Halim (Jakarta)", 100000),
        "2": ("Padalarang (Bandung)", 150000),
        "3": ("Tegalluar Summarecon (Bandung)", 150000)
    },
    "Padalarang (Bandung)": {
        "1": ("Halim (Jakarta)", 150000),
        "2": ("Karawang", 150000),
        "3": ("Tegalluar Summarecon (Bandung)", 50000)
    },
    "Tegalluar Summarecon (Bandung)": {
        "1": ("Halim (Jakarta)", 150000),
        "2": ("Karawang", 150000),
    }
}

DEPARTURES = {
    "1": "Halim (Jakarta)",
    "2": "Karawang",
    "3": "Padalarang (Bandung)",
    "4": "Tegalluar Summarecon (Bandung)"
}

print("Welcome to whoosh")

# CHOOSE DEPARTURE STATION
print("\nChoose your departure station:")
for key, name in DEPARTURES.items():
    print(f"{key}. {name}")

dep_choice = ""
while dep_choice not in DEPARTURES:
    dep_choice = input("Enter departure number: ")
    if dep_choice not in DEPARTURES:
        print("Invalid choice! Please enter a number from the list.")

departure = DEPARTURES[dep_choice]
print(f"Departure station: {departure}")

# CHOOSE DESTINATION STATION
STATIONS = ROUTES[departure]
print("\nChoose your destination:")
for key, (name, price) in STATIONS.items():
    print(f"{key}. {name} Rp {price:,}")
 
choice = ""
while choice not in STATIONS:
    choice = input("Enter destination number: ")
    if choice not in STATIONS:
        print("Invalid choice! Please enter a number from the list.")
 
DS, PT = STATIONS[choice]
print(f"You selected {DS}, ticket price Rp {PT:,}")

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

    # LOOP TO INPUT NIK UNTIL IT IS EXACTLY 16 DIGITS
    while True:
        nik = input("Enter NIK (16 digits): ")
        if len(nik) == 16 and nik.isdigit():
            break
        print("Invalid NIK! NIK must be exactly 16 digits (numbers only).")

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
