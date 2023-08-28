def safe_print_list(my_list=[], x=0):
    '''Function that prints x elements of a list'''

    for i in range(x):
        try:
            print(f"{my_list[i]}", end='')
        except:
            break
    print()
    return (i)
