def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    give_report(words)

def count_words(words):
    return len(words)
def dic_characters(words):
    dic ={}
    for c in words:
        lower_word=c.lower()
        for l in lower_word:
            if l in dic:
                dic[l] = dic[l]+1
            else:
                dic[l] = 1
    return dic

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def give_report(words):
    number_of_words = count_words(words)
    dic = dic_characters(words)
    chars_sorted_list = chars_dict_to_sorted_list(dic)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")


main()
