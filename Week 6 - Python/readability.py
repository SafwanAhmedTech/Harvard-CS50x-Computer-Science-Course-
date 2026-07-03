text = input("Text: ")
wordcount = 1
lettercount = 0
length = len(text)

for n in range(length):
    if text[n].isalpha():
        lettercount += 1
    elif text[n] == " ":
        wordcount += 1

l = lettercount / (float(wordcount)/100)
fullstopcount = 0

for n in range(length):
    if text[n] == '.' or text[n] == '?' or text[n] == '!':
        fullstopcount += 1

s = fullstopcount / (float(wordcount) / 100)
index = 0.0588 * l - 0.296 * s - 15.8
index = round(index)

if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")

