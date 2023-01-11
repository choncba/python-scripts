#%%
users_form = [  ('id', '1'), ('username', 'lbono'), ('is_active', 'on'), ('is_verified', 'on'), ('is_superuser', 'on'), 
                ('id', '2'), ('username', 'choncba'), 
                ('id', '3'), ('username', 'pepe')
            ]

def getMultipartForm(form_list, param):

    users = []
    for i, item in enumerate(form_list):
        if item[0] == param:                            # Detecto el primer key
            user_entry = {item[0]:item[1]}              # Genero un dict desde este key
            del form_list[i]                            # Saco la tupla de la lista para seguir iterando
            for user_item in form_list:                 # Sigo iterando hasta volver a encontrar el parametro
                if user_item[0] == param: break         # Si lo encuentra, interrumpe
                else:   user_entry.update({user_item[0]:user_item[1]})
            users.append(user_entry)                    # Agrego el dict a la lista

    return users

users_list = getMultipartForm(users_form,"id")
print( users_list)

# %%
users_form = [  ('id', '1'), ('username', 'lbono'), ('is_active', 'on'), ('is_verified', 'on'), ('is_superuser', 'on'), 
                ('id', '2'), ('username', 'choncba'), 
                ('id', '3'), ('username', 'pepe')
            ]

def find_indices(list_to_check, item_to_find):
    return [idx for idx, value in enumerate(list_to_check) if value[0] == item_to_find]

indices_id = find_indices(users_form, "id")
user1 = users_form[0:5]
user2 = users_form[5:7]
user3 = users_form[7:len(users_form)]
print(indices_id)
print(user1)
print(user2)
print(user3)

users_list = []
for num_user in range(len(indices_id)):
    start = indices_id[num_user]
    stop = indices_id[num_user+1] if num_user+1 < len(indices_id) else len(users_form)
    user = users_form[start:stop]    
    users_list.append(user)
    print(user)

print(users_list)

users_dict = []
for usr in users_list:
    user_entry = {}
    for item in usr:
        user_entry.update({item[0]:item[1]})
    users_dict.append(user_entry)

print(users_dict)    
# %%
users_form = [  ('id', '1'), ('username', 'lbono'), ('is_active', 'on'), ('is_verified', 'on'), ('is_superuser', 'on'), 
                ('id', '2'), ('username', 'choncba'), 
                ('id', '3'), ('username', 'pepe')
            ]

def getMultipartForm(form_list, item_to_find):

    indices_id = [idx for idx, value in enumerate(form_list) if value[0] == item_to_find]
    num_users = len(indices_id)

    users_list = []
    for num_user in range(num_users):
        start = indices_id[num_user]
        stop = indices_id[num_user+1] if num_user+1 < len(indices_id) else len(form_list)
        usr = form_list[start:stop]
        user_entry = {}
        for item in usr:
            user_entry.update({item[0]:item[1]})
        users_list.append(user_entry)

    return users_list

print(getMultipartForm(users_form, "id"))




# %%
