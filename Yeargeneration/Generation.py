Year = int(input("Please enter the year you were born: "))                           #This is used to ask the year you were born
if Year < 1945:                                                                      #First threshold condition
    Category_Name = "Silent Generation"                                              #Category for the first condition
elif Year < 1964:                                                                    #Second threshold condition
    Category_Name = "Baby Boomer"                                                    #Category for the second condition
elif Year < 1980:                                                                    #Third threshold condition                                                                 
    Category_Name = "Generation X"                                                   #Category for the third condition
elif Year < 1996:                                                                    #Fourth threshold condition
    Category_Name = "Millennials"                                                    #Category for the fourth condition
elif Year < 2012:                                                                    #Fifth threshold condition
    Category_Name = "Generation Z"                                                   #Category for the fifth condition
else:                                                                                #Default condition for all other cases
    Category_Name = "Generation Alpha"                                               #Default category for the else condition
print(f"You were born in: {Category_Name}")                                          #Print the Generation you were born in

