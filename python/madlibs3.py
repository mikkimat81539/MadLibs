adjBlanks = "...."
nounBlanks = "____"

story = f"Once upon a time, there was a {adjBlanks} {adjBlanks} {nounBlanks}"

allAdjBlanks = story.count(adjBlanks)
allNounBlanks = story.count(nounBlanks)

print(allAdjBlanks)
print(allNounBlanks)
