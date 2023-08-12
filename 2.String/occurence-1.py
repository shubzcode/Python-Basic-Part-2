#Count the Occurrences of a Specific Character in a String 
def count_occurrences(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

input_string = input("Enter a string: ")
search_char = input("Enter a character to count: ")

occurrences = count_occurrences(input_string, search_char)
print(f"The character '{search_char}' appears {occurrences} times in the string.")