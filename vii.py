#let temp = temperature, conv = convertion
print("ctrl+z to exit program")
get_temp_value = float(input("Insert the temperature value: "))
get_conv_form = int(input("Insert conversion form\n1- from Centigrade to Fahrenheit\n2-From Fahrenheit to Centigrade\n: "))

if get_conv_form == 1 or get_conv_form == 2:
    if get_conv_form == 1:
        #let cent = centigrade, fah = fahrenheit.
        cent_to_fah = (get_temp_value * 9/5) + 32
        print(f"{cent_to_fah}°F")
    elif get_conv_form == 2:
        fah_to_cent = (get_temp_value - 32)*5/9
        print(f"{fah_to_cent}°C")
    else:
        print("Invalid Entry")
elif get_conv_form != 1 or get_conv_form != 2:
    print("Invalid Entry")
print("done")