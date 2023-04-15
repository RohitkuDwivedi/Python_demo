# take input from user and filter small case charecters from it:

user_input = 'rohit deepak archana'
char_dict:dict = {} # annotation


# loop on string and check case
for val in user_input:
    if val.islower():
        val_ocurance = user_input.count(val)
        # we have lower case char val and is count val_ocurance
        # DICT[KEY] = VALUE
        char_dict[val]=val_ocurance
    else:
        pass # false block
print(char_dict)

#loop on dict and get key and val
for key,val in char_dict.items(): # dict.keys() dict[key]
    print(f'{key}:{val}')


#loop on dict and get key
for key in char_dict.keys(): # dict.keys() dict[key]
    print(f'{key}:{char_dict[key]}')


