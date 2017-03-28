if 43 > 42:
    print ("ABC")

# ==============================

movies = ["A", "B", "C"]

print (movies[1])


# ==============================

cast = ["Cleese", "Palin", "Jones", "Idle"]
print (cast)
print (len(cast))
print (cast[1])
cast.append("A")
print (cast)
cast.pop()
print (cast)
cast.pop()
print (cast)
cast.extend(["A12", "A23"])
print (cast)
cast.remove("Palin")
print (cast)
cast.insert(0, "XYZ")
print (cast)


# ==============================
movies = ['\"A\"', 'B', 'C', [1, 2, 3]]
movies.insert(1, 1981)
movies.insert(3, 1971)
movies.insert(5, 1985)
for each_movies in movies:
    print (each_movies)
print (movies[6][0])
print (movies)
movies.insert(5, [1, 9, ["x", "y", "z"], 8, 5])
for e_m in movies:
    print (isinstance(e_m, list))
# ==============================
print (movies)
for e_m1 in movies:
    if isinstance(e_m1, list):
        for e_m2 in e_m1:
            print (e_m2)
    else:
        print (e_m1)

print ("======================================")

# # print (dir(__builtins__))
# for eb in dir(__builtins__):
#     print (eb)
#     print (help(eb))
#     print ("======================================")

print ("======================================")

print (movies)


def print_lol(L):
    for each_item in L:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print (each_item)
print_lol(movies)


import sys
sys.path
