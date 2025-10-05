def word_frequency(text):  
    # Convert to lowercase  
    text = text.lower()  
      
    # Remove punctuation  
    for char in "!?,.;:'\"()-":  
        text = text.replace(char, "")  
      
    # Split into words  
    words = text.split()  
      
    # Count frequencies  
    freq = {}  
    for word in words:  
        freq[word] = freq.get(word, 0) + 1  
      
    return freq  
  
  
# Example usage  
text_input = "Python is fun and Python is powerful. Fun is good!"  
result = word_frequency(text_input)  
  
# Display results  
for word, count in result.items():  
    print(f"{word}: {count}")  
