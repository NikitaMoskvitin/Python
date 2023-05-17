def P(K,M):
    if M == 1:
        return K
    else:
        return P(K,M-1) + 2*K +2*M -3
K = int(input())
M = int(input())
print(P(K,M))
