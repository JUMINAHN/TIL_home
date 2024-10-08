# 정문으로 걸어서 가장 짧은 거리에 있는 방 선호
# 걷는 거리가 가장 짧도록 방을 배정
# 각층에 W개의 방이 있는 H층 건물 W*H
# YY,XX 로 구성됨 => YY는 층수(H), XX는 넓이&가로 길이(W)
# W가 같을떄는 Y가 작은것을 기준으로 선호
# 결론적으로 맨 왼쪽부터 순서대로 배정됨
# N번쨰 손님에게 배정되어야하는 방 번호 출력
#문제를 푸는데 갑자기 희원 언니가 간단하게 생각하라고 했떤 부분이 생각이 남
'''
2
6 12 10 => 402
30 50 72 => 1203
'''
# import sys
#
# sys.stdin = open('input10250.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #N번쨰로 도착할 손님의 수
    H, W, N = map(int, input().split()) #높이 6, 가로 12, N번쨰 방문 손님
    #단순히 값을 대입하기 보다는 몫과 나머지로도 가능한 듯 하다..?
    YY = N % H
    XX = N // H
    if XX >= 9:
        print(f'{YY}{XX+1}') #9부터 해당되기 떄문에 XX가 10부터이면 안됨
    else :
        print(f'{YY}0{XX+1}')

#반례 
'''
1
10 10 100
정답은 1010
내 코드는 011
'''

