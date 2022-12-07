class HRClass:
    def user_name(self, input_name):
        return input_name

    def user_age(self, input_age):
        return input_age

    def user_address(self,input_address):
        return input_address

hr=HRClass()
name=hr.user_name('허정민')
age=hr.user_age('20')
address=hr.user_address('청주시')