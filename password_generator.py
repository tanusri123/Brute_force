counter = 0
character =['0','1','2','3','4','5','6','7','8','9','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',',','.','/',';','[','{','-','+','=','}',']','(',')']
file_open = open("wordlist.txt","w")

for i in character:
    for j in character:
        for k in character:
            for l in character:
                guess = str(i)+str(j)+str(k)+str(l)
                file_open.write(guess)
                file_open.write('\n')
                counter+=1
print('wordlist of {} password created'.format(counter))