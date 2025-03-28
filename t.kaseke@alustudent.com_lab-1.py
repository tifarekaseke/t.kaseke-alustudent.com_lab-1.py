import re

class Essay:
    def __init__(self, file_path):
        self.words = self.load_words(file_path)

    def load_words(self, file_path):
        """Load the essay from a file and return a set of words."""
        with open(file_path, 'r') as file:
            text = file.read()
        return self.clean_and_split(text)

    def clean_and_split(self, text):
        """Remove punctuation and split the text into a set of words."""
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        return set(text.lower().split())      # Convert to lowercase and use a set

class PlagiarismDetector:
    def __init__(self, essay1, essay2):
        self.essay1 = essay1
        self.essay2 = essay2

    def find_common_words(self):
        """Finds common words between the two essays."""
        return self.essay1.words & self.essay2.words  # Set intersection

    def search_word(self, word):
        """Check if a specific word is in either essay."""
        return word in self.essay1.words or word in self.essay2.words

    def calculate_plagiarism_percentage(self):
        """Calculates the plagiarism percentage."""
        unique_words = self.essay1.words | self.essay2.words  # Union
        common_words = self.essay1.words & self.essay2.words   # Intersection

        if len(unique_words) == 0:
            return 0
        return (len(common_words) / len(unique_words)) * 100

def main():
    # Load essays from text files
    essay1 = Essay('essay1.txt')
    essay2 = Essay('essay2.txt')

    # Create a plagiarism detector
    detector = PlagiarismDetector(essay1, essay2)

    # Find and print common words
    common_words = detector.find_common_words()
    print("Common Words:", common_words)
    print("Count of Common Words:", len(common_words))

    # Search for a specific word
    search_term = input("Enter a word to search for: ").lower()
    found = detector.search_word(search_term)
    print(f"Is the word '{search_term}' found? {'Yes' if found else 'No'}")

    # Calculate and print plagiarism percentage
    plagiarism_percentage = detector.calculate_plagiarism_percentage()
    print(f"Plagiarism Percentage: {plagiarism_percentage:.2f}%")
    if plagiarism_percentage >= 50:
        print("Plagiarism Detected")
    else:
        print("No Plagiarism Detected")

if __name__ == "__main__":
    main()
