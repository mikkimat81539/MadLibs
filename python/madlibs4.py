adjBlanks = "..."
nounBlanks = "___"
verbBlanks = "***"

storyTime = f"""Danger in the city of {nounBlanks}. 
People {verbBlanks} and {adjBlanks}. What a scary time right now."""

print(storyTime)

replaceNoun = storyTime.replace(nounBlanks, input("Enter an noun: "))
replaceAdj = storyTime.replace(adjBlanks, input("Enter an adjective: "))
replaceVerb = storyTime.replace(verbBlanks, input("Enter an verb: "))

print(storyTime)
