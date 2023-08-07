snack_inventory =[]



def add_snack():
    name = input("Enter snack name: ")
    Id = input("Enter snack id: ")
    price = int(input("Enter snack price: "))

    obj ={
        "Name":name,
        "ID":Id,
        "Price":price
    }

    for i in snack_inventory:
        if i["ID"] == Id:
            print("Id is already  exists")
            return
        
    snack_inventory.append(obj)
    print("Item added successfully")


def remove_snack():
    Id = input("Enter snack id: ")

    for i in snack_inventory:
        if i["ID"] == Id:
            snack_inventory.remove(i)
            print("item removed successfully")
            return 


    print("Item note found") 
    return 



def update_snack ():
    Id =input ("Enter snack id: ")
    new_price = int(input("Enter snack new price: "))
    for i in snack_inventory :
        if i["ID"] == Id:
            if i["Id"]== Id:
                i["Price"] = new_price
                print("Item Updated successfully")
                return 
            

    print ("Item not found")    
    return 


def record_sale() :
    print(snack_inventory)



while True :
    print("Welcome to Mumbai Munchies!")
    print("Please choose one of the following options:")
    print("1. Add Snack")
    print("2. Remove snack")
    print("3. update Snack availability")
    print("4. Record Sale")
    print("5. Exit")

    choice = int(input("choose your input: "))

    if choice == 1:
        add_snack()

    elif choice == 2:
        remove_snack()

    elif choice == 3:
       update_snack()

    elif choice == 4:
        record_sale()

    elif choice == 5:
        print("you have successfully quit ")
        break;
    
    else:
        print("Invaild input try again ")
        continue
    
