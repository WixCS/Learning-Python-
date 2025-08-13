#Write a program to fill in a letter template given below with name and date

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","Prince").replace("<|Date|>","25th April 2025"))