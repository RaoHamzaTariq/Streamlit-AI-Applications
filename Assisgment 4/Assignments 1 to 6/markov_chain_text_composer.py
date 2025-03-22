import random
import re

class MarkovChainTextComposer:
    def __init__(self, order=1):
        """
        Initializes the Markov Chain Text Composer.

        Args:
            order (int, optional): The order of the Markov Chain.  Defaults to 1.
                Higher order chains consider longer sequences of words, leading to
                more context-aware but potentially less varied output.
        """
        self.order = order
        self.chain = {}
        self.text = None  # Store the input text
        self.words = [] #store the words

    def read_text(self, text):
        """
        Reads the input text and stores it for analysis.  Cleans the text
        by removing punctuation and converting to lowercase.

        Args:
            text (str): The input text to learn from.
        """
        # Remove punctuation and convert to lowercase
        text = re.sub(r'[^\w\s]', '', text).lower()
        self.text = text
        self.words = text.split()

    def build_chain(self):
        """
        Builds the Markov Chain from the stored text.  The chain is a dictionary
        where keys are tuples of 'order' words, and values are lists of
        possible next words.
        """
        if not self.text:
            raise ValueError("Please read text before building the chain.")

        self.chain = {}
        words = self.words
        for i in range(len(words) - self.order):
            key = tuple(words[i:i + self.order])
            next_word = words[i + self.order]
            if key in self.chain:
                self.chain[key].append(next_word)
            else:
                self.chain[key] = [next_word]

    def generate_text(self, length=200, seed=None):
        """
        Generates text using the Markov Chain.

        Args:
            length (int, optional): The length of the text to generate (in words).
                Defaults to 200.
            seed (str, optional):  A seed string to start the generation.
                If None, a random seed is chosen.  If a string, the last
                'order' words of the string are used as the seed.

        Returns:
            str: The generated text.

        Raises:
            ValueError: If the chain is empty or the seed is invalid.
        """
        if not self.chain:
            raise ValueError("The Markov chain is empty.  Please read text and build the chain first.")

        if not self.chain:
            raise ValueError("The Markov chain is empty.  Please read text and build the chain first.")

        if seed:
            seed_words = re.sub(r'[^\w\s]', '', seed).lower().split()
            if len(seed_words) < self.order:
                raise ValueError(f"Seed must contain at least {self.order} words.")
            seed_key = tuple(seed_words[-self.order:])  # Use the last 'order' words
            if seed_key not in self.chain:
                print("WARNING: Seed not found in chain. Using random seed.")
                seed_key = random.choice(list(self.chain.keys()))
        else:
            seed_key = random.choice(list(self.chain.keys()))

        generated_words = list(seed_key)  # Start with the seed
        for _ in range(length - self.order):
            if seed_key in self.chain:
                next_word = random.choice(self.chain[seed_key])
                generated_words.append(next_word)
                seed_key = tuple(generated_words[-self.order:])  # Update the seed
            else:
                # If the current key isn't in the chain, pick a random key to continue.
                # This helps prevent the generation from getting stuck.
                seed_key = random.choice(list(self.chain.keys()))
                generated_words.extend(list(seed_key))

        return ' '.join(generated_words)
    
    def get_chain(self):
        """
        Returns the built Markov Chain.

        Returns:
            dict: The Markov Chain dictionary.
        """
        return self.chain


def main():
    """
    Main function to run the Markov Chain Text Composer.
    """
    order = 2  # You can change the order here
    composer = MarkovChainTextComposer(order)

    # Get text from the user or a file
    text_source = input("Enter 'text' to input text directly or 'file' to read from a file: ").lower()
    if text_source == 'text':
        input_text = input("Enter your text: ")
        composer.read_text(input_text)
    elif text_source == 'file':
        filename = input("Enter the path to your text file: ")
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                input_text = f.read()
            composer.read_text(input_text)
        except FileNotFoundError:
            print(f"Error: File not found at {filename}")
            return
        except Exception as e:
            print(f"Error reading file: {e}")
            return
    else:
        print("Invalid input. Please enter 'text' or 'file'.")
        return

    composer.build_chain()

    # Display the Markov Chain (optional, for debugging or exploration)
    print("\nMarkov Chain:")
    print(composer.get_chain())

    # Get generation parameters from the user
    while True:
        try:
            length = int(input("Enter the desired length of the generated text (in words): "))
            if length <= order:
                print(f"Length must be greater than the Markov Chain order ({order}).")
                continue
            break  # Exit loop if length is valid
        except ValueError:
            print("Invalid input. Please enter an integer for the length.")

    seed = input("Enter a seed string (or leave blank to use a random seed): ")
    generated_text = composer.generate_text(length, seed)
    print("\nGenerated Text:")
    print(generated_text)

if __name__ == "__main__":
    main()
