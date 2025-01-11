from collections import Counter
import re

def count_words_in_file(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the contents of the file
            text = file.read()

            # Convert text to lowercase and split it into words using regular expressions
            words = re.findall(r'\b\w+\b', text.lower())

            
            word_counts = Counter(words)

            
            sorted_word_counts = dict(sorted(word_counts.items()))

            
            for word, count in sorted_word_counts.items():
                print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = file_path = r"C:\Users\rouna\OneDrive\Desktop\cognifyz\sample.txt"
 # Replace with the path to your text file
    count_words_in_file(file_path)
