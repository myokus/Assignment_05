#------------------------------------------# 
# Title: CDInventory.py 
# Desc: Script CDInventory to store CD Inventory data
# Change Log: (Who, When, What) 
# DBiesinger, 2030-Jan-01, Created File #
# MYokus, 2021-Aug-06, Added Code 
#------------------------------------------#


# Declare variables

strChoice = '' # User input
lstTbl = []  # list of dictionaries to hold data
dicRow = {}  # a dictionary
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n (Note: There must be CDInventory.txt file in the directory to load the data from the text file!).\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 7. Exit the program if the user chooses so
        break
    if strChoice == 'l':  # no elif necessary, as this code is only reached if strChoice is not 'x'
        # 2. Load inventory from file
        lstTbl.clear() # Clear the inventory list in the memory before loading the file
        objFile = open(strFileName, 'r') # Open the CDInventory.txt file
        for row in objFile:
            lstRow = row.strip().split(',') # Remove "\n" at the end of each row and separates each element with a comma
            dicRow = {'id': int(lstRow[0]), 'title': lstRow[1], 'artist': lstRow[2]}
            lstTbl.append(dicRow) # Append the new dictionary to the list
        objFile.close() # Close the CDInventory.txt file
    elif strChoice == 'a':
        # 3. Add CD data to list in memory
        strID = input('Enter an ID: ') # Read "CD ID" user input
        strName = input('Enter the CD\'s Title: ') # Read "CD Title" user input
        strMail = input('Enter the Artist\'s Name: ') # Read "CD Name" user input
        intID = int(strID)
        dicRow = {'id': intID, 'title': strName, 'artist': strMail} # New CD data dictionary
        lstTbl.append(dicRow) # Append the new CD data dictionary to the list
        print()
    elif strChoice == 'i':
        # 4. Display current inventory
        print('ID, Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ') # Unpacking the list with *
        print()
    elif strChoice == 'd':
        # 5. Delete CD from inventory
        deleteRow = int(input('Which CD entry (row) do you like to delete?: '))
        lstTbl.remove(lstTbl[deleteRow-1]) # Remove Xth entry in CD data inventory
    elif strChoice == 's':
        # 6. Save inventory to a text file CDInventory.txt
        objFile = open(strFileName, 'w') # Open the CDInventory.txt file. 
        #"w" mode: An existing file with the same name will be erased and it will write over.
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n' # Remove ',' at the end of each row and add a new line
            objFile.write(strRow) # Write each DC data row to the CDInventory.txt file
        objFile.close() # Close the CDInventory.txt file
    else:
        print('Please choose either l, a, i, d, s or x!')