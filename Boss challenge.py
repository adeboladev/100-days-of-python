

foods = ["rice","beans","yam",]
for food in foods:
	print(food)
	
new_food = input("what food do you want to add?")
foods.append(new_food)
print(foods)

old_food = input("which food do you want to remove?")
foods.remove(old_food)
print(foods)

print("you have", len(foods), "food left.")
 
for food in foods:
 	print("you have", (food), "left",)