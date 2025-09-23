# word_count.py
import argparse

def count_words(text):
    return len(text.split())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="Text to count words in")
    args = parser.parse_args()
    print("Word count:", count_words(args.text))

if __name__ == "__main__":
    main()
