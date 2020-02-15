class Solution(object):
    def twoSum(self, nums, target):
        x = 'false'
        for i in range(len(nums)) :
            j=i+1
            if x != 'True' :
                    
                    for j in range(len(nums)) :
                        if nums[i]+nums[j] == target and i != j  :
                            SolutionList = [i,j]
                            i = len(nums) 
                            return(SolutionList)
                            x='True'
                            break
                        else :
                            pass   
            else :
                break           
        
nums= [2,7,11,15]
target= 9
S=Solution()       
S1 = S.twoSum(nums,target)
print(S1)