from pprint import pprint

def letter_count(content: str) -> dict[str, int]:
  content: str = content.lower()
  word_counts: dict[str, int] = {}
  for i in "abcdefghijklmnopqrstuvwxyz":
    word_counts[i]: int = content.count(i)
  return word_counts

def main() -> None:
  with open("books/frankenstein.txt") as f:
    file_contents: str = f.read()
    words: list[str] = file_contents.split()
    word_counts: dict[str, int] = letter_count(file_contents)
    max_char = max(word_counts, key=word_counts.get)
    max_count = word_counts[max_char]
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words were found in the document\n")
    for letter, appearances in word_counts.items():
      print(f"The character \"{letter}\" appeared {appearances} times")
    print(f"\nCharacter \x1B[32m\"{max_char}\"\x1B[39m has appeared the most with \x1B[33m{max_count}\x1B[39m appearances") # Edit
    print("--- End report ---")

if __name__ == "__main__":
  main()