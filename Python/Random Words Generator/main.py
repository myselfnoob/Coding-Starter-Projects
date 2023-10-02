import requests

def fetch_random_words(num_words):
    url = f"https://random-word-api.herokuapp.com/word?number={num_words}"
    response = requests.get(url)
    if response.status_code == 200:
        words = response.json()
        return words
    else:
        print("Failed to fetch random words. Please try again later.")
        return []

def main():
    try:
        num_words = int(input("Enter the number of words to generate: "))
        if num_words <= 0:
            print("Please enter a positive number of words.")
            return

        words = fetch_random_words(num_words)

        if words:
            print("Random words:")
            for word in words:
                print(word)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
