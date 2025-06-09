text = input('ensert a sentence or paragraph:  ')
words = text.lower().split()
total_words = len(words)
print("Total Words:  " + str(total_words))

freq_word = {}
for word in words:
    if word in freq_word:
        freq_word[word] += 1
    else:
        freq_word[word] = 1
print('    word frequencies') 
for word in freq_word:
    print(word + ": " + str(freq_word[word]))  

most = ''
appears = 0
for word in words:
    if freq_word[word] > appears:
        most = word
        appears = freq_word[word]
print("The most repeated word is: " + most +  "  appears: " + str(appears )+ " times")        
         
