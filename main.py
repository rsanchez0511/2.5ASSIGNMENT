from ac_logic import AC_automation

set_temp = 22

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

AC_automation(temp_float, set_temp==22)