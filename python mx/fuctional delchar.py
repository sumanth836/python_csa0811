text=input("entre the string:")
char=input("Entre the char:")
newtext=""
for i in range(len(text)):
    if text[i]!=char:
        newtext=newtext+text[i]
print("\nString after removing char:")
text=newtext
print(text)
