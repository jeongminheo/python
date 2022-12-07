import 허정민_exam05_02
import 허정민_exam05_03

#파일 쓰기모드로 생성
file_date=open('mytxt.txt',mode='w',encoding='utf-8')

#앞 exam05모듈에 해당 내용 저장
name=허정민_exam05_03.UserInfo.user_name('허정민')
age=허정민_exam05_03.UserInfo.user_age('23')
address=허정민_exam05_03.UserInfo.user_address('청주시 서원구')
mail=허정민_exam05_02.UserInfo.user_mail('gjwjdals56@gmail.com')
phone=허정민_exam05_02.UserInfo.user_phone('01085179562')

#파일에 쓰기
file_date.write(name)
file_date.write('\n')
file_date.write(age)
file_date.write('\n')
file_date.write(address)
file_date.write('\n')
file_date.write(mail)
file_date.write('\n')
file_date.write(phone)

#파일 닫기
file_date.close()

#파일읽기
file_date2=open('mytxt.txt',mode='rt',encoding='utf-8')
data_line1=file_date2.readline()
data_line2=file_date2.readline()
data_line3=file_date2.readline()
data_line4=file_date2.readline()
data_line5=file_date2.readline()
file_date2.close()

print(data_line1)
print(data_line2)
print(data_line3)
print(data_line4)
print(data_line5)

