def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	chars_dict = get_chars_dict(text)
	format_report(book_path, num_words, chars_dict)

def get_num_words(text) -> int:
	count = text.split()
	return len(count)

def get_chars_dict(text) -> {}:
	chars = {}

	for char in text:
		lower_char = char.lower()
		if lower_char in chars:
			chars[lower_char] += 1
		else:
			chars[lower_char] = 1

	return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]

def format_report(path, num_words, chars_dict):
	char_list = []
	for char in chars_dict:
		if char.isalpha():
			char_list.append({"name": char, "num": chars_dict[char]})

	char_list.sort(reverse=True, key=sort_on)

	report = f"""
--- Begin report of {path} ---
{num_words} words found in the document
	"""

	for char in char_list:
		report = report + f"\n The '{char["name"]}' character was found {char["num"]} times"

	report = report + "\n --- End report ---"
	print(report)

if __name__ == "__main__":
    main()
