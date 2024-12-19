from random import randint
from sty import fg, FgRegister

def generate_rgb() -> tuple[int]:
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    return red, green, blue


def generate_fg_color(red:int, green:int, blue:int) -> FgRegister:
    return fg(red, green, blue)

red, green, blue = generate_rgb()
random_fg_color = generate_fg_color(red, green, blue)
print(random_fg_color, 'Hello World!', fg.rs)

# Version avancée
# print(generate_fg_color(*generate_rgb()), 'Hello World!', fg.rs)
