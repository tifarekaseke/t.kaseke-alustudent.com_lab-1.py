class Essay:
    def __init__(self, text):
        self.words = self.clean_and_split(text)

    def clean_and_split(self, text):
        """Remove punctuation and split the text into a set of words."""
        cleaned_text = ''
        for char in text:
            if char.isalnum() or char.isspace():  # Keep alphanumeric characters and spaces
                cleaned_text += char.lower()  # Convert to lowercase
        return set(cleaned_text.split())  # Convert to a set of words

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
    # Loading content of file 1 and file 2
    with open("essay-1.txt", "r") as file_1:
        data_1 = file_1.read().lower()

    with open("essay-2.txt", "r") as file_2:
        data_2 = file_2.read().lower()

    # Create Essay objects from the loaded data
    essay1 = Essay(data_1)
    essay2 = Essay(data_2)

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
