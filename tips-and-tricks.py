#Challenge number one



# x_coords=[45,92,20,71,53]
# y_coords=[24,21,68,47,19]

# x=0
# while x<5:
#     print(x_coords[x],y_coords[x])
#     x+=1

# for n in range (len(x_coords)):
#     print(x_coords[n],y_coords[n])

# for x,y in zip(x_coords,y_coords):
#     print(x,y)

#Wanted outcome: 25,24
#92,21
#20,68




#Challenge number two



# shopping_list=["bread","cereal", "rice", "pasta", "eggs", "orange juice"]

# order=["Item 0: ","Item 1: ", "Item 2: ", "Item 3: ", "Item 4: ", "Item 5: "]
# for x,y in zip(shopping_list,order):
#     print(y,x)

# for i in range(len(shopping_list)):
#     print("Item {}: {}".format(i,shopping_list[i]))

#Wanted outcome: Item 0: bread, Item 1:cereal


#Challenge number three



# a=10
# b=20
# tmp=a 
# a=b
# b=tmp
# print(a)
# print(b)

# a,b=b,a0

#Wanted outcome: a=20 b=10



#Challenege number four
#We want to inspect a variable, object, module, class, etc...

# import math

# print(dir(math))




#Challenege number five



# sentence="A cranky old lady shoots lemons with her high-powered machinegun while wearing crocks."
#from pprint, import pprint

# words = sentence.split(" ")
# results={}
# for word in sorted(words):
#     first_letter=word[0]
    # if first_letter in results:
    #     results[first_letter].append(word)
    # else:
    #     results[first_letter].append(word)
#     print(first_letter, word)
#     results[first_letter]=word
# pprint(results)



#Challenege number five

# list=[]
# for _ in range (10):
#     list.append("LorenzoTheWolf")
# print(list)

# list=["LorenzoTheWolf" for _ in range(10)]
# list=["LorenzoTheWolf"]*10



#Challenge number six
age=15

if 5<= age<=17:
    print("You can join a class!")
else:
    print('No luck.')