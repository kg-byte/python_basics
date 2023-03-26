my_list = range(1, 5)
try:
    fourth_item = my_list[4]
except KeyError as err:
    print("An error occured when accessing the items in `my_list`")
finally:
    print("Finished accessing `my_list`")
