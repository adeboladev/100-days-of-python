

foods = ["rice","semolina","cocopops","bread","chinchin",]

for food in foods:
	print(food)
	
print(foods[0])

foods.append("ekuru")
print(foods)

foods.remove("cocopops")
print(foods)

for food in foods:
	print(food)
	
new_food= input("what food do you want to add?")
foods.append(new_food)
print(foods)
print("you now have",len(foods),"foods.",)



