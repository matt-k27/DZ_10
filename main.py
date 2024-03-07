import keyword
import string

print('DZ10')

inputtedText = str(input('Enter your name of variable pls: '))
result = True

if inputtedText[0].isdigit() or inputtedText.isdigit() or inputtedText in keyword.kwlist:
    result = False

for char in inputtedText:
    if (char in string.punctuation and char != '_') or char == ' ' or char.isupper():
        result = False

print(result)

print('Thank you for using')

###########################################################

# inputtedText = str(input('Enter your text pls: '))
# result = True
#
# if inputtedText[0].isdigit() or inputtedText.isdigit():
#     result = False
#
# for char in inputtedText:
#     if (char in string.punctuation and char != '_') or char == ' ' or char.isupper():
#         result = False
#
# if inputtedText in keyword.kwlist:
#     result = False
#
# print(result)
#
# print('Thank you for using')