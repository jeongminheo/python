class HRClass:
    def user_name(self, input_name):
        return input_name

    def user_age(self, input_age):
        return input_age

    def user_address(self,input_address):
        return input_address


class HRClassOver(HRClass):
    def user_name(self, input_name):
        u_name='이름 : '+ input_name+' 님'
        return u_name

    def user_age(self, input_age):
        u_age='나이 : '+input_age
        return u_age

UserInfo=HRClassOver()
age=UserInfo.user_age('20')
temp=0
