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
        file_name = input("Enter file name for delete: ").strip()
        if not file_name:
            print("Error! File name should not be empty.")
            return
        
        path = Path(file_name)
        
        if path.suffix == "":
            path = path.with_suffix(".txt")
        
        if not path.exists():
            print(f"Error! {[path]} file name has not exist.")
            return
        
        if not path.is_file():
            print(f"Errir! {path} file is not a file.")
            return
        
        item_found = False
        item_id = input("Enter item id for delete: ").strip()
        with open(path, 'r') as file:
            items = file.readlines()
            for index, line in enumerate(items):
                if not line.strip():
                    continue
                
                item = line.strip().split(",")
                if len(item)<5:
                    print("Sorry! invalid information.")
                    continue
                
                if item[0].strip() == item_id.strip():
                    item_found = True
                    items.pop(index)
                    break
        if item_found:
            with open(path, 'w') as  file:
                file.writelines(items)
            print("Item deleted successfully.")
            return
        else:
            print("Sorry! Item does not found.")
    except PermissionError:
        print("Error! You have no permission to delete item from menu.")
    except OSError as err:
        print(f"File system error! {err}")
    except Exception as err:
        print(f"Unexpected Error! {err}")
        

def create_customer_order():
    try: 
        file_name = input("Enter order file to create file: ").strip()
        if not file_name:
            print("Sorry! File name should not be empty.")
            return
        
        path = Path(file_name)
        
        if path.suffix == "":
            path = path.with_suffix(".txt")
        
        if path.exists():
            print(f"Sorry! {path} file name has already exist please change file name.")
            return
        
        
        with open(path, 'w') as file:
            pass

        print("Order file created successfully.")
        return
    
    except PermissionError:
        print("Error! you have no permission to create order file name.")
    except OSError as err:
        print(f"File System Error!: {err}")
        
    

def add_customer_order():
    menu_file_name = input("Enter menu item file name: ").strip()
    
    if not menu_file_name:
        print("Error! file name should not be empty.")
        return
    
    order_file_name = input("Enter order file name: ").strip()
    
    if not order_file_name:
        print("Sorry! File name should not be empty.")
        return
    
    
    path_menu = Path(menu_file_name)
    path_order = Path(order_file_name)
    
    if path_menu.suffix == "":
        path_menu = path_menu.with_suffix(".txt")
        
    
    if not path_menu.exists():
        print(f"Soory! {path_menu} file does not exist.")
        return
    
    if not path_menu.is_file():
        print(f"Sorry! {path_menu} file is not a file.")
        return
    
    if path_order.suffix == "":
        path_order = path_order.with_suffix(".txt")
            
        
    if not path_order.exists():
        print(f"Soory! {path_order} file does not exist.")
        return
        
    if not path_order.is_file():
        print(f"Sorry! {path_order} file is not a file.")
        return
    
    
    order_id = input("Enter order id: ").strip()
    if not order_id:
        print("Sorry! ID should not be empty.")
        return
    
    customer_name = input("Enter customer name: ").strip()
    if not customer_name:
        print("Sorry! Customer name should not empty.")
        return
    
    item_id = input("Enter item id: ").strip()
    if not item_id:
        print("Sorry! Item name should not be empty.")
        return
    
    try: 
        quentity = float(input("Enter quantity: ").strip())
        if quentity<1:
            print("Sorry! value must be in positive number.")
    except ValueError:
        print("Sorry! please enter valid number.")
        return
    try: 
        found = False
        with open (path_menu, 'r') as file:
            for line in file:
                if not line.strip():
                    continue
                
                info = line.strip().split(',')
                if info[0].strip()==item_id:
                    found = True
                    item_name = info[1].strip()
                    item_price = float(info[3].strip())
                    available_quantity = float(info[4].strip())
                    
                    if available_quantity>=quentity:
                        total_price = item_price*quentity
                        
                        order = (
                            f"{order_id}, {customer_name}, {item_id}, {item_name}, {quentity}, {item_price}, {total_price}\n"
                        )
                        
                        with open(path_order, 'a') as file:
                            file.write(order)
        if found:
            print("Order added successfully.")
            return
        else:
            print("Sorry! Order item does not exist.")
    except PermissionError:
        print("Error! You have no permission to add order.")
    except OSError as err:
        print(f"File system error! {err}")
    


def view_order():
    order_file_name = input("Enter order file name: ").strip()
    if not order_file_name:
        print("Sorry! file name should not be empty.")
        return
    
    path = Path(order_file_name)
    if path.suffix == "":
        path = path.with_suffix(".txt")
    
    if not path.exists():
        print(f"Error! {path} file name does not exist.")
        return
    
    if not path.is_file():
        print(f"Error! {path} file is not a file.")
        return
    
    try: 
        order_found = False
        order_id = input("Enter order id to view: ")
        with open(path, 'r') as file:
            for line in file:
                if not line.strip():
                    continue
                
                info = line.strip().split(",")
                
                if len(info)<7:
                    print("Sorry! invalid information.")
                    continue
                
                if info[0].strip() == order_id:
                    order_found = True
                    print("\nOrder Information")
                    print("=============================")
                    print(
                        f"Order ID: {info[0]}\n"
                        f"Customer Name: {info[1]}\n"
                        f"Item ID: {info[2]}\n"
                        f"Item Name: {info[3]}\n"
                        f"Order Quantity: {info[4]}\n"
                        f"Item Price: Rs.{info[5]}\n"   
                    )
                    print("==============================")
                    print(f"Total Price: {info[6]}\n")
        if order_found:
            print("Order shown successfully")
            return
        else:
            print("Sorry! Such order does not found.")
    except PermissionError:
        print("Error! You have no permission to search order.")
    except OSError as err:
        print(f"File System Error! {err}")  
            

def search_order():
    order_file_name = input("Enter order file name to search: ").strip()
    if not order_file_name:
        print("Sorry! File name should not be empty.")
        return
    
    path = Path(order_file_name)
    if path.suffix=="":
        path = path.with_suffix(".txt")
    
    if not path.exists():
        print(f"Sorry! {path} file name does not exist.")
        return
    
    if not path.is_file():
        print(f"Sorry! {path} file name is not a file.")
        return
    
    
    try:
        order_found = False
        order_id = input("Enter order id to search: ")
        with open(path, 'r') as file:
            for line in file:
                if not line.strip():
                    continue
                
                info = line.strip().split(",")
                if len(info)<7:
                    print("Sorry! Invalid information.")
                    continue
                
                if info[0].strip()==order_id:
                    order_found = True
                    print("\nOrder Information")
                    print("=============================")
                    print(
                        f"Order ID: {info[0]}\n"
                        f"Customer Name: {info[1]}\n"
                        f"Item ID: {info[2]}\n"
                        f"Item Name: {info[3]}\n"
                        f"Order Quantity: {info[4]}\n"
                        f"Item Price: Rs.{info[5]}\n"   
                    )
                    print("==============================")
                    print(f"Total Price: {info[6]}\n")
        if order_found:
            print("Order searched successfully.")
            return
        else:
            print("Sorry! Such order does not exist.")
            return
    except PermissionError:
        print("Error! You have no permission to search order.")
    except OSError as err:
        print(f"File System Error! {err}")
    
               
def update_order():
    order_file_name = input("Enter order file to update order: ").strip()
    if not order_file_name:
        print("Sorry! File name should not be empty.")
        return
    
    path_order = Path(order_file_name)
    if path_order.suffix=="":
        path_order = path_order.with_suffix(".txt")
    
    if not path_order.exists():
        print(f"Sorry! {path_order} file name does not exist.")
        return
    
    if not path_order.is_file():
        print(f"Sorry! {path_order} file name is not a file.")
        return
    
    item_file_name = input("Enter item file to update order: ").strip()
    if not item_file_name:
        print("Sorry! File name should not be empty.")
        return
    
    path_item = Path(item_file_name)
    
    if path_item.suffix=="":
        path_item = path_item.with_suffix(".txt")
    
    if not path_item.exists():
        print(f"Sorry! {path_item} file name does not exist.")
        return
    
    if not path_item.is_file():
        print(f"Sorry! {path_item} file name is not a file.")
        return
    
    try: 
        order_found = False
        order_id = input ("Enter order id for update order: ").strip()
        with open(path_order, 'r') as file:
            order_items = file.readlines()
            for index, line in enumerate(order_items):
                if not line.strip():
                    continue
                
                info = line.strip().split(",")
                
                if len(info)<7:
                    print("Sorry! Invalid informatin.")
                    continue
                
                if info[0].strip()==order_id:
                    order_found = True
                    
                    customer_name = input("Update customer name: ").strip()
                    if not customer_name:
                        print("\nSorry! Customer name should not be empty.")
                        return
                    
                    try: 
                        quantity = float(input("Update quantity: "))
                        if quantity<1:
                            print("\nSorry! Quantity should be in positive.")
                            return
                    except ValueError:
                        print("\nError! Please enter a valid quantity.")
                        return
                    
                    
                    
                    item_found = False
                    item_id = input("Enter item id for update: ").strip()
                    with open(path_item, 'r') as file:
                        for line in file:
                            if not line.strip():
                                continue
                            
                            info = line.strip().split(",")
                            
                            if len(info)<5:
                                print("Sorry! Invalid information.")
                                continue
                            
                            if info[0].strip()==item_id:
                                item_found = True
                                item_name = info[1].strip()
                                item_price = float(info[3].strip())
                                available_quantity = float(info[4].strip())
                                
                                
                                if available_quantity<quantity:
                                    print(f"\nSorry! only {available_quantity} items are available.")
                                    return
                                else:
                                    total_price = item_price*quantity
                                    
                                    
                                    order_items[index] = (
                                        f"{order_id}, {customer_name}, {item_id}, {item_name}, {quantity}, {item_price}, {total_price}\n"
                                    )
                                    
                    if item_found:
                        pass
                    else:
                        print("Error! Item id deos not found.")
                        return
        if order_found:
            with open(path_order, 'w') as file:
                file.writelines(order_items)
            print("Updated successfully.")
            return
        else: 
            print("Sorry! Such information does not exsit.")
    except PermissionError:
        print("Sorry! you do not have permission to update orders.")
    except OSError as err:
        print(f"File system error! {err}")
  
                
                
def delete_order():
    order_file = input("Enter order file to delete: ").strip()
    if not order_file:
        print("Sorry! order file should not empty.")
        return
    
    path = Path(order_file)
    if path.suffix=="":
        path = path.with_suffix(".txt")
    
    if not path.exists():
        print(f"Sorry! {path} file does not exsit.")
        return
    
    if not path.is_file():
        print(f"Sorry! {path} file is not a order file")
        return
    
    try:
        order_found = False
        order_id = input("Enter order id for delete: ")
        
        with open(path, 'r') as file:
            order_items = file.readlines()
            for index, line in enumerate(order_items):
                if not line.strip():
                    continue
                
                info = line.strip().split(",")
                
                if len(info)<7:
                    print("Sorry! invalid information.")
                    continue
                
                if info[0].strip()==order_id:
                    order_found = True
                    order_items.pop(index)
                    break
        if order_found:
            with open(path, 'w') as file:
                file.writelines(order_items)
            print("Delete successfully.")
            return
        else:
            print("Sorry! Such information has not found.")
    except PermissionError:
        print("Sorry! you have no permission to delete order items.")
    except OSError as err:
        print(f"File system error! {err}")
        
            


def cafe_summary():
    item_file_name = input("Enter menu file name: ").strip()
    if not item_file_name:
        print("Sorry! File name should not be empty.")
        return
    
    count_item = 0
    
    item_path = Path(item_file_name)
    if item_path.suffix == "":
        item_path = item_path.with_suffix(".txt")
    
    if not item_path.exists():
        print(f"Sorry! {item_path} file does not exist.")
        return
    
    if not item_path.is_file():
        print(f"Sorry! {item_path} file is not a file.")
        return
    
    order_file_item = input("Enter order file: ").strip()
    if not order_file_item:
        print("Sorry! file name should not be empty.")
        return
    
    count_order = 0
    order_path = Path(order_file_item)
    
    if order_path.suffix=="":
        order_path = order_path.with_suffix(".txt")
    
    if not order_path.exists():
        print(f"Sorry! {order_path} file does not exist.")
        return
    
    if not order_path.is_file():
        print(f"Sorry! {order_path} file is not a file.")
        return
    
    try: 
        with open(item_path, 'r') as file:
            for line in file:
                if line:
                    count_item+=1
                    continue
    
        with open(order_path, 'r') as file:
            for line in file:
                if line:
                    count_order+=1
                    continue

    
        print("\nCafe Summery:")
        print("================================")
        print(
            f"Total Items = {count_item}\n"
            f"Total Orders = {count_order}"
        )
    except PermissionError:
        print("Sorry! you have no permission.")
    except OSError as err:
        print(f"File System error! {err}")
    except Exception as err:
        print(f"\nUnexpected error! {err}")
        
    
    

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
    
