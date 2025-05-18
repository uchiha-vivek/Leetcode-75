class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, current, total):
            if total == target:
                res.append(current.copy())
                return

            if i >= len(candidates) or total > target:
                return

            # Include candidates[i]
            current.append(candidates[i])
            dfs(i, current, total + candidates[i])
            current.pop()

            # Skip candidates[i]
            dfs(i + 1, current, total)

        dfs(0, [], 0)
        return res

if __name__ == "__main__":
    sol = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    ans = sol.combinationSum(candidates, target)  # ✅ Pass 'target', not 'sum'
    print(ans)
