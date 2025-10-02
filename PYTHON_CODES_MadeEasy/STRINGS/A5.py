def merge_alternatively(str1, str2):
    merged = ""
    index = 0
    len1 = len(str1)
    len2 = len(str2)
    
    # Loop through both strings
    while index < len1 or index < len2:
        if index < len1:
            merged += str1[index]
        if index < len2:
            merged += str2[index]
        index += 1

    return merged

# Example
string1 = "abc"
string2 = "12345"
result = merge_alternatively(string1, string2)
print(result)  # Output: "a1b2c345"
