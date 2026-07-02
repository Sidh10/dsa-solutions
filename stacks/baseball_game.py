class Solution:
    def calPoints(self, operations: List[str]) -> int:
        list_sol = []
        for i in operations:
            if i == "C":
                list_sol.pop()
                continue
            if i =="D":
                if list_sol:
                  x = int(list_sol[-1])*2
                  list_sol.append(x)
                  continue
            if i== "+":
                if len(list_sol)>=2:
                  sum_val = int(list_sol[-1])+int(list_sol[-2])
                  list_sol.append(sum_val)
                  continue
                else: 
                    return False
            list_sol.append(int(i))
        total_sum = sum(list_sol)
        return total_sum