def begin_story():
	user_response = 0
	print("you want to take a break from the city so you decide to go to the woods. what would you like to do?")
	user_response = int(input("1.Go camping\n2.go hiking."))
	decision1(user_response)
	
def decision1(user_response):
	print("you get all the stuff to eaither go campping or hiking.")
	if user_response == 1:
		print("you decided to go camping. What do you do next?")
		user_response = int(input("1.make a fire.\n2.go fishing."))
		decision2_1(user_response)
	elif user_response == 2:
		print("you decided to go hiking. What road do you want to take?")
		user_response = int(input("1.long flat road.\n2.short steep road."))
		decision2_2(user_response)
	
def decision2_1(user_response):
	print("while going camping, you stumble upon a problem...")
	if user_response == 1:
		print("you have no wood for your fire. What do you do next?")
		user_response = int(input("1.Go look for wood.\n2.break tree branch to use for fire."))
		decision3_1_1(user_response)
	elif user_response == 2:
		print("you decided to go fishing for food. What do you do next?")
		user_response = int(input("1.go to the big lake.\n2.go to the small lake."))
		decision3_1_2(user_response)

def decision2_2(user_response):
	print("while going hiking you take some supplies with you.")
	if user_response == 1:
		print("there is someone that needs help. What do you do next?")
		user_response = int(input("1.help them\n2.keep hiking."))
		decision3_1(user_response)
	elif user_response == 2:
		print("you trip over somthing in a bag.. What do you do next?")
		user_response = int(input("1.open the bag\n2.keep hiking."))
		decision3_2(user_response)
		
def decision3_1_2(user_response):
  print("you take your lucky rod.")
  if user_response == 1:
    print("you catch a bunch of fish. now what.")
    user_response = int(input("1.keep them.\n2.throw them back."))
    decision3_1_3(user_response)
  elif user_response == 2:
    print("you only catch a little fish.")
    
def decision3_1_3(user_response):
  print("if you would have kept them you would have food, and if you throw them back you now have no food.")
  
def decision3_1_1(user_response):
  print("while looking for wood you see somthing in the distance.")
  if user_response == 1:
    print("you get closer and notice its a cave. what do you do next.")
    user_response = int(input("1.explore the cave.\n2.keep looking for wood."))
    decision3_2_1(user_response)
  elif user_response == 2:
	  print("the whole tree breaks and falls on you, YOU DIED.")
	  
def decision3_2_1(user_response):
  print("its getting dark")
  if user_response == 1:
    print("you go into the cave and get trapped,what do you do?.")
    user_response = int(input("1.yell for help.\n2.try to escape."))
    decision3_2_2(user_response)
  elif user_response == 2:
    print("you find wood, what now?.")
    user_response = int(input("1.go back.\n2.keep loking for more wood."))
    decision3_2_3(user_response)
    
def decision3_2_2(user_response):
  print("what ever you do you will stay trapped and eventually die.")
  
def decision3_2_3(user_response):
  print("whatever you do, you have wood and go back and enjoy your camping trip.")
    
def decision3_1(user_response):
  print("its getting dark")
  if user_response == 1:
    print("there is a body in the bag and the cops blame you for the murder.")
  elif user_response == 2:
    print("you finish your hiking and are now in shape.")
    
def decision3_2(user_response):
  print("its a short hike and getting dark")
  if user_response == 1:
    print("there is money inside of it and take it and now ur a millionare")
  elif user_response == 2:
    print("you finished ur short hike but your still not in shape.")

user_name = input("Enter your name")
begin_story()
