def AC_automation(temp_float, set_temp=22):
    if temp_float > set_temp + 2: 
     message = "Cool air ON"
     AC_on = True
    elif temp_float < set_temp - 2:
      message = "Heat ON"
      Heat_on = True
    else:
      message = "Air stable"

    print(message)
    return message