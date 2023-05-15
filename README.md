# Morse Code Decoder

This repository contains a simple Python script named `decode_morse.py` that decodes Morse code input. The script reads an input Morse code consisting of "." and "_" characters without spaces and tries to iterate through all possible words that the message can contain. Please note that for longer inputs, the decoding process may be slow.

The script uses a Portuguese dictionary named `palavras.txt` to determine all possible words in Portuguese that match the decoded Morse code.

## Usage

1. Clone the repository: `git clone https://github.com/senajoaop/decodificador_morse.git`
2. Navigate to the project directory: `cd decodificador_morse`
3. Run the Python script: `python decode_morse.py`
4. Enter the Morse code without spaces when prompted.
5. The script will attempt to decode the Morse code and display all possible word combinations in Portuguese.

Please note that the script assumes that the Morse code input follows the standard "." and "_" characters. Any deviation from this format may result in unexpected behavior.

## Contributing

Contributions to this repository are welcome! If you have any improvements, suggestions, or bug fixes, please feel free to contribute by following these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add your commit message"`
4. Push the branch to your forked repository: `git push origin feature/your-feature-name`
5. Open a pull request to the main repository.

Please ensure that your contributions align with the existing coding style and best practices.
