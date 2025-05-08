def num_operations(num1, num2):
    #Makes sure numbers are valid
    if not (isinstance(num1, (int, float)) or not (isinstance(num2, (int, float)))): 
        print("Error: Both inputs must be numbers")
        return None
    
    #Checks for Zero and if it is found it gives out the answer that zero was found
    if num1 == 0 or num2 == 0:
        return "Zero Found"
    
    # Handles the positive number case which makes it display the larger number and makes it display as many times as the lower number is 
    if num1 > 0 and num2 > 0:
        display_num = max(num1,num2)
        repition_count = min(num1, num2)
        for i in range(int(repition_count)):
            print(display_num)
        return None
    
    #Handles Negative Number case stuff
    return abs(num1 - num2)




print(num_operations(2, 3))  # prints 5 three times
print(num_operations(0, 10))  # returns "Zero found"
print(num_operations(-5, 3))  # returns 8 (absolute difference)




#OLD CODE USED FOR REFERENCE 
#     if num1 > num2:
#       for i in range(num2):
#         print(num1)
#     else:
#       for j in range(num1):
#         print(num2)
#   elif num1 == 0 or num2 == 0:
#       return "Zero found"
#   else:
#       if num1 < num2:
#           return num1 - num2
#       else:
#           return num2 - num1
      
