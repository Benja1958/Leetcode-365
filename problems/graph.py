
from typing import Optional, List
from collections import deque, defaultdict

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #initialialize a counter to keep track of number of islands
        #iterate through the grid while keeping track of visited boxes
        #use bfs to count number of islands
        #return the number of islands

        visited = set()
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        #implement bfs helper function to explore the size of an island
        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))
            directions = [[1,0], [0,1], [-1, 0], [0, -1]]

            while q:
                r, c = q.popleft()

                #get directions
                for x, y in directions:
                    r_x = r + x
                    c_y = c + y

                    if (0 <= r_x < rows) and (0 <= c_y < cols) and ((r_x, c_y) not in visited) and grid[r_x][c_y] == "1":
                        visited.add((r_x, c_y))
                        q.append((r_x, c_y))
                
            return




        #loop through the grid finding islands
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #we will explore those safe regions on the edge first
        #we will use bfs to explore
        #we will mark safe regions with "T" then will umark them later
        #final loop will be to change them back to "X" for unsafe regions

        rows = len(board)
        cols = len(board[0])

        def bfs(r, c):
            queue = deque([(r, c)])

            while queue:
                r, c = queue.popleft()
                board[r][c] = "T"

                directions = [[1,0], [0,1], [-1, 0], [0, -1]]

                for x, y in directions:
                    r_x = r + x
                    c_y = c + y
                    if (0 <= r_x < rows) and (0 <= c_y < cols) and board[r_x][c_y] == "O":
                        board[r_x][c_y] = "T"
                        queue.append((r_x, c_y))

        for r in range(rows):
            if board[r][0] == "O":
                bfs(r, 0)
            if board[r][cols - 1] == "O":
                bfs(r, cols - 1)
        
        for c in range(cols):
            if board[0][c] == "O":
                bfs(0, c)
            if board[rows-1][c] == "O":
                bfs(rows - 1, c)

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #will use bfs to solve since involves level traversal of the graph
        #will use a hashmap to do the cloning 
        if not node:
            return None
        old_to_new = {}
        queue = deque([node])
        old_to_new[node] = Node(node.val)

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                old_to_new[curr].neighbors.append(old_to_new[neighbor])
        return old_to_new[node]
    

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #we will build an graph adjcency list of the current element with all the divisons
        #then from that graph we will calculate all the queries in an iteration manner

        #a -> b -> c -> d with arrow being wights

        #build thw graph
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])

        #create a bfs helper function to trace the route and get the value from start to end
        def bfs(start, end):
            #first check if the points in the graph, return -1 immediately
            if start not in adj or end not in adj:
                return -1

            visited = set()
            queue = deque()
            queue.append([start, 1])
            visited.add(start)

            while queue:
                curr, weight = queue.popleft()

                if curr == end:
                    return weight

                for neig, val in adj[curr]:
                    if neig not in visited:
                        queue.append([neig, weight * val])
                        visited.add(neig)
            return -1


        #build up the final answer
        result = []
        for start, end in queries:
            val = bfs(start, end)
            result.append(val)
        return result


if __name__ == "__main__":
    sol = Solution()

    # ---------- numIslands ----------
    num_islands_tests = [
        {
            "grid": [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            "expected": 1,
        },
        {
            "grid": [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            "expected": 3,
        },
    ]

    for i, tc in enumerate(num_islands_tests, start=1):
        actual = sol.numIslands(tc["grid"])
        print(f"numIslands test {i}: {actual} | expected: {tc['expected']}")
        assert actual == tc["expected"], f"numIslands test {i} failed"

    print("All numIslands tests passed.")

    # ---------- solve (Surrounded Regions) ----------
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    expected_board = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]
    sol.solve(board)
    print(f"solve test: {board} | expected: {expected_board}")
    assert board == expected_board, "solve test failed"
    print("All solve tests passed.")

    # ---------- cloneGraph ----------
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    cloned = sol.cloneGraph(n1)

    def graph_signature(start: Optional[Node]) -> dict:
        if not start:
            return {}
        sig = {}
        visited = set()
        q = deque([start])
        visited.add(start)
        while q:
            curr = q.popleft()
            sig[curr.val] = sorted(nei.val for nei in curr.neighbors)
            for nei in curr.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return sig

    original_sig = graph_signature(n1)
    cloned_sig = graph_signature(cloned)
    print(f"cloneGraph test: {cloned_sig} | expected: {original_sig}")
    assert cloned_sig == original_sig, "cloneGraph structure mismatch"
    assert cloned is not n1, "cloneGraph failed: root node was not cloned"
    print("All cloneGraph tests passed.")

    # ---------- calcEquation ----------
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    expected = [6.0, 0.5, -1, 1, -1]

    actual = sol.calcEquation(equations, values, queries)
    print(f"calcEquation test: {actual} | expected: {expected}")
    assert actual == expected, "calcEquation test failed"
    print("All calcEquation tests passed.")
