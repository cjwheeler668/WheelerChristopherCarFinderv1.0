import os

#input from user
# Password prompt
def get_password():
  """Prompts the user for a password and validates it."""
  password = input("Enter the password: ")
  while password != "OnLoad":
    print("Incorrect password. Please try again.")
    password = input("Enter the password: ")
  print("Password accepted.")
  
def load_vehicles_from_file():
  """Loads authorized vehicles from a file if it exists."""
  if os.path.exists("vehicles.txt"):
    with open("vehicles.txt", "r") as file:
      return file.read().splitlines()
  else:
    return []
    
def save_vehicles_to_file(vehicles):
  """Saves the AllowedVehiclesList to a file named "vehicles.txt"."""
  with open("vehicles.txt", "w") as file:
      file.write("\n".join(vehicles))
    
#Menu Functions
def print_vehicles(vehicles):
  """Prints the list of authorized vehicles."""
  print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
  for vehicle in vehicles:
    print(vehicle)
    
def search_vehicle(vehicles):
  """Searches for a vehicle in the list."""
  print("Please Enter the full Vehicle name: ")
  vehicle = input()
  if vehicle in vehicles:
    print(f"The {vehicle} is an authorized vehicle") 
  else:
    print(f"The {vehicle} is not an authorized vehicle") 
    
def add_vehicle(vehicles):
  """Adds a vehicle to the list."""
  print("Please enter the full Vehicle name you would like to add: ")
  vehicle = input()
  if vehicle in vehicles:
    print(f"The {vehicle} is already in the list")
  else:
    vehicles.append(vehicle)
    print(f"You have added \"{vehicle}\" as an authorized vehicle")
    return vehicles
    
def delete_vehicle(vehicles):
  """Deletes a vehicle from the list."""
  print("Please enter the full Vehicle name you would like to REMOVE: ")
  vehicle = input()
  if vehicle in vehicles:
    print(f"Are you sure you watn to remove \"{vehicle}\" from the list Authourized Vehicle List?")
    confirm = input("Enter yes or no: ")
    if confirm.lower() == "yes":
      vehicles.remove(vehicle)
      print(f"You have removed \"{vehicle}\" from the list")
      return vehicles
    else:
      return vehicles
  else:
    print(f"The {vehicle} is not in the list of authorized vehicles")
    return vehicles
    
# Menu Function
def menu():
  print("*******************************")
  print("AutoCountry Vehicle Finder v1.0")
  print("*******************************")
  print("Plese enter the following number bellow from the following menu: ")
  print("[1] PRINT all Authorized Vehicles")
  print("[2] SEARCH for Authorized Vehicle")
  print("[3] ADD Authorized Vehicle")
  print("[4] DELETE Authorized Vehicle")
  print("[5] Exit")
  print("*******************************")
# Main Program Logic
# Password prompt
get_password()

# Array of authorized vehicles
AllowedVehiclesList = load_vehicles_from_file()

# Menu function (already defined)
menu()

# Give option to choose
option = int(input("Enter your option: "))

# While loop to keep the program running
while option != 5:
  if option == 1:
    print_vehicles(AllowedVehiclesList)

  elif option == 2:
    search_vehicle(AllowedVehiclesList)

  elif option == 3:
    AllowedVehiclesList = add_vehicle(AllowedVehiclesList)
    save_vehicles_to_file(AllowedVehiclesList)
  elif option == 4:
    AllowedVehiclesList = delete_vehicle(AllowedVehiclesList)
    save_vehicles_to_file(AllowedVehiclesList)
  # Gives menu option to choose
  
  menu()
  option = int(input("Enter your option: "))
  
# Exit the program
save_vehicles_to_file(AllowedVehiclesList)
print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")