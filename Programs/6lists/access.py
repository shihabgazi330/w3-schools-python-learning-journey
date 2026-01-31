this_list = ["apple", "banana", "jackfruit", "orange", "malta", "pineapple"]
print(this_list[1])
# negative indexing
print(this_list[-2]) #-1 refers to the last item, -2 refers to the second last item etc.

print(this_list[2:9]) # specify a range of indexes
# note that the list doesn't have items up until index 9 still it counts up until tpo the end

print(this_list[:3]) # By leaving out the start value, the range will start at the first item i.e. 0th index
print(this_list[3:]) # by leaving out the last value, the range will end at the last item i.e. len(list)th index
print(len(this_list))
print(this_list[-4:-1]) # returns the items from -4th item to, but NOT including -1th item

