virat=[9,3,7,8]
bumrah=[2,10,6,9]
rohit=[8,2,6,7]

def dot_product(vec_a,vec_b):
    total=0
    for i in range (len(vec_a)):
        total+=vec_a[i]*vec_b[i]
    return total
# print(dot_product(virat,bumrah))
# print(dot_product(virat,rohit))

# we are wroking in the different scales that why we are getting the huge differnce 
rajat=[9,8,7,9]
rahul=[90,80,70,90]

print(f"dot.product of the rajat and rahul {dot_product(rahul,rajat)}")
print(f"dot.product of the rajat and rajat {dot_product(rajat,rajat)}")

# cosine_similarity= dot_product(a,b)/(magnitude(a)*magnitude(b))
import math
def vector_size(vec):
    total=0
    for x in vec:
        total+=x*x
    return math.sqrt(total)
print(f"size of the vector [3,4]{vector_size([3,4])}")
print(f"size of the vector [3,4]{vector_size(rajat)}")
print(f"size of the vector [3,4]{vector_size(rahul)}")

def cosine_similarity(vec_a,vec_b):
    dot=dot_product(vec_a,vec_b)# this is for the dot product 
    size_a=vector_size(vec_a)# this is for the magnitude of the vector a
    size_b=vector_size(vec_b)#this is for the magnitude of the vector b

    if size_a ==0 or size_b == 0:
        return 0
    return dot/(size_a*size_b)
# print(f"dot.product of the rajat and rahul {cosine_similarity(rahul,rajat)}")
# print(f"dot.product of the rajat and rajat {cosine_similarity(rajat,rajat)}")


king = [0.8, 0.6, -0.3, 0.9, 0.2]
queen = [0.7, 0.7, -0.2, 0.8, 0.3]
cricket = [-0.1, 0.2, 0.8, -0.4, 0.7]
potato = [-0.5, -0.3, 0.1, -0.6, -0.2]

print(f"king <---------->queen {cosine_similarity(king,queen)}")
print(f"king <---------->potato {cosine_similarity(king,potato)}")

def find_best_word_in_llm(required_vector ,vocabulary):
    score={}
    for word_name ,word_vector in vocabulary.items():
        score[word_name]=cosine_similarity(required_vector,word_vector)
    return sorted(score.items(),key=lambda x:-x[1])
vocab={"king":king,"queen":queen,"cricket":cricket,"potato":potato}
requirement =[0.75,0.65,-0.25,0.85,0.25]
for word ,score in find_best_word_in_llm(requirement,vocab):
    print(f"{word}:{score:.3f}")