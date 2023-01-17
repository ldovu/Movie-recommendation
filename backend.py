############################# ENCODING STRINGS ###############################
def encode_string(string):
   encode_str = ""
   for c in string:
       if len(str(ord(c))) == 2:
           encode_str += "0" + str(ord(c))
       else:
           encode_str += str(ord(c))
   return encode_str
##############################################################################

############################# DECODING STRINGS ###############################
def decode_string(string):
    decode_str = ""
    iterations = len(string)//3
    my_list = []

    for i in range(iterations):
        character = ""
        for j in range(3):
            character += string[(i * 3) + j]
        my_list.append(character)

    for item in my_list:
        if item[0] == "0":
            item = item[1:]
        decode_str += chr(int(item))

    return decode_str
##############################################################################
