#!/usr/bin/python3

# list_division : division two integer
# my_list_1 : first number
# my_list_2 : second number
# list_length : third number
# Return : integer or error

def list_division(my_list_1, my_list_2, list_length):
    list_1 = []
    answer = 0
    for num in range(0, list_length):
        try:
            answer = my_list_1[num] / my_list_2[num]
        except TypeError:
            print("wrong type")
            answer = 0
        except ZeroDivisionError:
            print("division by 0")
            answer = 0
        except IndexError:
            print("out of range")
            answer = 0
        finally:
            list_1.append(answer)
    return (list_1)
