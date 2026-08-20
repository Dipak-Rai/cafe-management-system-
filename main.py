from pathlib import Path
import os


def create_file():
    try:
        file_name = input("Enter file name: ")
        path = Path(file_name)
        
        if not os.path.exists(path):
            with open(path, 'w') as file:
                pass
            print("Thank you! File has created successfully.")
            
        else:
            print("Sorry! Such file has already exist.")
    except Exception as err:
        print(f"Error! something went wrong. {err}")

def add_menu_item():
    try:
        file_name = input("Please enter file name where do yo want to kept menu: ")
        path = Path(file_name)
        
        if os.path.exists(path):
            item_id = input("Enter item id: ").strip()
            item_name = input("Enter item name: ").strip()
            category = input("Enter item category: ").strip()
            price = input("Enter item price: ").strip()
            available_quantity = input("Enter item quantity: ").strip()
            
            menu_item = (
                f"\n{item_id}, {item_name}, {category}, {price}, {available_quantity}"
            )
            with open(path, 'a') as file:
                file.write(menu_item)     
            print("\n Menu added successfully.")
            
        else:
            print("Sorry! Such file has not exit")
    except Exception as err:
        print(f"Error! Someting went wrong. {err}")

def view_menu_item():
    try:
        file_name = input("Enter file name which do you want to view: ")
        path = Path(file_name)
        
        if os.path.exists(path):
            with open(path, 'r') as file:
                for line in file:
                    info = line.strip().split()
                    print("====================")
                    print("CAFE MENU")
                    print("====================")
                    print(
                        f"\nItem ID : {info[0]}\n"
                        f"Item Name : {info[1]}\n"
                        f"Item Category : {info[2]}\n"
                        f"Item Price : {info[3]}\n"
                        f"Item quentity : {info[4]}"
                    )
            print("\n View Data Seccessfully")
            
        else:
            print("Sorry! Such file has not exist.")
    except Exception as err:
        print(f"Error! Someting went wrong. {err}")

def search_menu_item():
    try:
        file_name = input("Enter file name to search item: ")
        path = Path(file_name)
        
        if not os.path.exists(path):
            print("Sorry such file  does not exist.")
        else:
            menu_id = input("Enter ID for search menu item: ")
            found = False
            with open(path, 'r') as file:
                for line in file:
                    info = line.strip().split(',')
                    
                    if info[0].strip()==menu_id.strip():
                        print("====================")
                        print(f"{info[1]} Item")
                        print("====================") 
                        print(             
                            f"\nItem ID : {info[0]}\n"
                            f"Item Name : {info[1]}\n"
                            f"Item Category : {info[2]}\n"
                            f"Item Price : {info[3]}\n"
                            f"Item quentity : {info[4]}"
                        )
                        print("\n Menu item has been found successfully.")
                        found = True
            if not found:
                print("Sorry! Such item does not found in cafe menu.")
    except Exception as err:
        print(f"Sorry! Someting wrong {err}")

def update_menu_item():
    try:
        file_name = input("Enter file name: ")
        item_id = input("Enter item ID to update: ").strip()
        path = Path(file_name)
        if os.path.exists(path):
            with open(path, 'r') as file:
                items = file.readlines()
                
            found = False
            for index, line in enumerate(items):
                item = line.strip().split(',')
                
                if item[0].strip() == item_id.strip():
                    print("\nCurrent Menu Item")
                    print("======================")
                    print(f"Item ID    : {item[0]}")
                    print(f"Item Name  : {item[1]}")
                    print(f"Category   : {item[2]}")
                    print(f"Price      : Rs. {item[3]}")
                    print(f"Quantity   : {item[4]}")

                    print("\nEnter New Information")

                    item_name = input("Enter Item Name: ").strip()
                    category = input("Enter Category: ").strip()
                    price = input("Enter Price: ").strip()
                    quantity = input("Enter Quantity: ").strip()

                    items[index] = (
                        f"{item_id},{item_name},{category},"
                        f"{price},{quantity}\n"
                    )
                    found =True
                    break
            if found:
                with open(path, 'w') as file:
                    file.writelines(items)
                print("\n Menu item updated successfully.")
            else:
                print("Sorry! Such item ID has not found.")
        else:
            print("Sorry! Such file does not exist.")
    except Exception as err:
        print(f"Sorry! Something wrong. {err}")

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
    
