L=['Network' , 'Math' , 'Programming', 'Physics' , 'Music']
word_length=0;
for i in L:
    if(len(i)>word_length):
        word_length=len(i)
        res=i
print('The longest word is: {0}'.format(res))
