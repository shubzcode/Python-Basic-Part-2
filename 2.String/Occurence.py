# Count the Occurrences of a Specific Character in a String
def count_occurrences(string, character):
    count = 0
    for c in string:
        if c == character:
            count += 1
    return count


print(count_occurrences("hello world", "w"))
