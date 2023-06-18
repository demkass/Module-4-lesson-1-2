def is_palindrome(s):
    return s == s[::-1]

if is_palindrome(input("Введите Ваше слово: ")):
    print("True")
else:
    print("False")