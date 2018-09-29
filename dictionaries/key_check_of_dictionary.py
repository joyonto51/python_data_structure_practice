my_dict ={1: 2, 2:3, 3:1, 4:5, 5:0}

def check_key(key):
    if key in my_dict:
        print("the key already exist.")
    else:
        print("the key is not exist.")

check_key(8)