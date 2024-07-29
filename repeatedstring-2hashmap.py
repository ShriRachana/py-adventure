# Python implementation
 
# Function returns word with highest frequency
def findWord(arr):
   
    # Create HashMap to store word and it's frequency
    hs = {}
 
    # Iterate through array of words
    for i in arr:
        if(i in hs):
            hs[i] += 1
        else:
            hs[i] = 1
    key = ""
    value = 0
    for i in hs:
       
        # Check for word having highest frequency
        if(hs[i] > value):
            value = hs[i]
            key = i
 
    # Return word having highest frequency
    return key
 
if __name__ == "__main__":
    arr = ["geeks","for","geeks","a","portal", "to","learn","can","be","computer","science","zoom","yup","fire","in","be","data","geeks"]
    sol = findWord(arr)
     
    # Print word having highest frequency
    print(sol)
    