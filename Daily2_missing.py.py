def missing(array):
    for i in range(1 , len(array)+2):
        if i not in array:
            return i

#Test case 1
arr1 = [1,2,4,5]
print("Missing element from Array1 is : " , missing(arr1))

#Test case 2
arr2 = [2,3,4,5]
print("Missing element from Array2 is : " ,missing(arr2))

#Test case 3
arr3 = [1,2,3,4]
print("Missing element from Array3 is : " ,missing(arr3))

#Test case 4
arr4 = [1]
print("Missing element from Array4 is : " ,missing(arr4))





   




