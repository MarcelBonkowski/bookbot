def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	chars_dict = get_chars_dict(text)
	print(chars_dict)

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

if __name__ == "__main__":
    main()
