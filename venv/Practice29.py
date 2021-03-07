choice = "yes"
#file= open("quote.txt", "w") # w will over write the previous data
file= open("quote.txt", "a") # a will append the data with previous data


while choice == "yes":
    quote= input("Enter your quote: ")
    print("\nYou entered: ",quote)
    file.write(quote)
    file.write("\n")
    print("Quote Saved")

    choice= input("\nYou want to write more quotes(yes/no)")