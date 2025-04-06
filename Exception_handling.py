# try:
#     input = input("Enter a string: ")
#     result = input[::-1]
#     print(f"Reversed string is {result}.")
# except ValueError:
#     print("Input cannot be empty!")    
try:
    user_input = input("Enter a string: ").strip()
    if not user_input:
        raise ValueError("Input cannot be empty!")
    print("Reversed string:", user_input[::-1])
except ValueError as e:
    print("Error:", e)