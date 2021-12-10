f = open("modules_d1_2019.txt", "r")

if f:
    print("Successfully opened data... \n")

total_fuel = 0

for line in f:
    # Strip off leading and trailing whitespace characters, and convert string to integer
    mass = int(line.strip())

    # Calculate required fuel for the module
    module_fuel = int(mass/3) - 2

    # Add module's required fuel to total fuel
    total_fuel += module_fuel

# Print the total fuel required to the command line
print("Total fuel for modules: " + str(total_fuel) + "\n")

f.close()

f = open("modules_d1_2019.txt", "r")

if f:
    print("Successfully reopened data... \n")

# Part 2:
total_fuel = 0

for line in f:
    # Strip off leading and trailing whitespace characters, and convert string to integer
    mass = int(line.strip())

    # Calculate required fuel for the module
    module_fuel = int(mass/3) - 2

    fuel_fuel = module_fuel
    # Keep calculating extra fuel until the quantity is <= 0
    while fuel_fuel > 0:
        # Calculate the required fuel for the fuel
        fuel_fuel = int(fuel_fuel/3) - 2

        # Add extra fuel to the total rocket fuel
        if fuel_fuel > 0:
            module_fuel += fuel_fuel

    # Add module's required fuel to total fuel
    total_fuel += module_fuel

    

print("Total fuel: " + str(total_fuel) + "\n")
