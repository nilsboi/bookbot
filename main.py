def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    count(file_contents)
    count_chars(file_contents)


def count(txt):
  words = txt.split()
  print(len(words))
  
def count_chars(txt):
  dic_count = {}
  for char in txt:
    char = char.lower()
    if char not in dic_count:
        dic_count[char] = 1
    else:
        dic_count[char] += 1
  print(dic_count)
  
main()