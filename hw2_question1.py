
MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',  'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',  'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',  'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',  'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',  'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---','3': '...--',
    '4': '....-', '5': '.....', '6': '-....','7': '--...',
    '8': '---..', '9': '----.'
}

def text_to_morse(input_file: str = "lorem.txt", output_file: str = "lorem_morse.txt"):
    """Convert an input text file to an output Morse code file."""

    with open(input_file, 'r') as infile:
        content = infile.read()


    morse_content = '\n'.join(map(lambda word: ' '.join(map(lambda char: MORSE_CODE.get(char.upper(), ''), word)), content.split()))

    with open(output_file, 'w') as outfile:
        outfile.write(morse_content)
    print(f"Morse Code Output:\n{morse_content}")
if __name__ == "__main__":
    text_to_morse()

