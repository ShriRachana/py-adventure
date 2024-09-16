class Solution:
    def twoSum(self, nums: list[int], target: int)-> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
        #Return an empty list if no solution is available. 
        return[]
    
def main():
    nums_input = input("Enter the numbers (separated by spaces): ")
    nums = list(map(int, nums_input.split()))

    target = int(input("Enter the target: "))

    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)

if __name__ == "__main__":
    main()