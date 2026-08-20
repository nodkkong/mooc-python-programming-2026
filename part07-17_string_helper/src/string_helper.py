# Write your solution here
def change_case(orig_string: str) -> str:
    result = ""
    for char in orig_string:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result

def split_in_half(orig_string: str) -> str:
    mid = len(orig_string) // 2
    return orig_string[:mid], orig_string[mid:]

def remove_special_characters(orig_string: str) -> str:
    result = ""
    for char in orig_string:
        if char.isalnum() or char == " ":
            result += char
    return result