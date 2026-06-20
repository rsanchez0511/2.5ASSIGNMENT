def AC_automation(temp_float, set_temp_float):
    if temp_float > set_temp_float + 2:
        message = "Cool air ON"
        AC_on = True
    elif temp_float < set_temp_float - 2:
        message = "Heat ON"
        Heat_on = True
    else:
        message = "Air stable"

    print(message)
    return message