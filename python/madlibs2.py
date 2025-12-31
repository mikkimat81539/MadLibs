blanks = "____"

story = f"There was a {blanks} dog."
print(story)

def userInput():
	return input("Enter an adjective: ")

storyReplace = story.replace(blanks, userInput())

print(storyReplace)
