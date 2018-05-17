name = "Ford"

subjects = ["English","Math","Science","History","Spanish"]

print ("Hello " + name)

for i in subjects:
    print("One of my classes is "+ i)

tvshows = ["The Office", "Arrow", "The Flash", "NCIS", "Jessica Jones"]

for i in tvshows:
    if i == "Jessica Jones":
        print (i + " is bad")

    else:
        print (i + " is a good show")









movies = []

while True:
    print ("What movie do you like? Type 'end' to quit.")
    answer = input ()

    if answer == "end":
        break
    else:
        movies.append(answer)


for i in movies:
    print ("One of your favorite movies is " + i)






        
