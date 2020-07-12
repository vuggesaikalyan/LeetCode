class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        solution=[]
        self.combinationSumRec(candidates, target, 0, 0, [], solution)
        return solution

    def combinationSumRec(self, candidates, target, index, sum, listT, solution):
        if sum == target:
            solution.append(list(listT))
        for i in range(index,len(candidates)):
            if sum + candidates[i] > target:
                break;
            listT.append(candidates[i])
            self.combinationSumRec(candidates, target, i, sum+candidates[i], listT, solution)
            listT.pop()