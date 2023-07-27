Input = [12, 35, 9, 56, 24]
one_element = Input[:-1]
print(one_element)

sec_element = Input[-1]
print(sec_element)

Input.pop(0)
Input.insert(0, sec_element)
print(Input)

Input.pop(-1)
Input.append(one_element)
print(Input)
