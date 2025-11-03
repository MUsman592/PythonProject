
#          ____________________________________________________________________________________
 
"""
                     . You know what strings are but you must also know string
                       take more space than other data types like int, float etc
                     . This happens because String stores every character with
                       their own Unicode
                     . is a universal character encoding standard that
                       assigns a unique number (code point) to every character,
                       regardless of language
                     . Like “A” unicode is 65 and “ ” this emoji unicode is 128522,
                       you can check them by using ord() function in python and
                       convert them back using chr() function.   
   
"""

block = "A"
print(ord(block))     # ord use to convert char into unicode


block1 = 65
print(chr(65))        # chr use to convert unicode into char

#           ____________________________________________________________________________________