fruits = "apply, orange, banana, strawberry, grape"

# Give me a list of fruit in sorted order saying
# The fruits are
# An Apple.
# An Orange.
# ...



fruit_list = fruits.split(', ')



fruit_list[2] = "pear"


fruit_list.sort()



print "The fruits are"
for fruit in fruit_list:
    if fruit[0] in 'aeiou':   
        print "An %s." %fruit.capitalize()
    else:
        print "A %s." %fruit.capitalize()

words = []
for word in "IM YELLING AT YOU".lower().split():
    word_as_list = list(word)
    word_as_list[0] = word_as_list[0].upper()
    words.append("".join(word_as_list))
print " ".join(words)
