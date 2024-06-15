def main():
        path = "books/frankenstein.txt"
        the_book = get_book(path)
        total_words = get_word_count(the_book)
        letter_count_dict = get_letter_count_dict(the_book)
        sorted_dict_list = convert_dict_list(letter_count_dict)
        print_report(sorted_dict_list, total_words, path)

def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def get_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def get_letter_count_dict(text):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letter_count = {}
    for x in text:
        lower_case = x.lower()
        if lower_case in alphabet:
            if lower_case in letter_count:
                letter_count[lower_case] += 1
            else:
                letter_count[lower_case] = 1
    return letter_count

def print_report(sorted_dict_list, total_words, path):
    print(f"--- Begin report of {path}---")
    print(f"{total_words} words found in the document")
    print()
    for i in range(0, len(sorted_dict_list)):
        dict = sorted_dict_list[i]
        for i in dict:
            print(f"The '{i}' character was found {dict[i]}")
        # print(f"The {dict} character was found {}")
    print("--- End Report ---")

def convert_dict_list(dict):
    value = []    
    for i in dict:
       temp = {}
       temp[i] = dict[i]
       value.append(temp)
    value.sort(reverse=True, key=sort_on)
    return value

def sort_on(dict):
    for i in dict:
        return dict[i]
main()