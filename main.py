from pathlib import Path
import os


def create_file():
    try:
        file_name = input("Enter cafe menu file name to create: ")
        #check file name is empty:
        if not file_name:
            print("Error! File name should not empty.")
            return
        
        path = Path(file_name)
        # auto extension for file ".txt"
        if path.suffix=="":
            path = path.with_suffix(".txt")
        
        #check if path exist:  
        if path.exists():
            print("Error! This file has already exist.")
            return
        
        if not path.exists():
            with open(path, 'w') as file:
                pass
    except PermissionError:
        print("\nError! You have no permission to create cafe file.")
    except OSError as err:
        print(f"\nError! File system error.{err}")
    except Exception as err:
        print(f"\nUnexpected error!.{err}")
        
 
def add_menu_item():
    file_name = input("Enter file name to add menu: ").strip()
    # check file name is empty
    if not file_name:
        print("\nError! File name should not be empty.")
        return
    
    path = Path(file_name)
    
    #Add .txt extension autometically:
    if path.suffix=="":
        path = path.with_suffix(".txt")
    
    #check if not file name exsit:
    if not path.exists():
        print(f"\nError {path} file is not exist.")
        return
    
    if not path.is_file():
        print(f"\nError! {path} file is not a file.")
        return
    
    try:
        path_found = False
        item_id = input("Enter menu id: ").strip()
        with open(path, 'r') as file:
            for line in file:
                #Check if line is empty
                if not line.strip():
                    continue
                
                info = line.strip().split(',')
                if info[0].strip()==item_id.strip():
                    path_found = True
                    break
        if path_found:
            print("\nSorry! menu id is already exsit.")
            return
        else:
            pass
        
        item_name = input("Enter item name: ").strip()
        if not item_name:
            print("\nError! item name should not be empty.")
            return
        
        item_catagory = input("Enter item catagory: ")
        if not item_catagory:
            print("\nError! catagory name should not be empty.")
            return
        
        
        
        item_price = float(input("Enter item price: ").strip())
        try:
            if not item_price:
                print("\nError! item price should not be empty.")
                return
            if item_price<0:
                print("\Sorry! Price must be in positive number.")
                return
        except ValueError as err:
            print(f"\nSorry! enter valid item price.{err}")
            return
        
        item_quentity = float(input("Enter item quentity: ").strip())
        try:
            if not item_quentity:
                print("\nError! item quentity should not be empty.")
                return
            if item_quentity<0:
                print("\Sorry! quentity must be in positive number.")
                return
        except ValueError as err:
            print(f"\nSorry! enter valid item quentity.{err}")
            return
        
        items_info = (
            f"{item_id}, {item_name}, {item_catagory}, {item_price}, {item_quentity}\n"
        )
        
        with open (path, 'a') as file:
            file.write(items_info)
        print("\n Item added Successfully.")
        return
    
    except PermissionError:
        print("\nError! you are not allow to add item.")
    except OSError as err:
        print(f"Eorror! File system error. {err}")
        
          

def view_menu_item():
    try:
        file_name = input("Enter item file name to view: ").strip()
        if not file_name:
            print("Error! File name should not be empty.")
            return
        
        path = Path(file_name)
        
        if path.suffix=="":
            path = path.with_suffix(".txt")
        
        if not path.exists():
            print(f"Error! {path} file name has not exist.")
            return
        
        if not path.is_file():
            print(f"\nError! {path} file is not a file")
            return
        
        with open(path, 'r') as file:
            for line in file:
                if not line.strip():
                    continue
                
                info = line.strip().split(',')
                if len(info)<5:
                    print("\nSorry! Not foud such information.")
                    return
                print("\nItem Information:")
                print("=======================")
                print(
                    f"Item Id           : {info[0]}\n"
                    f"Item Name         : {info[1]}\n"
                    f"Item Catagory     : {info[2]}\n"
                    f"Item Price        : Rs.{float(info[3]):.2f}\n"
                    f"Item Quantity     : {info[4]}"
                )
                
        print("\nItems show successfully.")
    except PermissionError:
        print("\nError! You have no permission to view data.")
    except OSError:
        print("\nFile System Error!")
        
        
    
 
 

def search_menu_item():
    file_name = input("Enter file name: ").strip()
    if not file_name:
        print("\nError! File name should not be empty.")
        return
    
    path = Path(file_name)
    
    if path.suffix == "":
        path = path.with_suffix(".txt")
    
    if not path.exists():
        print(f"\nError! {path} file does not exist.")
        return
    
    if not path.is_file():
        print(f"\nError! {path} file is not a file.")
        return
    try:
        path_found = False
        item_id = input("Enter item id: ").strip()
        with open(path, 'r') as file:
            for line in file:
                if not line.strip():
                    continue
                
                info = line.strip().split(',')
                if len(info)<5:
                    print("\nSorry! Invalid information.")
                    continue
                
                if info[0].strip()==item_id.strip():
                    path_found = True
                    print("\nItem Information:")
                    print("=======================")
                    print(
                        f"Item Id           : {info[0]}\n"
                        f"Item Name         : {info[1]}\n"
                        f"Item Catagory     : {info[2]}\n"
                        f"Item Price        : Rs.{float(info[3]):.2f}\n"
                        f"Item Quantity     : {info[4]}"
                    )
                    break
        if path_found:
            print("\nItem data showed seccessfully.")
            return
        else:
            print("\nSorry! Such item doest not exist.")
    except PermissionError:
        print("\nError! You have no permission to search item.")
    except OSError as err:
        print(f"\nFile System Error!!. {err}")
            

def update_menu_item():
    file_name = input("Enter file name: ").strip()
    if not file_name:
        print("\nError! File name should not be empty.")
        return
    
    path = Path(file_name)
    if path.suffix == "":
        path = path.with_suffix(".txt")
    
    if not path.exists():
        print(f"\nError! {path} file does not exist.")
        return
    
    if not path.is_file():
        print(f"\nError! {path} file is not a file.")
        return
    try:
        item_found = False
        item_id = input("Enter item id for update: ").strip()
        with open(path, 'r') as file:
            items = file.readlines()
            for index, line in enumerate(items):
                if not line.strip():
                    continue
                
                item = line.strip().split(",")
                if len(item)<5:
                    print("\nError! Invalid Information.")
                    continue
                
                if item[0].strip()==item_id.strip():
                    item_found = True
                    print("\nItem Information:")
                    print("=======================")
                    print(
                        f"Item Id           : {item[0]}\n"
                        f"Item Name         : {item[1]}\n"
                        f"Item Catagory     : {item[2]}\n"
                        f"Item Price        : Rs.{float(item[3]):.2f}\n"
                        f"Item Quantity     : {item[4]}"
                    )
                    
                    print("\n Update item")
                    update_item_name = input("Update item name: ").strip()
                    if not update_item_name:
                        print("\nError! Item name should not be empty.")
                        return
                    
                    update_item_catagory = input("Update item catagory: ").strip()
                    if not update_item_catagory:
                        print("\nError! Item catagory should not be empty.")
                        return
                    
                    try:
                        update_item_price = float(input("Update item price: ").strip())
                    
                        if update_item_price<=0:
                            print("\nError! Item price should not be negative number")
                            return
                    except ValueError:
                        print("\nError! Please enter valid number.")
                        return
                        
                    try:
                        update_item_quantity = int(input("Update item quantity: ").strip())
                    
                        if update_item_quantity<=0:
                            print("\nError! Quantity should not be in negative number.")
                            return
                    except ValueError:
                        print("\nError! Please enter valid quantity.")
                        return
                    
                    items[index] = (
                        f"{item[0].strip()}, {update_item_name}, {update_item_catagory}, {update_item_price}, {update_item_quantity}\n"
                    )
        if item_found:
            with open(path, 'w') as file:
                file.writelines(items)
            print("\nUpdate item successfully.")
        else:
            print("\nError! Shuch information does not  exist.")
    except PermissionError:
        print("\nError! You have not permission to update item.")
    except OSError as err:
        print(f"\nFile System Error! {err}")
        
                
def delete_menu_item():
    try:
        file_name = input("Enter file name: ")
        item_id = input("Enter item id for delete: ").strip()
        path = Path(file_name)
        
        if os.path.exists(path):
            with open(path, 'r') as file:
                items = file.readlines()
            
            found = False
            for index, line in enumerate(items):
                item = line.strip().split(',')
                
                if item[0].strip() == item_id.strip():
                    print("\nMenu Item Found")
                    print("======================")
                    print(f"Item ID    : {item[0]}")
                    print(f"Item Name  : {item[1]}")
                    print(f"Category   : {item[2]}")
                    print(f"Price      : Rs. {item[3]}")
                    print(f"Quantity   : {item[4]}")
                    
                    found = True
                    items.pop(index)
                    break
            if found:
                with open(path, 'w') as file:
                    file.writelines(items)
                print("\n Menu item deleted successfully.")
            else:
                print("Sorry! Such item ID does not found.")  
        else:
            print("Sorry! Such file does not exist.")
    except Exception as err:
        print(f"Sorry! Something wrong! {err}")

def create_customer_order():
    try:
        file_name = input("Enter file name to create customer order: ")
        path = Path(file_name)
        
        if not os.path.exists(path):
            with open(path, 'w') as file:
                pass
        else:
            print("Sorry! Such file has already exist")
    except Exception as err:
        print(f"Sorry! Something Wrong. {err}")

def add_customer_order():
    try:
        menu_file = input("Enter menu file name: ")
        order_file = input("Enter order file name: ")
        
        path_menu_file = Path(menu_file)
        path_order_file = Path(order_file)
        
        if os.path.exists(path_menu_file):
            order_id = input("Enter order ID: ").strip()
            customer_name = input("Enter customer name: ").strip()
            item_id = input("Enter item ID: ").strip()
            quantity = int(input("Enter quantity: ").strip())
            
            found = False
            with open(path_menu_file, 'r') as file:
                menu_items = file.readlines()
                
            for line in menu_items:
                item = line.strip().split(',')
                
                if item[0]==item_id:
                    found = True
                    item_name = item[1].strip()
                    price = int(item[3].strip())
                    available_quantity = int(item[4].strip())
                    
                    if quantity<=available_quantity:
                        total = price * quantity
                        
                        order = (
                            f"\n{order_id}, {customer_name}, {item_id}, {quantity}, {price}, {total}"
                        )
                        
                        with open(path_order_file, 'a') as file:
                            file.write(order)
                        print("\n Customer Order")
                        print("===================")
                        print(f"Order ID: {order_id}\n")
                        print(f"Customer Name: {customer_name}\n")
                        print(f"Item: {item_name}\n")
                        print(f"Quantity : {quantity}\n")
                        print(f"Price : Rs. {price}\n")
                        print(f"Total Price: Rs. {total}")
                        print("\n Order has created successfully.")
                        
                    else:
                        print("Sorry! Not enough quantity")
                    break
            if not found:
                print("Sorry! Item ID does not exist")
        else:
            print("Sorry! Such file does not exist.")
    except Exception as err:
        print(f"Sorry! Something Wrong. {err}")

def view_order():
    try:
        order_file = input("Enter order file name: ").strip()
        path = Path(order_file)

        if os.path.exists(path):

            with open(path, 'r') as file:
                items = file.readlines()

            for line in items:

                if not line.strip():
                    continue

                item = line.strip().split(',')

                if len(item) == 6:

                    print("\n** Customer Order **")
                    print("---------------------------")
                    print(
                        f"Order ID      : {item[0]}\n"
                        f"Customer Name : {item[1]}\n"
                        f"Item          : {item[2]}\n"
                        f"Quantity      : {item[3]}\n"
                        f"Price         : Rs. {item[4]}\n"
                        f"Total Price   : Rs. {item[5]}"
                    )

                else:
                    print("Invalid order information.")

        else:
            print("Sorry! Such file does not exist.")
    except Exception as err:
        print(f"Sorry! Something Wrong. {err}")
            

def search_order():
    try:
        order_file = input("Enter file name: ").strip()
        path = Path(order_file)
        
        if os.path.exists(path):
            order_id = input("Enter order id: ").strip()
            
            found = False
            with open(path, 'r') as file:
                order_items = file.readlines()
            for line in order_items:
                item = line.strip().split(',')
                
                if item[0].strip()==order_id:
                    found = True
                    print("\n Order Information")
                    print("=========================")
                    print(f"Order ID: {item[0]}\n")
                    print(f"Customer Name: {item[1]}\n")
                    print(f"Item: {item[2]}\n")
                    print(f"Quantity : {item[3]}\n")
                    print(f"Price : Rs. {item[4]}\n")
                    print(f"Total Price: Rs. {item[5]}")
            if not found:
                print("Sorry! order id doest no match.")
                
        else:
            print("Sorry! This file does not exit.")
    except Exception as err:
        print(f"Sorry! Something Wrong. {err}")
                    
def update_order():
    try:
        order_file = input("Enter order file name for update: ")
        path = Path(order_file)
        if os.path.exists(path):
            order_id = input("Enter order ID for update: ").strip()
            found = False
            with open(path, 'r') as file:
                order_items = file.readlines()
            for index, line in enumerate(order_items):
                item = line.strip().split(',')
                
                if item[0].strip()==order_id:
                    found = True
                    print("\n Current Customer Order")
                    print("=============================")
                    print(
                        f"Order ID : {item[0]}\n"
                        f"Customer Name : {item[1]}\n"
                        f"Item ID : {item[2]}\n"
                        f"Quantity : {item[3]}\n"
                        f"Price : {item[4]}\n"
                        f"Total Price : {item[5]}"              
                    )
                    
                    print("\n Update Customer Order")
                    print("============================")
                    customer_name = input("Update customer name: ")
                    item_id = input("Update item ID: ")
                    quantity = int(input("Update quantity: "))
                    price = int(item[4].strip())
                    
                    total = price*quantity
                    
                    order_items[index] = (
                        f"{order_id}, {customer_name}, {item_id}, {quantity}, {price}, {total}\n"
                    )
                    break
            if found:
                with open(path, 'w') as file: 
                    file.writelines(order_items)
                print("\n Order Item Updated Successfully.")
                    
            else:
                print("Sorry! Such id has not exist")
        
        else:
            print("Sorry! This file does not exist.")
    except Exception as err:
        print(f'Sorry! Something Worng. {err}')
                
                
def delete_order():
    order_file = input("Enter order file for delete: ").strip()
    path = Path(order_file)
    
    if os.path.exists(path):
        found = False
        order_id = input("Enter order id for delete order item: ").strip()
        
        with open (path, 'r') as file:
            order_items = file.readlines()
            
            for index, line in enumerate(order_items):
                info = line.strip().split(',')
                
                if info and info[0].strip()==order_id:
                    found =True
                    order_items.pop(index)
                    break
        if found:
            with open(path, 'w') as file:
                file.writelines(order_items)
            print("Order item deleted successfully.")
        else:
            print("Sorry! such order ID does not exist")
    else:
        print("Sorry! Such file does not exist: ")


def cafe_summary():
    cafe_menu = input("Enter cafe menu file name: ").strip()
    customer_order = input("Enter customer order file name: ").strip()
    
    path_cafe = Path(cafe_menu)
    path_customer = Path(customer_order)
    
    menu_count = 0
    customer_order_coun = 0
    
    if path_cafe.is_file():
        with open(path_cafe, 'r') as file:
            for line in file:
                if line.strip():
                    menu_count+=1           
                
    else:
        print("Sorry! Such file does not exist: ")
    
    if path_customer.is_file():
            with open(path_customer, 'r') as file:
                for line in file:
                    if line.strip():
                        customer_order_coun+=1           
                    
    else:
        print("Sorry! Such file does not exist: ")
    
    print("\n ============= Hotel Summery ===============")
    print(f"Total menu items: {menu_count}")
    print(f"Total customer order items: {customer_order_coun}")
    
    

while True:
    print("\n Cafe Management System:")
    print("=============================")
    print("1. Create File")
    print("2. Add Menu Item")
    print("3. View Menu")
    print("4. Search Menu Item")
    print("5. Update Menu Item")
    print("6. Delete Menu Item")
    
    print("7. Create Customer Order")
    print("8. Add Customer Order")
    print("9. View Orders")
    print("10. Search Order")
    print("11. Update Order")
    print("12. Delete Order")
    
    print("13. Cafe Summary")
    print("14. Exit")
    
    
    choice = int(input("Please enter number what you want to do: "))
    
    if choice == 1:
        create_file()
        
    elif choice == 2:
        add_menu_item()
    
    elif choice == 3:
        view_menu_item()
        
    elif choice == 4:
        search_menu_item()
            
    elif choice == 5:
        update_menu_item()
    
    elif choice == 6:
        delete_menu_item()
    
    
    elif choice == 7:
        create_customer_order()
            
    elif choice == 8:
        add_customer_order()
    
    elif choice == 9:
        view_order()
    
    elif choice == 10:
        search_order()
    
    elif choice == 11:
        update_order()
    
    elif choice == 12:
        delete_order()
    
    elif choice == 13:
        cafe_summary()
    
    elif choice == 13:
        print("Thak you! give me opportunity to service.")
        break
    
    
    else: 
        print("Sorry! please enter valid number")
    
