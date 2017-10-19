def max_in_list(lst):
	ret_value = lst[0]
	for i in range(len(lst) - 1):
		if ret_value < lst[i + 1]:
			ret_value = lst[i + 1]
	return ret_value

new_list = [0,3,96,5,4]
print(max_in_list(new_list))
input()