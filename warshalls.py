import numpy as np
import random

# warshalls algoritm 

# generating tuples to place into relations
def generate_tuple(min_value, max_value):
    number_one = random.randint(min_value, max_value)
    number_two = random.randint(min_value, max_value)

    return (number_one, number_two)

# generating relations based on tuples
def generate_relation(min_value, max_value):
    relation = []
    number_elements = random.randint(min_value, max_value)

    for _ in range(number_elements):
        relation.append(generate_tuple(1, 10))

    return relation

# finds every single element that exists in each tuple to 
# find range for indexing purposes but also
# to allow for the rows and cols of the matrix
def find_relation_elements(relation):
    relation_elements_array = []

    for pair in relation:
        if pair[0] not in relation_elements_array:
            relation_elements_array.append(pair[0])

        if pair[1] not in relation_elements_array:
            relation_elements_array.append(pair[1])

    relation_elements_array.sort()
    return relation_elements_array

# generates an index for each element based on it's position in the 
# relations elements array which contrains no duplicates
def element_index_lookup(element, relation_elements_array):
    index = -1

    for i, relation_element in enumerate(relation_elements_array):
        if relation_element == element:
            index = i
            break

    return index

# creating an graphing matrix for each element
def create_matrix(relation, relation_elements):
    matrix = np.zeros((len(relation_elements), len(relation_elements)), dtype = int)

    for pair in relation:
        el1i = element_index_lookup(pair[0], relation_elements)
        el2i = element_index_lookup(pair[1], relation_elements)
        matrix[el1i, el2i] = 1

    return matrix

# warshalls algorithm
# basically saying if xy and yz exist then xz must exist for transitiveness
def warshall(matrix):
    matrix = matrix.copy()

    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i, k] == 1 and matrix[k, j] == 1:
                    matrix[i, j] = 1

    return matrix

print("relation: \n ")
rel = generate_relation(1, 10)
print(rel)
print("\n")

print("elements: \n ")
elements = find_relation_elements(rel)
print(elements)
print("\n")

print("matrix: \n ")
matrix = create_matrix(rel, elements)
print(matrix)
print("\n")

print("complete: \n ")
transitive_closure = warshall(matrix)
print(transitive_closure)