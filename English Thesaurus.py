import json
import time
import difflib
from difflib import get_close_matches
data=json.load(open("data.json"))
data=dict(data)
while True:
    word=input("Enter the Word: ")
    word1=word.lower()
    word2=word.title()
    if word1 in data.keys():# or word2 in data.keys():
        w2=data[word1]
        for i in w2:
            print(i)
    elif word1=="\end":
        break
    elif len(get_close_matches(word1,data.keys()))>0:
        matches=get_close_matches(word1,data.keys(),n=3)
        for i in range(1,len(matches)+1):
            print(f"Press {i} for {matches[i-1]}")
            print(f"did you mean by the word {get_close_matches(word1,data.keys())[0]}")
        num=int(input(f"\n"))
        print(matches[num-1])
        print("Word doesn't exist.")

# work------------------------------------------------
# res=input("Type Y for yes and N for no: ")
#         res1=res.lower()
#         if res == "y":
#             print(data[get_close_matches(w,data.keys())[0]])


# From difflib import get_close_matches--------- it is used to get the most closer matcher of the word

# import json
# import difflib
# from difflib import get_close_matches
# data = json.load(open("data.json"))
# data= dict(data)
# def translate(w):
#     if w.lower() in data.keys():
#         return data[w.lower]
#     elif len(get_close_matches(w,data.keys()))>0:
#         print(f"did you mean by word {get_close_matches(w,data.keys())[0]} ?")
#         res=input("Type Y for yes and N for no: ")
#         res1=res.lower()
#         if res1 == "y":
#             return (data[get_close_matches(w,data.keys())[0]])
#         elif res1=="n":
#             return ("Sorry we couldn't expect this for you! Try again with diferent one")
#     elif w.title() in data.keys():
#         return (data[w.title()])
#     elif w.upper() in data.keys():
#         return (data[w.upper()])
#     else:
#         print("Word not found.")
# wp2=input("Enter the word: ")
# result=translate(wp2)
# # print(type(result))
# if type(result) == list:
#     for l in result:
#         print(l)
# else:
#     print(result)