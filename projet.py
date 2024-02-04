from pyfiglet import Figlet

def generate_ascii_art(text, font='standard'):
    try:
        fig = Figlet(font=font)
        ascii_art = fig.renderText(text)
        return ascii_art
    except UnicodeEncodeError:
        print("Error: Unable to render ASCII art due to encoding issues. Try using a different font.")
        return ""

def print_available_fonts():
    print("Available Fonts:")
    for font in Figlet().getFonts():
        print(font)

if __name__ == "__main__":
    input_text = input("Enter text to convert into ASCII art (include special characters like ° or ç): ")

    print_available_fonts()
    font_choice = input("Enter font (or press Enter for standard): ")

    if not font_choice or font_choice not in Figlet().getFonts():
        font_choice = 'standard'

    result = generate_ascii_art(input_text, font_choice)
    print(result)
