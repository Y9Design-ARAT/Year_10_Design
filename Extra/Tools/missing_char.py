def missing_char(str, n):
  
  newStr = ""
  newStr = str[0:n] + str[n + 1: len(str)] 
  #this piece of code will allow the computer to find the
  #correct index that will be removed
 
  return newStr

#this command is what will give us the final product