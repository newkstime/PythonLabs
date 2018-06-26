from Problem1.dinner_combo import Dinner_combo
from Problem1.deluxe_dinner_combo import Deluxe_dinner_combo

def main():
    choose_dinner_type = input("For Dinner Combo, enter [1]. For Deluxe Dinner Combo, enter [2]: ")
    while choose_dinner_type != '1' and choose_dinner_type != '2':
        print("Invalid selection. Please try again.")
        choose_dinner_type = input("For Dinner Combo, enter [1]. For Deluxe Dinner Combo, enter [2]: ")
    if choose_dinner_type == '1':
        final_order = Dinner_combo()
        final_order.choose_main_dish()
        final_order.choose_soup()
        final_order.display_order()
    elif choose_dinner_type == '2':
        final_order = Deluxe_dinner_combo()
        final_order.choose_main_dish()
        final_order.choose_soup()
        final_order.choose_appetizer()
        final_order.display_order()

main()
