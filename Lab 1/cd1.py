file  = open("./programcode.c", 'r')
lines = file.readlines()

keywords    = ["void", "main", "int", "float", "bool", "if", "for", "else", "while", "char", "return"]
operators   = ["=", "==", "+", "-", "*", "/", "++", "--", "+=", "-=", "!=", "||", "&&"]
punctuations= [";", "(", ")", "{", "}", "[", "]"]

found_keywords=[]
found_operators=[]
found_punctuations=[]
found_int=[]
found_identifier=[]

def is_int(x):
    try:
        int(x)
        return True
    except:
        return False

for line in lines:
    for i in line.strip().split(" "):
        if i in keywords:
            #print (i, " is a keyword")
            found_keywords.append(i)
        elif i in operators:
            #print (i, " is an operator")
            found_operators.append(i)
        elif i in punctuations:
            #print (i, " is a punctuation")
            found_punctuations.append(i)
        elif is_int(i):
            #print (i, " is a number")
            found_int.append(i)
        else:
            #print (i, " is an identifier")
            found_identifier.append(i)
print("keywords : ")
for x in found_keywords:
    print(x)
print("operators : ")
for x in found_operators:
    print(x)
print("punctuations : ")
for x in found_punctuations:
    print(x)
print("integers : ")
for x in found_int:
    print(x)
print("identifiers : ")
for x in found_identifier:
    print(x)
