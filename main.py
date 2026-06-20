from ac_logic import AC_automation


def set_temp():
   while True: 
    set_temp = input("Please enter desired temperature: ") 
    try: 
        set_temp_float = float(set_temp) 
        print ("Your desired temperature is:", set_temp, "celsius")
        return set_temp_float 

        break  

    except ValueError:
        print("Please enter a number") 

def current_temp():
   while True: 
    current_temp = input("Please enter current temperature: ") 
    try: 
        temp_float = float(current_temp) 
        print ("The current temperature is:", current_temp, "celsius")
        return temp_float 

        break  

    except ValueError:
        print("Please enter a numbers") 

if __name__ == "__main__":
 temp_float = current_temp()

if __name__ == "__main__":
 set_temp_float = set_temp()

AC_automation(temp_float, set_temp_float)