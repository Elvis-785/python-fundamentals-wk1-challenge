def count_vowel(text):
    count = 0
    # creating a set of vowels
    vowel = set("aeiouAEIOU")
    for alphabet in text:
        if alphabet in vowel:
            count = count+1
    return f"Number of vowels:{count}" 