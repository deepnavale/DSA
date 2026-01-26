class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff = arr[1]-arr[0]
        ans = []
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]<mindiff:
                ans  = [[arr[i-1],arr[i]]]
                mindiff = arr[i]-arr[i-1]
            elif arr[i]-arr[i-1]==mindiff:
                ans.append([arr[i-1],arr[i]])
        return ans
            
                
            