
#What this code does is, if the numerical value is even 
#result will be true, else result is false.
def isEven(a):

	if a % 2 == 0:
		return True

	return False
	
#tests the function
print (0)
print (3)
print (111)

################################################################

def first_last6(nums):

  if (nums[0] == 6):
    return True
  
  if (nums[len(nums) -1] == 6):
    return True
  
  return False

################################################################