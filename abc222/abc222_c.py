from sys import stdin

N, M = [int(x) for x in stdin.readline().rstrip().split()]
GCP = []
for _ in range(2 * N):
    GCP.append(list(stdin.readline().rstrip()))

rank = {}
for i in range(2 * N):
    rank[i] = 0
for m in range(M):
    m_rank = sorted(rank.items(), key=lambda x: (-x[1], x[0]))
    for k in range(N):
        a = m_rank[2 * k][0]
        b = m_rank[2 * k + 1][0]
        a_gcp = GCP[a][m]
        b_gcp = GCP[b][m]
        if a_gcp == b_gcp:
            continue
        elif (a_gcp == 'G' and b_gcp == 'C') or (a_gcp == 'C' and b_gcp == 'P') or (a_gcp == 'P' and b_gcp == 'G'):
            rank[a] += 1
        else:
            rank[b] += 1

for it in sorted(rank.items(), key=lambda x:(-x[1], x[0])):
    print(it[0] + 1)
