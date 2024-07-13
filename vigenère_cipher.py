from typing import Dict, List

# program to encode a message using the vigenère cipher :)

"""
The following information is copied from Wikipedia:

The Vigenère cipher: each letter of the plaintext is encoded with a different Caesar cipher,
whose increment is determined by the corresponding letter of another text, the key.

eg. if the plaintext is "attacking tonight" and the key is "OCULORHINOLARINGOLOGY," then

- the first letter a of the plaintext is shifted by 14 positions in the alphabet 
(because the first letter O of the key is the 14th letter of the alphabet, counting from 0), yielding o;
- the second letter t is shifted by 2 (because the second letter C of the key means 2) yielding v;
- the third letter t is shifted by 20 (U) yielding n, with wrap-around;
- and so on; yielding the message ovnlqbpvt hznzouz. 

If the recipient of the message knows the key, they can recover the plaintext by reversing this process.
"""

# dictionary to map each character in the alphabet to a number, starting from 0
alphabet = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,
            "p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}

plaintext = "attacking tonight"
# convert to lowercase to prevent issues with indexing from the dictionary
lower_plaintext = plaintext.lower() 

key = "OCULORHINOLARINGOLOGY"
# ensure that the key is at least the same length as the plaintext - it can be longer but not shorter
while len(key) < len(plaintext):
    # the key is repeated until it matches the length
    key += key
# convert to lowercase to prevent issues with indexing from the dictionary
lower_key = key.lower()

# lists to store the corresponding numbers to each character in the plaintext 
plaintext_list = []
key_list = []

# store the numeric value of each character in the plaintext into the corresponding list
for char in lower_plaintext:
    if char != " ":
        plaintext_list.append(alphabet[char])
    # if the plaintext has any spaces, append -1 since it does not correspond to any key:value pair in the dictionary
    # this will not only prevent errors but is also important for later when the plaintext is actually encoded
    else:
        plaintext_list.append(-1)
        
for char in lower_key:
    # yeah not gonna lie i don't actually know how it works if there's a space in the key
    if char != " ":
        key_list.append(alphabet[char])
    else:
        key_list.append(-1)

# copy the plaintext list to simplify the process of adding the values in the two lists
encoded_list = plaintext_list.copy()

# counters: i for encoded_list and j for key_list
i = 0
j = 0

# add the numerical values of the two lists together, this is the process of shifting each letter in the plaintext based on the key
while i < len(plaintext):
    # -1 represents a space
    if plaintext_list[i] != -1:
        encoded_list[i] += key_list[j]
        # if the resulting number is >= 26, we need to account for wrap around by subtracting 26
        if encoded_list[i] >= 26:
            encoded_list[i] -= 26
        # increment both counters
        i+=1
        j+=1
    # if there is a space, represented by -1, then increment the counter for encoded_list, i.e. move to the next character
    # however, the counter for key_list is not incremented because a space in the plaintext does not correspond to a skip in the key
    # for example, if you have 'i really like piplup' as the plaintext and 'alot' as the key, when you go from 'i' to 'really', 'i' corresponds to 'a' and 'r' corresponds to 'l', not 'o'
    else:
        i+=1

message = ""

# function to invert the key:value pairs in alphabet
def inverse (d: Dict[int,int]) -> Dict[int,List[int]]:
    inversion = {}
    for key in d:
        inversion[d[key]] = key
    return inversion

inverse_alphabet = inverse(alphabet)

# convert the numerical value to the letter using the inversed dictionary
for num in encoded_list:
    if num != -1:
        message += inverse_alphabet[num]
    # -1 represents a space (refer to line 44)
    else:
        message += " "
        
print(message)
