catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
    ['황금의 칼날', '비열한 간신', '무명의 영웅'],
    ['성공의 열쇠', '내면의 변화', '목표의 달성'],
]

''' 
도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
'성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
'''

#새로운 변수에 같은 값을 할당한다. -> 원본 식별자에 영향을 주지 않도록 복사해야 함
#얕은 복사, 깊은 복사 주의
backup_catalog = catalog[:] #원본 자체를 복사해서 새로운 값으로 --> 슬라이싱을 했을떄 새로운 값을 가져오는..
#catalog변수에서 잘못 저장된 값을 수정
catalog[-1] = ['성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀']

print(backup_catalog == catalog)
print('backup_catalog : ')
print(backup_catalog)
print()
print('catalog : ')
print(catalog)




# catalog = [
#     ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
#     ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
#     ['황금의 칼날', '비열한 간신', '무명의 영웅'],
#     ['성공의 열쇠', '내면의 변화', '목표의 달성'],
# ]

# ''' 
# 도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
# '성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
# '''