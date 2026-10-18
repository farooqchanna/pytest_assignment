def reverse_string(text):
    return text[::-1]
def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")