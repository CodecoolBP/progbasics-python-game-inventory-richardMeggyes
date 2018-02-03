# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


# Displays the inventory.
def display_inventory(inventory):
    for key, val in inventory.items():
        print("%4i:%10s" % (val, key))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory.keys():
            inventory[item] = inventory[item] +1
        else:
            inventory[item] = 1
    return inventory


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    print("")
    print("Inventory:")
    print("  count    item name")

    longest_key_len = 0
    for key in inventory.keys():
        if len(key) > longest_key_len:
            longest_key_len = len(key)

    print("-" * (longest_key_len + 11))
    total_items = 0

    count_f_sort = True
    if order == "count,asc":
        count_f_sort = False

    for key, val in sorted(inventory.items(), key=lambda p: p[1], reverse=count_f_sort):
        total_items += val

        print("{:^10} {:{align}{width}}".format(val, key, align=">", width = longest_key_len))

    print("-" * (longest_key_len + 11))
    print("Total number of items:", total_items)



# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    csv_lines = ""
    item_list = []
    with open (filename, "r") as f:
        csv_lines = f.readlines()

    for line in csv_lines:
        line = line.replace("\n", "")

        line = line.split(",")
        for item in line:
            item_list.append(item)

    add_to_inventory(inventory, item_list)

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    with open(filename, "w+") as f:
        export_list = []
        for k, v in inventory.items():
            for i in range(0, v):
                export_list.append(k)
        f.write(",".join(export_list))
