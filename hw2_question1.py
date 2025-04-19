from pathlib import Path
import re

MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }

def english_to_morse(input_file="lorem.txt", output_file="lorem_morse.txt"):
    text = Path(input_file).read_text().upper()

    # Split the text into "words" using space or newline as delimiter
    word_chunks = re.split(r'[ \n]', text)

    # Convert each "word" into morse with no spaces between characters
    morse_words = [''.join(filter(None, map(MORSE_CODE.get, word))) for word in word_chunks]

    # Save to output file
    Path(output_file).write_text('\n'.join(morse_words))
if __name__ == "__main__":
    english_to_morse()

