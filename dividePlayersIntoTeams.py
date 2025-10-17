class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        totalChemistry = 0
        
        targetTeamSkill = skill[0] + skill[-1]
        currentTeamSkill = 0
        
        for i in range(n // 2):
            if skill[i] + skill[-i-1] != targetTeamSkill:
                return -1
            totalChemistry += skill[i] * skill[-i-1]               

        return totalChemistry
        