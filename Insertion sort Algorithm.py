# Insertion Sort Algorithm in Monotonically Decreasing Order

# Function to perform insertion sort
def insertion_sort(arr):
    # Looping through the array starting from the second element
    for i in range(1, len(arr)):
        # The element to be compared and inserted in the sorted portion
        key = arr[i]
        
        # Initializing j to the last element of the sorted portion
        j = i - 1
        
        # Shifting elements of arr[0..i-1] that are smaller than key to one position ahead
        # This creates space for the key element
        while j >= 0 and arr[j] < key:  # Change '<' to '>' for decreasing order
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key element at its correct position
        arr[j + 1] = key

    return arr

# Example usage
if __name__ == "__main__":
    # Taking user input for the array
    user_input = input("Enter numbers separated by spaces: ")
    
    # Converting the input string into a list of integers
    input_array = list(map(int, user_input.split()))
    
    # Calling the function to sort the array in decreasing order
    sorted_array = insertion_sort(input_array)
    
    # Printing the sorted array
    print("Sorted array in decreasing order:", sorted_array)
