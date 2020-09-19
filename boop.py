f = open('text.txt','r')
data = f.read()
f.close()

new_data = data.replace('boop','sup')

f = open('text.txt','w')

f.write(new_data)

f.close()