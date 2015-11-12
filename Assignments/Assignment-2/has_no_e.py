#Anne Tissera 100554223

fin = open('gadsby_stripped.txt')

def has_no_e(phrase):
for char in phrase:
if char in 'Ee':
return False
return True

print ("Input a string to check")
phrase = input("")

print (has_no_e(phrase))

fin = open('gadsby_stripped')

for line in fin:
phrase = line.strip()
if(has_no_e(phrase)):
print ("True")
break
else:
print("False")

