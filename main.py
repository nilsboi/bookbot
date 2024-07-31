def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    
    dict_words = count(file_contents)
    dict_count = count_chars(file_contents)
    print_report(dict_count, dict_words)


def count(txt):
  words = txt.split()
  return len(words)
  
def count_chars(txt):
  dic_count = {}
  for char in txt:
    char = char.lower()
    if char not in dic_count:
        dic_count[char] = 1
    else:
        dic_count[char] += 1
  return dic_count
 
def sort_on(dict):
    return dict["num"]
   
def print_report(dict, dict_words):
  list_chars = []
  for key in dict:
    list_chars.append({
      "char": key,
      "num": dict[key]
    })
     
  list_chars.sort(reverse=True, key=sort_on)
  
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{dict_words} words found in the document")
  for i in list_chars:
    char = i["char"]
    count = i["num"]
    if char.isalpha():
      print(f"The '{char}' character was found {count} times")
  print("--- End report ---")
  
main()