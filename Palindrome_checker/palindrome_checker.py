def check_palindrome(): 
    """
    Function to check if a user-entered string is a palindrome.
    A palindrome reads the same forwards and backwards (e.g., "racecar", "A man a plan a canal Panama").
    """
    # Get input from the user
    user_input = input("Enter a string to check if it's a palindrome: ") 
     
    # Clean the input by removing spaces and converting to lowercase
    # This allows phrases like "A man a plan a canal Panama" to be recognized as palindromes
    
    cleaned_input = user_input.replace(" ", "").lower()

    # Check if the cleaned string is equal to its reverse
    # [::-1] creates a reversed copy of the string

    if cleaned_input == cleaned_input[::-1]:
        print("Yes, it is a palindrome.")
    else:
        print("No, it is not a palindrome.")

# Run the function or Execute the function when the script is run
check_palindrome()
