class Solution:
    def clumsy(self, n: int) -> int:
        n_arr = []
        eval_arr = [n]

        for i in range(1, n):
            n_arr.append(i)

        for count in range(n-1):
            if count % 4 == 0:
                curr = eval_arr[-1] * n_arr[-1]
                n_arr.pop()
                eval_arr.pop()
            elif count % 4 == 1:
                curr = int(eval_arr[-1] / n_arr[-1])
                n_arr.pop()
                eval_arr.pop()
            elif count % 4 == 2:
                curr = n_arr[-1]
                n_arr.pop()
            else:
                curr = -n_arr[-1]
                n_arr.pop()
                
            eval_arr.append(curr)
        return sum(eval_arr)

print(Solution().clumsy(10))