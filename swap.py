#Python – Swap elements in String list

main_list = ['gfg', 'is', 'best', 'for', 'world']
print("gfg', 'is', 'best', 'for', 'world: " + str(main_list))

first_element = main_list[0]
print(first_element)

last_element = main_list[-1]
print(last_element)

main_list.pop(0)
print(main_list)

main_list.pop()
print(main_list)

 main_list.insert(0, last_element)
 print(main_list)

 main_list.append(first_element)
 print(main_list)