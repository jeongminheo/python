import 허정민_exam05_01

class HRClassOver(허정민_exam05_01.HRClass):
    def user_name(self, input_name):
        u_name='이름 : '+ input_name+' 님'
        return u_name

    def user_age(self, input_age):
        u_age='나이 : '+input_age
        return u_age
        
UserInfo=HRClassOver()

