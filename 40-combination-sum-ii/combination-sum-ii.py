class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def generate(candidates, target, current, index, result):
            if sum(current) == target:
                result.append(current[:])
                return
            if index >= len(candidates):
                return
            if sum(current) > target:
                return

            # exclude
            next_index = index
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1
            generate(candidates,target, current, next_index, result)

            # include
            current.append(candidates[index])
            generate(candidates,target, current, index + 1, result)
            current.pop()

        def combinations(target, candidates):
            result = []
            generate(candidates, target, [], 0, result)
            return result

        result = combinations(target, candidates)

        return result

        



        