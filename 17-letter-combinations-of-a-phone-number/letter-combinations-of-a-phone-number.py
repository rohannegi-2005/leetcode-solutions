class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        thisdict = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]   
        }

        def generate(digits, current, result, index):
            
            # base case
            if index == len(digits):
                result.append(current)
                return
            
            letters = thisdict[digits[index]]
           
            for ch in letters:
                generate(digits, current + ch, result, index + 1)

        def generate_pairs(digits):
            result = []
            
            generate(digits, "", result, 0)
            return result

        return generate_pairs(digits)