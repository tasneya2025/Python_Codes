#WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)  [1, 2, 3, 2, 1]   [1, “abc”, “abc”, 1]

# list1 = [1,2,3,2,1]
# list1_copy=list1.copy()
# list1_copy.reverse()


# if(list1==list1_copy):
#     print("its palindrome")
# else:
#     print("its not palindrome")   



list1 = [1, "abc", "abc", 1]
list1_copy=list1.copy()
list1_copy.reverse()


if(list1==list1_copy):
    print("its palindrome")
else:
    print("its not palindrome") 