import numpy as np
corpus = """
The king sat on the throne in the grand palace.
The king wore a golden crown on his head.
The queen wore a silver crown on her head.
The king ruled the kingdom with great wisdom.
The queen ruled the kingdom with great grace.
The king loved playing cricket in the garden.
The queen loved playing chess in the palace.
The prince trained with the knight every morning.
The queen sat on the throne beside the king.
The knight protected the king and the queen.
The people loved the king and the queen dearly.
The princess studied with the sage every evening.
The sage advised the king and the queen wisely.
The kingdom had a beautiful garden and a grand palace.
The crown was the symbol of the great kingdom.
The king walked through the garden every evening.
The queen walked through the palace every morning.
The knight and the sage served the kingdom faithfully.
The prince loved playing cricket with the knight.
The princess loved playing chess with the sage.
"""

################################
#step-1 Pre processing of the input
words =corpus.lower().split()
# print(f"total word in the corpus:{len(words)}")
# print(f"print first 20 words :{words[:20]}")

#step-2 creation of vocab
vocab=sorted(set(words))#this because we using the set for the unique words to collection
vocab_size=len(vocab)
# print(vocab_size)

# dictionary for quick access
word_to_idx={word:idx for idx,word in enumerate(vocab)}#this code and the below code are for the giving the index postion to the word which will be easy for finding the word
idx_to_word={idx:word for idx,word in enumerate(vocab)}

# for i,word in enumerate (vocab):
#     print(f"{i:3d}:{word}")
# print(idx_to_word[45])
# print(word_to_idx["sat"])

# now the below code id for the making the pair between the word in the numbers
WINDOW_SIZE=2

def create_training_pair(words,window_size):
    pairs=[]#all the pair we are making as theh list
    for center_pos in range (len(words)):
        center_idx=word_to_idx[words[center_pos]]#now this for finding the value of the center index using this value we gonna get the after two words and befor two words with the help of the window size 

        window_start=max(0,center_pos - window_size)# this for not getting the negative value means if the value 0 than there migh be the chanes of getting the -1 ,-2 like that which may cause the wrong output 
        window_end=min(len(words),center_pos+window_size)# this for  not exeding the max value which may occures to the errors 

        for neighbor_pos in range (window_start,window_end):
            if neighbor_pos != center_pos:
                neighbor_idx=word_to_idx[words[neighbor_pos]]
                pairs.append((center_idx,neighbor_idx))#this for making the pairs of the value and there index postion for example if there the word then after that next word will taken and make them as the pair 
    return pairs

training_pairs=create_training_pair(words,WINDOW_SIZE) 
# print(f"training pairs{training_pairs}")#we will get the pairs of words with respect to there index postion
# print(idx_to_word[43])
# print(word_to_idx["sage"])

# print(f"\nFirst 15 pairs:")
for center_idx,neighbor_idx in training_pairs[:15]:
    center_word=idx_to_word[center_idx]
    neighbor_word=idx_to_word[neighbor_idx]
    # print(f"({center_word},{neighbor_word})")

EMBEDDING_DIM=30
np.random.seed(42)
vectors=np.random.randn(vocab_size,EMBEDDING_DIM)*0.1#this for give the evry value are assined to the word in the vectors 

def cosine_similarity(word1,word2):
    v1=vectors[word_to_idx[word1]]
    v2=vectors[word_to_idx[word2]]
    dot =np.dot(v1,v2)

    norm1=np.linalg.norm(v1)
    norm2=np.linalg.norm(v2)

    if norm1==0 or norm2==0:
        return 0
    return dot/(norm1*norm2)

#Training
learning_rate=0.05
num_epochs=80
num_negatives=5

def sigmoid(x):
    x=np.clip(x,-10,10)    
    return 1/(1+np.exp(-x))
print(f"{sigmoid(-5):.4f}")
