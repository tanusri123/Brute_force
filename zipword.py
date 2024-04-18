import zipfile
import time

folderpath = input("Path to the file: ")
zipf = zipfile.ZipFile(folderpath)
global result
result = 0
global tried
tried = 0
c=0
if not zipf:
    print("zip file/folder is not password protected! You can succesfully open it")
else:
    starttime = time.time()
    wordListfile = open('wordList.txt','r',error='ignore')
    body = wordListfile.read().lower()
    words = body.split('\n')

for i in range(len(words)):
    word = words[i]
    password = word.encode('utf8').strip()
    c= c+1
    print('Trying to decode password by:{}'.format(word))
    try:
        with zipfile.ZipFile(folderpath,'r') as zf:
            zf.extractall(pwd=password)
            print("Success! The password is:"+word)
            endtime = time.time()
            result = 1
        break
    except:
        pass
if(result == 0):
    print("Sorry, password not found. A total of "+str(c)+"+ possible combination tried in"+srt(duration)+"seconds. Password is not of 4 character")
else:
    duration = endtime-starttime
    print("Congratulation!! Password found after trying"+str(c)+"combination in "+str(duration)+'seconds')



