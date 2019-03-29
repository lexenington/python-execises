from pprint import pprint
#########################
# Program for most repeated character
#########################

sentence = "This is a common interview question"

sentence = sentence.lower()
char_freq = {}
for char in sentence:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

sorted_list = sorted(char_freq.items(), key=lambda kv: kv[1], reverse=True)
pprint(sorted_list[0])
