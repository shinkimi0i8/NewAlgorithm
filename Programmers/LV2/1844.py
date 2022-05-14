from collections import deque


def solution(maps):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    N = len(maps[0])
    M = len(maps)
    visited = [[-1 for _ in range(N)] for _ in range(M)]
    visited[0][0] = 1
    queue = deque()
    queue.append((0, 0))
    while queue:
        cy, cx = queue.popleft()
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if 0 <= ny < M and 0 <= nx < N:
                if visited[ny][nx] == -1 and maps[ny][nx] == 1:
                    visited[ny][nx] = visited[cy][cx] + 1
                    queue.append((ny, nx))
    return visited[-1][-1]


print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1],
        ]
    )
)
