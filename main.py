# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

output = dict()

def read_file_content(filename):
    filename = open(filename,'r')
    return filename

def count_words():   
    text = read_file_content("./story.txt")
    for line in text:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
    
        for word in words:
            if word in output:
                output[word] = output[word] + 1
            else:
                output[word] = 1
    print(output)

count_words()