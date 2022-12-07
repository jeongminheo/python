class UserInfo:
    def username(self, input_name):
        return input_name

    def userage(self, input_age):
        return input_age + 20

# 사전에 정의된 클래스에서 기능 추가하고 싶을 때 사용 : 상속 개념
# 부모 : 베이스 클래스 | 자식 : 파생 클래스
# 클래스 선언할 때 () 안에 베이스 클래스 이름을 명시
class UserInfoExt(UserInfo):  # 상속은 부모 / 자식
    def useraddress(self, input_address):
        return "사는 곳 : " + input_address 

# info = UserInfo()
# 파생클래스를 통해서 부모 클래스의 모든 기능을 사용 가능
info = UserInfoExt()
name = info.username("홍길동")
address = info.useraddress("서울시")

# 기존에 있던 부모 클래스의 기능 변경
# 메서드 오버라이드(오버라이딩)
class UserInfoUpdate(UserInfo): # 다형성 지원하기 위해서는 상속을 먼저함
    def username(self, input_name): # 오버라이드 할때 Python super()         
        # 기존의 부모 기능을 호출
        temp_data = super().username(input_name) + "님" # 기능 보강
        return temp_data

ext_info = UserInfoUpdate()
name2 = ext_info.username("홍길동2")
age2 = ext_info.userage(111)

temp = 0
        
