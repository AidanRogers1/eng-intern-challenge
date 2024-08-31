def is_braille(message):
    """
    Check if input is braille or english
    :param message: braille or english input string
    :return: returns true for braille, false for english
    """
    for item in message:
        if item not in (".", "O"):
            return False
    return True


def translate_to_braille(message):
    """
    Translate english strings to braille
    :param message: english input string
    """
    output = ""
    is_number = False

    for item in message:
        if item.isupper():
            output += ".....O"  # Check for capital
            item = item.lower()

        if item.isdigit():
            if not is_number:
                output += ".O.OOO"  # Check for number
                is_number = True
            output += list(number_translations.keys())[list(number_translations.values()).index(item)]
        else:
            if is_number:
                is_number = False  # Reset after numbers
            output += list(character_translations.keys())[list(character_translations.values()).index(item)]

    print(output)
    return


def translate_to_english(message):
    """
    Translate braille input strings to english
    :param message: braille input string
    """
    output = ""
    counter = 1
    capitalize = False
    number = False
    for x in range(len(message)):
        output += message[x]

        if counter % 6 == 0:          # Separate braille string into characters

            if output == ".O.OOO":    # Check for numbers
                number = True
            elif output == "......":  # Check for spaces
                number = False


            if capitalize:
                print(character_translations[output].capitalize(), end="")  # Print capitals
            elif number and output != ".O.OOO":
                print(number_translations[output], end="")  # Print numbers
            elif not number:
                print(character_translations[output], end="")  # Print lowercase

            if output == ".....O":  # Capitalize next character
                capitalize = True

            else:
                capitalize = False

            output = ""
        counter += 1


    return



character_translations = {

    "O.....": "a",  "O.O...": "b",  "OO....": "c",
    "OO.O..": "d",  "O..O..": "e",  "OOO...": "f",
    "OOOO..": "g",  "O.OO..": "h",  ".OO...": "i",
    ".OOO..": "j",  "O...O.": "k",  "O.O.O.": "l",
    "OO..O.": "m",  "OO.OO.": "n",  "O..OO.": "o",
    "OOO.O.": "p",  "OOOOO.": "q",  "O.OOO.": "r",
    ".OO.O.": "s",  ".OOOO.": "t",  "O...OO": "u",
    "O.O.OO": "v",  ".OOO.O": "w",  "OO..OO": "x",
    "OO.OOO": "y",  "O..OOO": "z",
    ".....O": "",  # Capital follows
    ".O.OOO": "",  # Number follows
    "......": " "  # Space

 }

number_translations = {

    "O.....": "1", "O.O...": "2", "OO....": "3",
    "OO.O..": "4", "O..O..": "5", "OOO...": "6",
    "OOOO..": "7", "O.OO..": "8", ".OO...": "9",
    ".OOO..": "0"

}


text = input()



if is_braille(text):
    translate_to_english(text)
else:
    translate_to_braille(text)
