from collections import namedtuple

Animal = namedtuple("Animal", "name, phrase, extra, ladykiller", defaults=["", "", False])
chain = [
    Animal("fly"),
    Animal(
        "spider",
        "It wriggled and jiggled and tickled inside her.",
        extra=" that wriggled and jiggled and tickled inside her",
    ),
    Animal("bird", "How absurd to swallow a bird!"),
    Animal("cat", "Imagine that, to swallow a cat!"),
    Animal("dog", "What a hog, to swallow a dog!"),
    Animal("goat", "Just opened her throat and swallowed a goat!"),
    Animal("cow", "I don't know how she swallowed a cow!"),
    Animal("horse", "She's dead, of course!", ladykiller=True),
]


def recite(start_verse: int, end_verse: int) -> list[str]:
    verses: list[str] = []
    for n in range(start_verse, end_verse + 1):
        if verses:
            verses += [""]
        verses += verse(n - 1)
    return verses


def verse(n: int) -> list[str]:
    lines: list[str] = []
    animal = chain[n]
    lines += i_know(animal)
    if not animal.ladykiller:
        for i in range(n, 0, -1):
            lines += hunt(chain[i], chain[i - 1])
        lines += i_dont_know()
    return lines


def i_know(animal: Animal) -> list[str]:
    lines = [f"I know an old lady who swallowed a {animal.name}."]
    if animal.phrase:
        lines.append(animal.phrase)
    return lines


def hunt(predator: Animal, prey: Animal) -> list[str]:
    return [f"She swallowed the {predator.name} " f"to catch the {prey.name}{prey.extra}."]


def i_dont_know() -> list[str]:
    return ["I don't know why she swallowed the fly. Perhaps she'll die."]
