def mergeAlternately(word1, word2):
    merged = ""
    i, j = 0, 0

    while i < len(word1) and j < len(word2):
        merged += word1[i] + word2[j]
        i += 1
        j += 1

    # Append the remaining characters from word1 and word2, if any
    while i < len(word1):
        merged += word1[i]
        i += 1

    while j < len(word2):
        merged += word2[j]
        j += 1

    return merged
