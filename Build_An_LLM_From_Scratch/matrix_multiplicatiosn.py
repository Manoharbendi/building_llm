import numpy as np 

cricketers=np.array([
    [9,3,7,8],#virat
    [2,10,6,9],#bumrah
    [8,2,6,7]#rohit
])
# print(cricketers)

ideal_captain=np.array([8,5,7,9])
name=["Virat","Bumrah","Rohit"]

# print("at a time(loop) ")# this loop is for the above cricketers array for one row and column
# for i ,name in enumerate(name):
#     score=0
#     for j in range (4):
#         score+=cricketers[i][j]*ideal_captain[j]
#     print(f"{name}:{score}")

# print("\n all at once (matrix):")
# all_scores=cricketers@ideal_captain #this easy way to multiple the matrix 
# for name ,score in zip (name ,all_scores):
#     print(f"{name}:{score}")

import time 
# It refers to the total number of unique token IDs available in the vocabulary.
vocab_size=100_000
# Imagine you want your model to learn different patterns and relationships in language.A numerical vector provides a space in which the model can learn these patterns.
dimensions=4096
#  all the words or token that are defiend in the 4096 dimension
vocabulary=np.random.randn(vocab_size,dimensions).astype(np.float32)
# requirement vector is the 4096 dimension
requirement=np.random.randn(dimensions).astype(np.float32)
print(vocabulary)
print(requirement)

start =time.time()
score_slow=[]

for i in range(vocab_size):
    score =0
    for j in range (dimensions):
        score+=vocabulary[i][j]*requirement[j]
    score_slow.append(score)
loop_time = time .time() - start
# print(f"the loop time is :{loop_time}")#the loop time is :187.49529194831848

start=time.time 
score_fast=vocabulary@requirement
matrix_time=time.time()-start
print(matrix_time)