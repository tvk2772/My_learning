""" Create my friends list as vocabulary
key = surname
information = tuple(name,birthday,living city, living country)"""

friend_list = {}

def create_new_friend():
    
    name = input("Your friend's name: ")
    
    if name == '':
        return None
    
    surname = input("Your friend's surname: ")
    birthday = input("Your friend's birthday: ")
    
    new_friend = (name,birthday)
    
    return surname,new_friend
    
def add_new_friend(friend_list):
    
    while True:
        res = create_new_friend()
        if res == None:
            break
        else:
            friend_list[res[0]]=res[1]
            
## if __name__ == '__main__':
add_new_friend(friend_list)
print(friend_list)