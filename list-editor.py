# This program allows you to edit a list
# Program created by: Jeferson A. Tadios

def main():
    if menu_input == 1:
        user_input = int(input("Enter the element you want to add: "))
        list_num.append(user_input)
    elif menu_input == 2:
        user_input1 = int(input("Enter the element you want to insert: "))
        user_input2 = int(input("Enter the index number you want to insert the element: "))
        list_num.insert(user_input2, user_input1)
    elif menu_input == 3:
        user_input1 = int(input("Enter the element index you want to change: "))
        user_input2 = int(input("Enter the element you want to change in index "+str(user_input1)+": "))
        list_num[user_input1] = user_input2
    elif menu_input == 4:
        user_input = int(input("Enter the index you want to delete: "))
        list_num.pop(user_input)
    elif menu_input == 5:
        list_num.sort()
    elif menu_input == 6:
        list_num.sort(reverse=True)
    elif menu_input == 7:
        print("Thank you for using this program! Have a nice day (◍•ᴗ•◍)✧*。")
        exit()
    else:
        print("Invalid Input! [Input should be only 1-7]")
        print("")
    print("[!] Default List Array has been updated! [!]",list_num)
    cont()
    showMenu()

def showMenu():
    print(""+"\n")
    print("∎ New List Array = "+ str(list_num)+
      "\n ↳List Element - Values inside the list e.g ("+str(list_num[0]),"and",str(list_num[1])+")"+
      "\n ↳List Index - The position of the values inside the list e.g (Position of value",str(list_num[0]),"is index 0 and position of value",str(list_num[1]),"is index 1)" +
      "\n"+
      "\n✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯"+
      "\n          Menu:"+
      "\n            ↳ [1] Add an element in the list"+
      "\n            ↳ [2] Insert an element in the list"+
      "\n            ↳ [3] Modify an element in the list"+
      "\n            ↳ [4] Delete an element in the list"+
      "\n            ↳ [5] Arrange the list in ascending order"+
      "\n            ↳ [6] Arrange the list in descending order"+
      "\n            ↳ [7] Exit"
    )
    print("✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯"+"\n")

def cont():
    print("")
    continue_prog = input("Do you want to continue? [Y/N]: ").upper()
    if continue_prog != "Y":
        exit()

list_num = [14, 24, 25, 18, 11, 22, 7, 6, 4, 20]
print("")
print("∎ Default List Array = "+ str(list_num)+
  "\n ↳ List Element - Values inside the list e.g ("+str(list_num[0]),"and",str(list_num[1])+")"+
  "\n ↳ List Index - The position of the values inside the list e.g (Position of value",str(list_num[0]),"is index 0 and position of value",str(list_num[1]),"is index 1)" +
  "\n"+
  "\n✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯"+
  "\n          Menu:"+
  "\n            ↳ [1] Add an element in the list"+
  "\n            ↳ [2] Insert an element in the list"+
  "\n            ↳ [3] Modify an element in the list"+
  "\n            ↳ [4] Delete an element in the list"+
  "\n            ↳ [5] Arrange the list in ascending order"+
  "\n            ↳ [6] Arrange the list in descending order"+
  "\n            ↳ [7] Exit"
)
print("✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯"+"\n")


while True:
    menu_input = input("What do you want to do (｡•̀ᴗ-)✧ ? (1-7): ")
    print("")
    if menu_input.isdigit():
        menu_input = int(menu_input)
        main()
    else:
        print("Invalid Input! Please try again [Input should be only 1-7]"+"\n")