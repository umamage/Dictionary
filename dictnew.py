import json
from difflib import get_close_matches
dic = json.load(open("data.json"))
def meaning(word):
    lword=word.lower()
    if(word in dic.keys()):
        return dic[word]
    elif(lword in dic.keys()):
        return dic[lword]
    elif(word.title() in dic.keys()):
        return dic[word.title()]
    elif(word.upper() in dic.keys()):
        return dic[word.upper()]
    elif len(get_close_matches(lword,dic.keys(),cutoff=0.8))>0:
        print("Did you mean %s instead?" % get_close_matches(lword,dic.keys(),cutoff=0.8)[0])
        ans = input("Enter Y/N: ")
        if(ans.lower() == 'y'):
            return dic[get_close_matches(lword,dic.keys(),cutoff=0.8)[0]]
        elif (ans.lower() == 'n'):
            return "Sorry! word not found. Please check"
        else:
            return "Sorry! we didn't understand your input"
    else:
        return "Sorry! word not found. Please check"

w = input("Enter word: ")
mng = meaning(w)
if(isinstance(mng,str)):
    print(mng)
else:
    for ele in mng:
        print(ele)
