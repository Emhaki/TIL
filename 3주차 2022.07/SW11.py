# # 1989. 초심자의 회문 검사 D2

# "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

# 단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.


# [제약 사항]

# 각 단어의 길이는 3 이상 10 이하이다.


# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에 하나의 단어가 주어진다.


# [출력]

# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

from posixpath import split


T = int(input())
S = []
K = []
for i in range(1, T+1):
    N = str(input())
    for j in N:
        S.append(j)
        Y = S.reverse()
    for k in S:
        K.append(k)
    if S == K:
        print("#%d" % i, end=" ")
        print(1)
    else:
        print("#%d" % i, end=" ")
        print(0)
