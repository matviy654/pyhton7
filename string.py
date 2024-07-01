#task1
# def is_palindrome(s):
#     s = s.lower()
#     s = ''.join(char for char in s if char.isalnum())
#     return s == s[::-1]

# str = input("Введіть рядок: ")

# if is_palindrome(str):
#     print("Це паліндром.")
# else:
#     print("Це не паліндром.")
#task2
# def words2(text, words3):
#     words = text.split()
#     for i in range(len(words)):
#         word_clean = words[i].strip(".,!?;:")
#         if word_clean.lower() in words3:
#             words[i] = words[i].upper()
#     return ' '.join(words)
# text = input("Введіть текст: ")
# words3 = input("Введіть список зарезервованих слів через пробіл: ").split()
# words3 = [word.lower() for word in words3]
# text2 = words2(text, words3)
# print(text2)
#task3
# import re

# def count_sentences(text):
#     sentences = re.split(r'[.!?]', text)
#     count = sum(1 for sentence in sentences if sentence.strip())
#     return count

# text = input("Введіть текст: ")

# sentence_count = count_sentences(text)
# print("Кількість речень у тексті:", sentence_count)
#task4
