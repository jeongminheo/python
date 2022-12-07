#변수에 데이터저장
#문자열 변환
#이름:홍길동
#변환이름: xxxx -> utf8 변환(encode)
#변수에 저장 변환이름 저장


name1='허정민'
name2=name1.encode('utf-8')


#메일주소:
#변환주소:-> utf8변환


mail1='gjwjdals56@gmail.com'
mail2=mail1.encode('utf-8')

#출력변수 저장:"이름:xxxxx,메일주소 :xxxxx"-utf변환값
show=('이름:'+str(name2)+', 메일주소 :'+ str(mail2))
print(show)