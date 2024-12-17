import string
from collections import Counter

fhandle=open("File.txt",'r') #please put File.txt in the same file folder as your code
st=fhandle.read()  # all words have been loaded to the string variable st
fhandle.close() # end/ close file

##### Task 1 #####
# remove punctuations, save your results to a new string variable my_st and display this new string (print)
def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)
my_st = [remove_punctuation(st) for text in st]
print(my_st)

##### Task 2: Frequency Counter ######

words = st.lower().split()
count = Counter(words)
print(count)

##### Task 3 #####
# remove duplicated words, capitalize the first letter of all words, and save as a new variable unique_upper_words

words = st.split()
print (" ".join(sorted(set(words), key=words.index)))

unique_upper_words = [word.capitalize() for word in words]
print(unique_upper_words)
