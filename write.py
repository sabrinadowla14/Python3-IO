f=open("new_file.txt", 'a')
lines = ['Hello', 'How', 'are', 'You']
text = '.\n'.join(lines)
f.writelines(text)
f.close()