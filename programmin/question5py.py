filename = 'example.txt'  
word = 'search_word' 

def search_word_in_file(filename, word):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
        for line_number, line in enumerate(lines, start=1):
            if word in line:
                print(f"Line {line_number}: {line.strip()}")
                
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {filename}.")

search_word_in_file(filename, word)






