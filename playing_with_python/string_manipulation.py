# capitalize()
text: str = 'hello'
print(text.capitalize()) # Hello

text = "HELLO"
print(text.capitalize()) # Hello

# casefold()
text = "MaRio"
print(text.casefold()) # mario


# center(): centers the text based on a given value
text = "Nacer"
print(text.center(20,"@")) # @@@@@@@Nacer@@@@@@@@: it basically occupies 20 spaces

# count()
text = "hello, it's me!, it's me again!!"
print(text.count("it's me")) # 2
