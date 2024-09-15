#보유하고 있지 않을 경우 특정 문자열을 출력하도록 한다
list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]


all_have = True
for rental in rental_list:
    if rental in list_of_book:
        continue
    else:
        all_have = False
        print(f'{rental} 은/는 보유하고 있지 않습니다.')
        break

if all_have:
    print('모든 도서가 대여 가능한 상태입니다.')


# rental_list = [
#     '장화홍련전',
#     '가락국 신화',
#     '온달 설화',
#     '금오신화',
#     '이생규장전',
#     '만복자서포기',
#     '수성지',
#     '백호집',
#     '원생몽유록',
#     '홍길동전',
#     '장생전',
#     '도문대작',
#     '옥루몽',
#     '옥련몽',
# ]

#보유하지 않은 함수 뽑아내기,,
#하나씩 뽑아내야하지 않을까 -> rental_list에 있는게 list_of_book에 없는지 확인하는 것
#뽑아내는 것은 rental_list만 하면 됨