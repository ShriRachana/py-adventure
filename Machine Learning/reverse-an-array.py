# Reverse An Array- Reverse a given list of numbers.
# Example 1 : {"nums": [50, 35, 78, 66, 17]} || Output: [17, 66, 78, 35, 50]
# Example 2: {"nums": [50, 40, 30, 20]} || Output: [20, 30, 40, 50]

# Notes: Modify the input array in-place and return the modified array.
# Constraints:
# 1 <= size of the input array <= 106
# 0 <= any element of the input array <= 106
#==========================================================================
# Pseudo Code Provided : 
''' 
def reverse_array(nums):    
    Args:
     nums(list_int32)
    Returns:
     list_int32
    # Write your code here.
    return []
'''
#=========================================================================== 
# Attempt 1 : 
'''
lst = [10, 11, 12, 13, 14, 15]
lst.reverse()
print("Using reverse() ", lst) 
print("Using reversed() ", list(reversed(lst)))
'''
# ==========================================================================

# Submitted Code: 
#Max Exe Time : 0.03 sec
#Max Memory Used : 10.07 MB

def reverse_array(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     list_int32
    """
    nums.reverse()
    return nums