file = open("demo.txt","w")
file.write("Something went \n wrong good bad anyone not \n in good oru so lingha thou  \n")
file.close()


r = open("demo.txt","r")
print(r.read())
