from time import sleep
    
def choiceControl(message):
    while True:
        try:
            choice = int(input(message))
        except ValueError:
            print("That's not a number. Try again!")
            continue
        else:
            return choice
            break

stripeLine = "---------------------------------------------------"

#Greeting a player
print("\nWelcome to the game {0}!".format(input("Please enter your player name: ")))
sleep(2)
print(stripeLine)

#Game starting point
#First paragraph
print("Game starts with you walking in a forest. In the forest, where everything is beautiful and you are enjoing this magnificent view"
      "\n\n"
      "But suddenly..."
      "\n\n"
      "You hear branch cracking in the distance."
      "\n"
      "You start listening very carefully but after a while in the distance you notice one big shadow moving towards you."
      "\n"
      "\n"
      "As this big shadows is walking towards you"
      "\n"
      "You are starting to understand what this big shadow is"
      "\n\n"
      "That's bear!"
      "\n\n"
      "But now it's too late")

#First choice
print("\n"
      "In a short amount of time you thought out only three options:"
      "\n"
      "1. You run away"
      "\n"
      "2. You stay in place"
      "\n"
      "3. You lie down")
print(stripeLine)

choice = choiceControl("What are you going to do? (Enter choice number): ")

#Second paragraph, first choice
if choice == 1:
    print(stripeLine)
    print("You start running away but bear does not liked it")
    print("\n"
          "As you are running for your life, bear is trying to catch you. After running for solid minute you see only two options: "
          "\n"
          "1. You run to the cave"
          "\n"
          "2. You climb up to the tree")
    
    print(stripeLine)
    
    choice = choiceControl("What are you going to do? (Enter choice number): ")
    
    if choice == 1:
        print("\n"
              "You ran into the cave where you try to hide. Unfortunately there is nowhere to hide, so bear catches you and adopts you.")
        print(stripeLine)
        print("The end!")
        print(stripeLine)
        
    elif choice == 2:
        print("\n"
              "You think that you are smart person and climbing up to the tree will help fou but unfortunately you have forgot that bears can climb.")
        print(stripeLine)
        print("The end!")
        print(stripeLine)

        
        
#Second paragraph, second choice and third choice
elif choice == 2 or choice == 3:
    print("Now that you are not moving, bear is not aggressive so he comes closer. Bear makes few quick whiffs and continues his trip. ")
    print(stripeLine)
    print("The end!")
    print(stripeLine)
