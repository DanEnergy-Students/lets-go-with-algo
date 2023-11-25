# def expo_search(lst, T_no: list):
#     so_list= lst.sorted
#     if len(lst)==0:
#         return f'this is a null  list'
#     i=0
#     while i<len(lst):

def binary_search(arr, left, right, x):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, left, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, right, x)
    else:
        return -1

def exponential_search(arr, x):
    if len(arr) == 0:
        return -1
    if arr[0] == x:
        return 0
    index = 1
    while index < len(arr) and arr[index] <= x:
        index *= 2
    return binary_search(arr, index // 2, min(index, len(arr)-1), x)

# Example usage:
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40,50,60,75,79,100]
    x = 75
    result = exponential_search(arr, x)
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in array")
        
    
    