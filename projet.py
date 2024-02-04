from pyfiglet import Figlet

def generate_ascii_art(text, font='standard'):
    fig = Figlet(font=font)
    ascii_art = fig.renderText(text)
    return ascii_art

def print_available_fonts():
    print("Available Fonts:")
    for font in Figlet().getFonts():
        print(font)

if __name__ == "__main__":
    input_text = input("Enter text to convert into ASCII art: ")

    print_available_fonts()
    font_choice = input("Enter font (or press Enter for standard): ")

    if not font_choice :
        font_choice = 'standard'

    result = generate_ascii_art(input_text, font_choice)
    print(result)
