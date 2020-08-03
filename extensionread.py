user_input = input("\nENTER THE FILENAME TO CHECK EXTENSION : ")

if user_input.lower().endswith('.py') :
    print("\nTHE EXTENSION OF THE FILE IS 'PYTHON'.")

elif user_input.lower().endswith(('.png', '.jpg', '.jpng')):
    print("\nTHE EXTENSION OF THE FILE IS 'IMAGE'.")

elif user_input.lower().endswith('.html'):
    print("\nTHE EXTENSION OF THE FILE IS 'HTML'.")

elif user_input.lower().endswith('.rtf'):
    print("\nTHE EXTENSION OF THE FILE IS 'WORD DOCUMENT'.")

else:
    print("\nSORRY, FAILED TO RECOGNIZE THE EXTENSION OF THE FILENAME INPUTED.")
