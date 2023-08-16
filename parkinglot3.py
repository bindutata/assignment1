'''class ParkingLot:
    def _init_(self):
        self.floors = 3
        self.capacity_per_floor = 30
        self.available_spots = {
            'Compact': [[self.capacity_per_floor, []] for _ in range(self.floors)],
            'Large': [[self.capacity_per_floor, []] for _ in range(self.floors)],
            'Small': [[self.capacity_per_floor, []] for _ in range(self.floors)],
            'Electrical': [[self.capacity_per_floor, []] for _ in range(self.floors)]
        }
    
    def book_spot(self, user_name, vehicle_type):
        vehicle_mapping = {
            'car': 'Compact',
            'van': 'Large',
            'motorcycle': 'Small',
            'electrical': 'Electrical'
        }
        vehicle_type = vehicle_mapping.get(vehicle_type.lower())
        
        if not vehicle_type:
            return "Invalid vehicle type."
        
        for floor in range(self.floors):
            if self.available_spots[vehicle_type][floor][0] > 0:
                spot_number = self.capacity_per_floor - self.available_spots[vehicle_type][floor][0] + 1
                self.available_spots[vehicle_type][floor][0] -= 1
                self.available_spots[vehicle_type][floor][1].append(spot_number)
                return f"Spot booked for {user_name}. Floor: {floor + 1}, Spot Number: {spot_number}"
        
        return "No parking spots available for the selected vehicle type."

    def check_out(self, user_name, vehicle_type, floor, spot_number):
        vehicle_mapping = {
            'car': 'Compact',
            'van': 'Large',
            'motorcycle': 'Small',
            'electrical': 'Electrical'
        }
        vehicle_type = vehicle_mapping.get(vehicle_type.lower())
        
        if not vehicle_type:
            return "Invalid vehicle type."

        if self.available_spots[vehicle_type][floor - 1][0] == self.capacity_per_floor:
            return "This spot is not allocated or already checked out."

        if spot_number in self.available_spots[vehicle_type][floor - 1][1]:
            self.available_spots[vehicle_type][floor - 1][0] += 1
            self.available_spots[vehicle_type][floor - 1][1].remove(spot_number)
            return f"Spot checked out for {user_name}."
        else:
            return "Spot not found."

    def display_available_spots(self):
        for floor in range(self.floors):
            print(f"Floor {floor + 1} - Compact: {self.available_spots['Compact'][floor][0]}, Large: {self.available_spots['Large'][floor][0]}, Small: {self.available_spots['Small'][floor][0]}, Electrical: {self.available_spots['Electrical'][floor][0]}")

class ParkingFeeCalculator:
    def calculate_fee(self, hours):
        base_fee = 40
        extra_fee_per_hour = 15
        total_fee = base_fee + (hours - 1) * extra_fee_per_hour
        return total_fee

if __name__ == "_main_":
    parking_lot = ParkingLot()
    fee_calculator = ParkingFeeCalculator()

    while True:
        print("\nWell come to the venky parking lot..")
        print("\nHere maximun time of parking is 6 hours only kindly note it.")
        choice = int(input("1. Book Spot\n2. Check Out\n3. Customer Info\n4. Display Available Spots\n5. Exit\nEnter your choice: "))

        if choice == 1:
            user_name = input("Enter your name: ")
            vehicle_type = input("Enter your vehicle type (car/van/motorcycle/electrical): ")
            result = parking_lot.book_spot(user_name, vehicle_type)
            print(result)
            hours_parked = int(input("Enter hours parked: "))
            total_fee = fee_calculator.calculate_fee(hours_parked)
            print(f"Total parking fee: {total_fee} rupees")

        elif choice == 2:
            user_name = input("Enter your name: ")
            vehicle_type = input("Enter your vehicle type (car/van/motorcycle/electrical): ")
            floor = int(input("Enter floor number: "))
            spot_number = int(input("Enter spot number: "))
            result = parking_lot.check_out(user_name, vehicle_type, floor, spot_number)
            print(result)

        elif choice == 3:
            user_name = input("Enter your name: ")
            mobile_number = input("Enter your mobile number: ")
            vehicle_type = input("Enter your vehicle type (car/van/motorcycle/electrical): ")
            result = parking_lot.book_spot(user_name, vehicle_type)
            print(result)
            hours_parked = int(input("Enter hours parked: "))
            total_fee = fee_calculator.calculate_fee(hours_parked)
            print(f"Customer Info: Name: {user_name}, Mobile Number: {mobile_number}")
            print(f"Total parking fee: {total_fee} rupees")

        elif choice == 4:
            parking_lot.display_available_spots()

        elif choice == 5:
            break
p=ParkingLot()
p.book_spot('anu','car')
p.check_out()
p.display_available_spots()
f=ParkingFeeCalculator()
f.calculate_fee()'''


class ParkingLot:
    def __init__(self):
        self.number_of_floors = 5
        self.capacity_per_floor = 100
        self.available_spots = {
            'Compact': [[self.capacity_per_floor, []] for i in range(self.number_of_floors)],
            'Large': [[self.capacity_per_floor, []] for i in range(self.number_of_floors)],
            'Small': [[self.capacity_per_floor, []] for i in range(self.number_of_floors)],
            'Electrical': [[self.capacity_per_floor, []] for i in range(self.number_of_floors)]
        }
    
    def book_spot(self, user_name, vehicle_type):
        vehicle_mapping = {
            'car': 'Compact',
            'van': 'Large',
            'motorcycle': 'Small',
            'electrical': 'Electrical'
        }
        vehicle_type = vehicle_mapping.get(vehicle_type.lower())
        
        if not vehicle_type:
            return "Invalid vehicle type."
        
        for floor in range(self.number_of_floors):
            if self.available_spots[vehicle_type][floor][0] > 0:
                spot_number = self.capacity_per_floor - self.available_spots[vehicle_type][floor][0] + 1
                self.available_spots[vehicle_type][floor][0]-= 1
                self.available_spots[vehicle_type][floor][1].append(spot_number)
                return "Spot booked for {user_name}. Floor: {floor + 1}, Spot Number: {spot_number}"
        
        return "No parking spots available for the selected vehicle type."

    def check_out(self, user_name, vehicle_type, spot_number):
        vehicle_mapping = {
            'car': 'Compact',
            'van': 'Large',
            'motorcycle': 'Small',
            'electrical': 'Electrical'
        }
        vehicle_type = vehicle_mapping.get(vehicle_type.lower())
        
        if not vehicle_type:
            return "Invalid vehicle type."

        if self.available_spots[vehicle_type][floor - 1][0] == self.capacity_per_floor:
            return "This spot is not allocated or already checked out."

        if spot_number in self.available_spots[vehicle_type][floor - 1][1]:
            self.available_spots[vehicle_type][floor - 1][0] += 1
            self.available_spots[vehicle_type][floor - 1][1].remove(spot_number)
            return "Spot checked out for {user_name}."
        else:
            return "Spot not found."

    def display_available_spots(self):
        for floor in range(self.number_of_floors):
            print("Floor {floor + 1} - Compact:" {self.available_spots['Compact'][floor][0]} 
                  "Large:" {self.available_spots['Large'][floor][0]} 
                  "Small: "{self.available_spots['Small'][floor][0]}
                  "Electrical:" {self.available_spots['Electrical'][floor][0]})

class ParkingFeeCalculator:
    def calculate_fee(self, hours):
        base_fee = 20
        extra_fee_per_hour = 10
        total_fee = base_fee + (hours - 1) * extra_fee_per_hour
        return total_fee

if __name__ == "__main__":
    parking_lot = ParkingLot()
    fee_calculator = ParkingFeeCalculator()

    while True:
        print("\nWell come to the  parking lot..")
        #print("\nHere maximun time of parking is 6 hours only kindly note it.")
        choice = int(input("1. Book Spot\n2. Check Out\n3. Customer Info\n4. Display Available Spots\n5. Exit\nEnter your choice: "))

        if choice == 1:
            user_name = input("Enter your name: ")
            vehicle_type = input("Enter your vehicle type (car/van/motorcycle/electrical): ")
            result = parking_lot.book_spot(user_name, vehicle_type)
            print(result)
            hours_parked = int(input("Enter hours parked: "))
            total_fee = fee_calculator.calculate_fee(hours_parked)
            print(f"Total parking fee: {total_fee} rupees")

        elif choice == 2:
            user_name = input("Enter your name: ")
            vehicle_type = input("Enter your vehicle type (car/van/motorcycle/electrical): ")
            floor = int(input("Enter floor number: "))
            spot_number = int(input("Enter spot number: "))
            result = parking_lot.check_out(user_name, vehicle_type, floor, spot_number)
            print(result)

        elif choice == 3:
            user_name = input("Enter your name: ")
            mobile_number = input("Enter your mobile number: ")
            vehicle_type = input("Enter your vehicle type (car/van/motorcycle/electrical): ")
            result = parking_lot.book_spot(user_name, vehicle_type)
            print(result)
            hours_parked = int(input("Enter hours parked: "))
            total_fee = fee_calculator.calculate_fee(hours_parked)
            print(f"Customer Info: Name: {user_name}, Mobile Number: {mobile_number}")
            print(f"Total parking fee: {total_fee} rupees")

        elif choice == 4:
            parking_lot.display_available_spots()

        elif choice == 5:
            break

