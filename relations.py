
import random

def generate_set(n):
    return [random.randint(0, 1) for _ in range(n)]

def convert_set(generated):
    return [i for i, j in enumerate(generated) if j == 0]

def generate_cartesian(seta):
    return [(i, j) for i in seta for j in seta]

def generate_relation(cartesian):
    return random.sample(list(cartesian), random.randint(1, len(cartesian)))


# a reflexive relation is one where there exists a tuple with
# the same element for every possible element in the set a
def is_reflexive(seta, relation):
    return all((a, a) in relation for a in seta), 'reflexive'


# an irreflexive relation has no self-pairs
def is_irreflexive(seta, relation):
    return all((a, a) not in relation for a in seta), 'irreflexive'


# symmetric relations contain (b, a) for every (a, b)
def is_symmetric(relation):
    return all((b, a) in relation for (a, b) in relation), 'symmetric'


# antisymmetric relations cannot contain both (a, b) and (b, a)
# unless a == b
def is_antisymmetric(relation):
    return all(a == b or (b, a) not in relation for (a, b) in relation), 'antisymmetric'


# transitive relations contain (a, c) if (a, b) and (b, c) exist
def is_transitive(relation):
    return all((a, c) in relation for a, b in relation for d, c in relation if d == b), 'transitive'

# an equivalence relation is reflexive, symmetric and transitive
def is_equivalence_relation(seta, relation):
    r = is_reflexive(seta, relation)[0]
    s = is_symmetric(relation)[0]
    t = is_transitive(relation)[0]

    return r and s and t, 'equivalence relation'

# a partial order is reflexive, antisymmetric and transitive
def is_partial_order(seta, relation):
    r = is_reflexive(seta, relation)[0]
    a = is_antisymmetric(relation)[0]
    t = is_transitive(relation)[0]

    return r and a and t, 'partial order'

# a linear order is a partial order where 
# there exists an a, b or b, a for any a and b in the set
def is_linear_order(seta, relation):
    p = is_partial_order(seta, relation)[0]
    c = all((a, b) in relation or (b, a) in relation for a in seta for b in seta)

    return p and c, 'linear order'


setb = convert_set(generate_set(100))

# handles empty sets
if not setb: print("set empty")
else:
    cartesian = generate_cartesian(setb)
    relation = generate_relation(cartesian)

    set_len = len(setb)
    cart_len = len(cartesian)
    rel_len = len(relation)

    funcs = [
        is_reflexive(setb, relation),
        is_irreflexive(setb, relation),
        is_symmetric(relation),
        is_antisymmetric(relation),
        is_transitive(relation),
        is_equivalence_relation(setb, relation),
        is_partial_order(setb, relation),
        is_linear_order(setb, relation),
    ]


    print(f"\n length of the set: {set_len} \n cartesian length: {cart_len} \n relation length: {rel_len} \n")
    for value, name in funcs:
        status = name if value else f"not {name}"
        print(f"{status}")
