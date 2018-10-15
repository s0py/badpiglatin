textfile = open('words.txt', 'r')
text = textfile.read().split('\n')

vowels = 'aeiouy'

print(text)
for line in text:
	output_list = []
	output_line = ''

	words_in_line = line.split()
	for word in words_in_line:
		letters = list(word)
		if letters[0] in vowels:
			letters.append('yay')
		else:
			for letter in letters:
				if letters[0] in vowels:
					break
				else:
					letters.append(letters[0])
					del letters[0]
			letters.append('ay')
		word = ''.join(letters)
		output_list.append(word)

	output_line = ' '.join(output_list)
	print(output_line)