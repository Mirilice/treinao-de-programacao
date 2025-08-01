class Solution(object):
    def maxSubArray(self, nums):
        maxAtual = maxGlobal = nums[0]
        for i in range(1, len(nums)):
            maxAtual = max(nums[i], maxAtual + nums[i])
            #verifica se o proximo numero vai prejudicar a soma 
            maxGlobal = max(maxGlobal, maxAtual)
            #atualiza maxGlobal
#Algoritmo de Kadane
        return maxGlobal