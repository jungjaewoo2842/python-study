url="http://naver.com"
mystr=url.replace("http://","")
mystr=mystr[0:5]
password=(mystr[0:3]+str(len(mystr))+str(mystr.count("e"))+"!")
print("{0}의 비밀번호는{1}입니다".format(url,password))
