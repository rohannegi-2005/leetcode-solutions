class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = ""
        for word in address:
            if word == ".":
                defanged = defanged + "["
                defanged = defanged + word
                defanged = defanged + "]"
            else:
                defanged = defanged + word


        return defanged

        