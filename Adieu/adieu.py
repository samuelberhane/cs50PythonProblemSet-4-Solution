name_list = []
while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        print()
        break

final_string = "Adieu, adieu, to "
if len(name_list) == 1:
    for i in range(len(name_list)):
        final_string += name_list[i]
elif len(name_list) == 2:
    for i in range(len(name_list)):
        if i == 1:
            final_string += name_list[1]
        else:
            final_string += name_list[i] + " and "
else:
    for i in range(len(name_list)):
        if i == len(name_list) - 1:
            final_string += "and " + name_list[i]
        else:
            final_string += name_list[i] + ", "


print(final_string)