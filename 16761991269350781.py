from collections import OrderedDict
word_num = int(input())
syn_lis =[]
syn_dict = OrderedDict()
global_lis =[]
for i in range(word_num):
    syn_lis=[str(x)for x in input().split()]
    global_lis.append(syn_lis)
#print (global_lis)
syn_dict = {y[0]:y[1] for y in global_lis}
#print(syn_dict)
string = str(input())
string_lis = string.split(' ')
#print(string_lis)
result = []
word = ' '
for j in string_lis:
    if(j in syn_dict.keys()):
        pass
    else:
        syn_dict[j] = j
for item in string_lis:
        word = syn_dict[item]
        result.append(word)
print(' ' .join(result))
       
        
        

   