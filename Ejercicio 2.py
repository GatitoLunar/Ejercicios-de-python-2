def mas_larga(lst):
	word_a = lst[0]
	for word in lst:
		if len(word) > len(word_a):
			word_a = word
	return word_a

new_list = ["Tu", "vieja", "puta", "hahaha", "xddddddddd"]
print(mas_larga(new_list))
input()
