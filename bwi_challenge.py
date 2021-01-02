#opening the csv file and read all the data in there
#the date is taken out of the challenge discription
def open_data(filename):
	data = []
	driver = []
	with open(filename, "r") as infile:
		for line in infile:
			if line.startswith("Fahrer"):
				driver_check = []
				driver_check = line.split(",")
				driver_check[1] = float(driver_check[1])
				driver.append(driver_check)
			else:
				model = []
				model = line.split(",")
				for attribute in range(len(model)):
					if attribute is not 0:
						model[attribute] = float(model[attribute])
				data.append(model)

	return data, driver

#calculate utility/gramm ratio 
#we are caped by the mass we can transport, so its the best to aquire the maxiumum utility per gramm 
def calc_ugr(data):
	for hardware in data:
		ratio = hardware[3] / hardware[2]
		hardware.append(ratio)

	return data

#using bubble sort algorithm to sort the ratio decreasing
#bubble sort isn't that efficient but stable and the data isn't that big, so it can be used and its easy to implement
def bubble_sort(array, position):
    index = len(array) - 1
    while index >= 0:
        for j in range(index):
            if array[j][position] < array[j+1][position]:
                array[j], array[j+1] = array[j+1], array[j]
        index -= 1
    return array

#print the load of a truck and save it to a new file
def print_truck_load(truckload, truck_number):
	initial_sentense = f"Truck No. {truck_number} should load the following items:"
	print(initial_sentense)
	print("Hardware".ljust(20) + "Quantity".center(20))
	print(40*"-")
	for index in range(len(truckload)):
		print(f"{truckload[index][0]:20}\t{truckload[index][1]:8}")
	
	#calculate the utility
	commulated_utility = 0
	for index in range(len(truckload)):
		commulated_utility += truckload[index][3] * truckload[index][1]
	

	
	filename = "Truckload/packinglist_truck_no_" + str(truck_number) + ".txt"
	with open(filename, "w") as outfile:
		outfile.write(initial_sentense + "\n")
		outfile.write("Hardware".ljust(20) + "Quantity".center(20) + "\n")
		outfile.write(60*"-"+"\n")
		for index in range(len(truckload)):
			outfile.write(f"{truckload[index][0]:20}\t{truckload[index][1]:8}\n")
		outfile.write(f"\nThe commulated utility equals {commulated_utility}\n")
	print(f"\nThe maxiumum Utility of this load is: {commulated_utility}")
	print("You also can find a list of the load in folder Truckload.")

#funktion to load as much as possible of one item to the truck
def load_item(data, current_available_weight):
	num_loaded_items = 0
	#check if you still can load something
	while current_available_weight > 0:
		#check if quantity is available and when we load the item we dont overload the truck
		if data[1] > 0 and current_available_weight - data[2] >= 0:
			data[1] -= 1
			current_available_weight -= data[2]
			num_loaded_items += 1
		else:
			break

	return data, current_available_weight, num_loaded_items

#loading the truck with the best hardware first
def load_truck(data, driver_weight, max_truck_weight, truck_number):
	truckload = []
	current_available_weight = max_truck_weight - driver_weight
	#transforming the available weight into gramm not kg anymore
	current_available_weight = current_available_weight * 1000
	
	#try to load each item / best first
	for d in range(len(data)):
		# try to load as much of best item first, after that next item
		data[d], current_available_weight, num_loaded_items = load_item(data[d], current_available_weight)
		
		if num_loaded_items != 0:
			item = []
			item.append(data[d][0]) 		#append name of item
			item.append(num_loaded_items) 	#append number of items
			item.append(data[d][2])			#append weight of item
			item.append(data[d][3])			#append utility of each item
			truckload.append(item)

	
	#print the load for a truck in console and saves as txt data in folder Truckload
	print_truck_load(truckload, truck_number)
	
	#calculate load weight
	if calc_load_weight(truckload, driver_weight) > max_truck_weight:
		print("Something went wrong, please try again.")
		exit()

	return data

#calculate the loadweight of the truck inc. driver
def calc_load_weight(truck_load, driver_weight):
	mass = driver_weight * 1000
	for load in truck_load:
		mass += load[2] * load[1]

	print(f"the truck is loaded with {mass/1000}kg.\n\n")
	return mass/1000


if __name__ == '__main__':
	filename = "datensatz.csv"
	#load data out of csv file
	try:
		data_driver = open_data(filename)
	except FileNotFoundError: 
		filename = input("Whats the loading filename? ")
		data_driver = open_data(filename)
	data = data_driver[0]
	driver = data_driver[1]
	driver_count = len(driver)
	max_weight = input("Whats tha max load of the Truck? : ")
	if max_weight is "":
		max_weight = 1100.0
	else:
		try:
			max_weight = float(max_weight)
		except ValueError:
			print("The number you used is not valid. You are using the default value of 1100kg.\n")
			max_weight = 1100.0
	#calculates the utility per gramm ratio and appends to the data array
	data = calc_ugr(data)
	#sort the array decresing by the ratio
	data = bubble_sort(data, 4)
	truck_number = 1
	for truck_driver in driver:
		#loads truck and returns the edited data array
		data = load_truck(data, truck_driver[1], max_weight, truck_number)
		truck_number += 1



