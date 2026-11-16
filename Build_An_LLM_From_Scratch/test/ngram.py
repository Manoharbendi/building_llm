text = """
the king loved playing cricket in the royal garden every evening

the king and the queen walked in the royal garden together

the queen loved playing chess in the grand palace every afternoon

the people loved the king because the king loved the people

the king loved the queen and the queen loved the king dearly

the royal garden was beautiful in the evening light

the grand palace had a chess room where the queen played every day
"""

# print(text)

word=text.lower().split()
# print(word)

def build_ngram_model(word,n):
    count={}

    for i in range (len(word)-n+1):
        context= tuple(word[i:i+n-1]) #this is the  code  when we are taking the value of the n value like if we are using the bigram the value is 2 then it will take one value (this is base on the sliding window) 
        target=word[i+n-1]# this for the next word to chose #### for example if  are using the bigram them one value will be the one will be  context and one word will be the target if we are using the trigram then the  context will be two words and the target will the next word 

        if context not in count:
            count[context]={} #this for the ##### count ={"the:"{}} this gonna create the side one 
        if target not in count[context]:
            count[context][target]=0#this for the ##### count ={"the:"{king=1,game=1}} this gonna create the side one 
        count[context][target]+=1#for the increment the value in the {king=2,game=1} if the value get again and again

    probs = {}
    for context in count:
        total = sum(count[context].values())
        probs[context] = {}
        for target in count[context]:
            probs[context][target] = count[context][target] / total
    return probs

# the below one is for calculating the probabilty
bigram = build_ngram_model(word, 2)
trigram = build_ngram_model(word, 3)
fourgram = build_ngram_model(word, 4)

print("bigram - after - loved:")
for w, p in sorted(bigram[("loved",)].items(), key=lambda x: -x[1])[:5]:
    print(f" {w}: {p:.1%}")

print("trigram - after - king ,loved:")
if ("king", "loved") in trigram:
    for w, p in sorted(trigram[("king", "loved")].items(), key=lambda x: -x[1])[:5]:
        print(f" {w}: {p:.1%}")

# print(build_ngram_model(word,4))