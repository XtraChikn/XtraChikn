
from tkinter import Y
from Node import Node
from LinkedList import LinkedList
from data import *
from welcome import *

welcome_to()

def insert_menus():
    menu_list = LinkedList()
    for menu in menus:
        menu_list.insert_beginning(menu)
    return menu_list

def insert_meal_data():
    meal_data_list = LinkedList()
    for menu in menus:
        meal_sublist = LinkedList()
        for meal in meal_data:
            if meal[0] == menu:
                meal_sublist.insert_beginning(meal)
        meal_data_list.insert_beginning(meal_sublist)
    return meal_data_list


my_menu_list = insert_menus()
my_meal_list = insert_meal_data()

selected_menu = ""

while len(selected_menu) == 0:
    user_input = str(input(
        "\nWhat menu would you like to look at?\nType the beginning few letters of that menu and press enter to see if "
        "we have one.\n")).lower()

    matching_types = []
    type_list_head = my_menu_list.get_head_node()
    while type_list_head is not None:
        if str(type_list_head.get_value()).startswith(user_input):
            matching_types.append(type_list_head.get_value())
        type_list_head = type_list_head.get_next_node()

    for food in matching_types:
        print(food)

    if len(matching_types) == 1:
        select_type = str(input(
            "\nThe only menu for what you entered is " + matching_types[0] + ". \nDo you want to look at " +
            matching_types[0] + " meals? Type y for yes and n for no\n")).lower()


        if select_type == 'y':
            selected_menu = matching_types[0]
            print("Selected Menu: " + selected_menu)
            meal_list_head = my_meal_list.get_head_node()
            while meal_list_head.get_next_node() is not None:
                sublist_head = meal_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_menu:
                    while sublist_head.get_next_node() is not None:
                        print("--------------------------")
                        print("Main Ingredient: " + sublist_head.get_value()[1])
                        print("Name of Dish: " + sublist_head.get_value()[2])
                        print("Price: $" + sublist_head.get_value()[3])
                        print("Rating: " + str(sublist_head.get_value()[4]) + "/5")
                        print("--------------------------\n")
                        sublist_head = sublist_head.get_next_node()
                meal_list_head = meal_list_head.get_next_node()

            repeat_loop = str(input("\nWould you like to look at any other menu? Type y for yes and n for no.\n")).lower()
            if repeat_loop == 'y':
                selected_menu = ""
            elif repeat_loop == 'n':
                goodbye()
                repeat_loop = str(input()).lower()
            
        