class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def generate(nums, n, st):
            if (len(st) == n):
                ans.append(st.copy())
                return
            
            for i in range(len(nums)):
                st.append(nums[i]);
                tmp=nums[:]
                tmp.remove(nums[i])
                generate(tmp, n, st)
                st.pop()
            
        ans=[]
        generate(nums, len(nums), [])
        return ans