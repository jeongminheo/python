# Set : 리스트 데이터의 중복된 데이터를 제거
# 리스트나 튜플 모두 중복제거 됨(튜플일 경우 신중히 중복제거 선택)
# 숫자값을 경우 자동으로 set을 함
array_list1 = {1, 3, 5, 7,9, 1, 1, 2, 3} # 1, 3의 중복 데이터
array_list2 = set(array_list1)
result12 = array_list1 & array_list1

# 추가 add 기능 / 삭제  remove
array_list2.add(100) # 추가
array_list2.remove(1) # 삭제
# 여러개를 추가할 경우 update 기능을 사용
array_list2.update({2,4,6,8})
# 모두 사라짐
array_list2.clear() 

# 문자열
array_list3 = {"A", "B", "A", "A", "B", "B"}

# 교집합 / 합집합 / 차집합
array_list4 = {1, 5, 9}
array_list5 = {1, 2, 7}

result1 = array_list4 & array_list5 # 교집합
result2 = array_list4.intersection(array_list5) # 교집합 기능 사용

result3 = array_list4 | array_list5 # 합집합
result4 = array_list4.union(array_list5) # 합집합 기능 상용

result5 = array_list4 - array_list5 # 차집합
result6  = array_list4.difference(array_list5) # 차집합 기능 사용


temp = 0