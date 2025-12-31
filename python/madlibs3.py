adjBlanks = "...."
nounBlanks = "____"

story = f"Once upon a time, there was a {adjBlanks} {nounBlanks} {adjBlanks}"

allAdjBlanks = story.count(adjBlanks)
allNounBlanks = story.count(nounBlanks)

print(allAdjBlanks)
print(allNounBlanks)
