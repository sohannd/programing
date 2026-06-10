print("Paragraph Editor :)")

paragraph = input("Enter the Paragraph:")
replacing_word = input("Replacing Word:")
new_word = input("New Word:")

new_para = paragraph.replace(replacing_word, new_word)
print(new_para)